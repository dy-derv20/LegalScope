from LegalScope.menu.sidebar_menu import menu
from LegalScope.pages import homepage, about, contact

selected_page = menu()

if selected_page == "Home":
    homepage.show()
elif selected_page == "Contact":
    contact.show()
elif selected_page == "About":
    about.show()
