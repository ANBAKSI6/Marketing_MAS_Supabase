
import streamlit as st
import asyncio
from supabase_client import supabase
from graph.graph import graph
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="Chatbot", layout="wide")

#  AUTH CHECK
if "user" not in st.session_state:
    st.warning("Please login first")
    st.switch_page("pages/2_Login.py")

user = st.session_state.user

#  SIDEBAR
with st.sidebar:
    st.markdown("## 👤 User")
    st.write(user.email)

    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("pages/2_Login.py")

    st.markdown("---")

    if st.button("➕ New Chat"):
        convo = supabase.table("conversations").insert({
            "user_id": user.id,
            "title": "New Chat"
        }).execute()

        st.session_state.conversation_id = convo.data[0]["id"]
        st.rerun()

#  CREATE CONVERSATION
if "conversation_id" not in st.session_state:
    convo = supabase.table("conversations").insert({
        "user_id": user.id,
        "title": "New Chat"
    }).execute()

    st.session_state.conversation_id = convo.data[0]["id"]

#  LOAD MESSAGES
msgs = supabase.table("messages").select("*") \
    .eq("conversation_id", st.session_state.conversation_id).execute()

st.session_state.messages = []

for m in msgs.data:
    if m["role"] == "user":
        st.session_state.messages.append(HumanMessage(content=m["content"]))
    else:
        st.session_state.messages.append(AIMessage(content=m["content"]))

#  DISPLAY CHAT
st.markdown("## 💬 Marketing Assistant")

for m in st.session_state.messages:
    with st.chat_message("user" if isinstance(m, HumanMessage) else "assistant"):

        # ✅ FIX: show images if URLs present
        if isinstance(m, AIMessage) and isinstance(m.content, str) and "http" in m.content:
            urls = m.content.split("\n")
            for url in urls:
                if url.startswith("http"):
                    st.image(url, width=300)
                else:
                    st.write(url)
        else:
            st.write(m.content)

#  AGENT CALL
async def run_agent(messages):
    res = await graph.ainvoke({"messages": messages})
    return res["messages"][-1].content

#  INPUT
if prompt := st.chat_input("Ask your marketing query..."):
    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = asyncio.run(run_agent(st.session_state.messages))

            # ✅ FIX: render images instead of URLs
            if isinstance(response, str) and "http" in response:
                urls = response.split("\n")
                for url in urls:
                    if url.startswith("http"):
                        st.image(url, width=300)
                    else:
                        st.write(url)
            else:
                st.write(response)

    st.session_state.messages.append(AIMessage(content=response))

    #  SAVE TO DB
    supabase.table("messages").insert([
        {
            "conversation_id": st.session_state.conversation_id,
            "role": "user",
            "content": prompt
        },
        {
            "conversation_id": st.session_state.conversation_id,
            "role": "assistant",
            "content": response
        }
    ]).execute()