# import streamlit as st

# st.title("🚀 AI Marketing Assistant")

# st.write("All-in-one marketing tool")

# if st.button("Login"):
#     st.switch_page("pages/2_Login.py")

import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

st.markdown("# 🚀 AI Marketing Assistant")

st.markdown("### Your AI-powered marketing team")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### ✨ Features
- Marketing Strategy
- SEO Keywords
- Ad Copy
- Logo Generation
- Social Media Content
- Email Campaigns
""")

with col2:
    st.markdown("""
### 💡 Why Use This?
- No need for expensive agencies
- Instant results
- AI-powered insights
""")

st.markdown("---")

if st.button("🔐 Login / Signup", use_container_width=True):
    st.switch_page("pages/2_Login.py")