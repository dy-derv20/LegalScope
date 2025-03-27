import streamlit as st
from app.pages import homepage, about, contact, chatbot
from app.layout import create_menu





def main():
    # Set page configuration
    st.set_page_config(
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
    










if __name__ == "__main__":
    main()