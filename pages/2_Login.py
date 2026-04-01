# import streamlit as st
# from supabase_client import supabase

# st.title("Login / Signup")

# email = st.text_input("Email")
# password = st.text_input("Password", type="password")

# # LOGIN
# if st.button("Login"):
#     try:
#         res = supabase.auth.sign_in_with_password({
#             "email": email,
#             "password": password
#         })

#         if res.user:
#             st.session_state.user = res.user
#             st.success("Login successful")

#             # ✅ FIX THIS LINE BASED ON YOUR FILE NAME
#             st.switch_page("pages/3_Chatbot.py")

#     except Exception as e:
#         st.error("Login failed")

# # SIGNUP
# if st.button("Signup"):
#     try:
#         supabase.auth.sign_up({
#             "email": email,
#             "password": password
#         })
#         st.success("Account created. Please login.")
#     except Exception as e:
#         st.error("Signup failed")

import streamlit as st
from supabase_client import supabase

st.set_page_config(page_title="Login", layout="centered")

st.markdown("## 🔐 Login / Signup")

st.markdown("---")

email = st.text_input("📧 Email")
password = st.text_input("🔑 Password", type="password")

col1, col2 = st.columns(2)

# LOGIN
with col1:
    if st.button("Login", use_container_width=True):
        try:
            res = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            if res.user:
                st.session_state.user = res.user
                st.success("✅ Login successful")

                st.switch_page("pages/3_Chatbot.py")

        except Exception:
            st.error("❌ Invalid credentials")

# SIGNUP
with col2:
    if st.button("Signup", use_container_width=True):
        try:
            supabase.auth.sign_up({
                "email": email,
                "password": password
            })
            st.success("✅ Account created. Please login.")
        except Exception:
            st.error("❌ Signup failed")