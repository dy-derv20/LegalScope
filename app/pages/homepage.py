import streamlit as st

def show():
    """
    Render the homepage of the LegalScope
    """
    # Page title with centered styling
    st.markdown("# <p style='text-align:center;'>Welcome to LegalScope</p>", unsafe_allow_html=True)
    
    # Introduction section
    st.markdown("""
    ## About Our Legal AI Assistant
    
    Our advanced AI-powered legal assistant is designed to provide:
    
    - Instant legal guidance
    - Document analysis
    - Case research support
    - Confidential consultations
    
    Get started by navigating to the Chat section in the sidebar.
    """)
    
    # Feature highlights
    st.info("🔒 All conversations are encrypted and confidential")