import streamlit as st
from dotenv import load_dotenv
import os 


    
def show():
    
    st.markdown("# <p style='text-align:center;'>Login</p>", unsafe_allow_html=True)
    
    load_dotenv()

    users = os.getenv("users")
    
    

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid username or password. Try Again")

        