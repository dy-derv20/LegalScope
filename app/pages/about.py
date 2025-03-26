import streamlit as sl

def show():
    """
    Render the About page with services and description
    """
    # sub 1: Our Services
    sl.header("Our Services")
    sl.markdown("<hr style='margin-top:5px; margin-bottom:5px;'>", unsafe_allow_html=True)
    sl.markdown("""
    - <span style='font-size:20px;'> AI-Powered Legal Advice </span>
    - <span style='font-size:20px;'> Document Analysis | Drafting </span>
    - <span style='font-size:20px;'> Case Management Solutions </span>
    """, unsafe_allow_html=True)
    
    # sub 2: What we do
    sl.header("What we do")
    sl.markdown("<hr style='margin-top:5px; margin-bottom:5px;'>", unsafe_allow_html=True)
    sl.markdown(
        "<span style='font-size:20px;'>At AI Law Firm, we blend technology and legal expertise to provide innovative solutions that save time and reduce costs for our clients. </span>",
        unsafe_allow_html=True
    )
    
    # Additional details about the firm
    sl.markdown("### Our Mission")
    sl.markdown("""
    - Leverage cutting-edge AI technology
    - Provide accessible legal insights
    - Streamline legal processes
    - Ensure client confidentiality
    """, unsafe_allow_html=True)
