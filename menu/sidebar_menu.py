import streamlit as sl
from streamlit_option_menu import option_menu

def menu():
    with sl.sidebar:
        selection = option_menu(
            menu_title = 'Menu',
            options = ["Home", "About", "Contact"],
            icons = ["bookmark", "backpack4", "aspect-ratio-fill"],
            menu_icon = "alexa",
            default_index = 0,
        )
    return selection