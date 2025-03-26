import streamlit as sl

def show():
    """
    Render the Contact page with contact information
    """
    sl.header("Contact Us")
    sl.markdown("<hr style='margin-top:5px; margin-bottom:5px;'>", unsafe_allow_html=True)
    
    # Contact Information
    sl.markdown("""
    ### Reach Out to Us
    
    #### Primary Contact
    - **Email:** dydervishi@gmail.com
    - **Phone:** (954) 774-3067
    
    #### Secondary Contact
    - **Email:** jakeinman05@gmail.com
    - **Phone:** (754) 248-1313
    
    ### Contact Form
    """, unsafe_allow_html=True)
    
    # Simple contact form
    with sl.form(key='contact_form'):
        name = sl.text_input("Your Name")
        email = sl.text_input("Your Email")
        message = sl.text_area("Your Message")
        submit_button = sl.form_submit_button("Send Message")
        
        if submit_button:
            # Placeholder for form submission logic
            sl.success("Message sent successfully! We'll get back to you soon.")