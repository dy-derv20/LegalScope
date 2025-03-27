import streamlit as sl
import os
from dotenv import load_dotenv
import ast

def show():
    # Load environment variables from .env file
    load_dotenv()

    # Get the users from the USERS environment variable and convert to dictionary
    users = os.getenv("USERS")
    if users:
        users = ast.literal_eval(users)  # Converts string representation of dict to a Python dict
    else:
        sl.error("Error: Could not load users from the .env file.")
        return

    sl.markdown("### Please log in to continue.")
    
    # User input for login form
    username = sl.text_input("Username")
    password = sl.text_input("Password", type="password")

    # Submit login button
    if sl.button("Login"):
        if username in users and users[username] == password:
            sl.session_state["logged_in"] = True
            sl.session_state["user"] = username
            sl.success(f"Welcome {username}!")
            sl.experimental_rerun()  # Reload to reflect login
        else:
            sl.error("Invalid username or password.")
