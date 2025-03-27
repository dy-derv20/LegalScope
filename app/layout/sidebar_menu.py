import streamlit as sl
from streamlit_option_menu import option_menu


def create_menu():
    """
    Create a sidebar menu using streamlit_option_menu
    
    Returns:
    str: Selected page name
    """
    with sl.sidebar:
        selection = option_menu(
            menu_title='Menu',
            options=["Home", "About", "Contact", "Chatbot"],
            icons=["house", "backpack", "envelope", "chat-text"],
            menu_icon="alexa",
            default_index = 0,
        )
    
    return selection