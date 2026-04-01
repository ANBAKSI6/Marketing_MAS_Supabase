# import streamlit as st

# st.set_page_config(page_title="Marketing AI")
# st.title("Welcome")


import streamlit as st

# Page config
st.set_page_config(
    page_title="AI Marketing Assistant",
    page_icon="🚀",
    layout="wide"
)

# Hide default Streamlit menu/footer (clean UI)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Hero Section
st.markdown("""
# 🚀 AI Marketing Assistant

### Your all-in-one AI-powered marketing team

Generate:
- Marketing Strategies
- SEO Keywords
- Ad Copy
- Logos
- Social Media Content
- Email Campaigns

---
""")

# CTA Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🔐 Login / Signup", use_container_width=True):
        st.switch_page("pages/2_Login.py")

with col2:
    if st.button("💬 Go to Chatbot", use_container_width=True):
        st.switch_page("pages/3_Chatbot.py")

# Footer
st.markdown("---")
st.markdown("Built with using Streamlit + Supabase + AWS Bedrock")