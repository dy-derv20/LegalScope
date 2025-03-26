import streamlit as sl

def show():
    # sub 1
    sl.header("Our Services")
    sl.markdown("<hr style='margin-top:5px; margin-bottom:5px;'>", unsafe_allow_html=True)  # divider
    sl.markdown("""
    - <span style='font-size:20px;'> AI-Powered Legal Advice </span>
    - <span style='font-size:20px;'> Document Analysis | Drafting </span>
    - <span style='font-size:20px;'> Case Management Solutions </span>
    """, unsafe_allow_html=True)

    # sub 2
    sl.header("What we do")
    sl.markdown("<hr style='margin-top:5px; margin-bottom:5px;'>", unsafe_allow_html=True)
    sl.markdown(
        "<span style='font-size:20px;'>At AI Law Firm, we blend technology and legal expertise to provide innovative solutions that save time and reduce costs for our clients. </span>",
        unsafe_allow_html=True)
