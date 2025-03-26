import streamlit as sl
from app.pages import homepage, about, contact, chatbot
from streamlit_option_menu import option_menu

def main():
    # Set page configuration
    sl.set_page_config(
        page_title="LegalScope",
        page_icon="⚖️",
        layout="wide"
    )

    # Create menu and get selected page
    selected_page = create_menu()

    # Render appropriate page based on selection
    if selected_page == "Home":
        homepage.show()
    elif selected_page == "About":
        about.show()
    elif selected_page == "Contact":
        contact.show()
    elif selected_page == "Chatbot":
        chatbot.show()


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
            default_index=0,
        )
    return selection

if __name__ == "__main__":
    main()