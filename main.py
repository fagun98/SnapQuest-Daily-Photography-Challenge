import streamlit as st

from streamlit_option_menu import option_menu

#pages
import challenge
import gallery
import home 
import rules 

# Set page title
st.set_page_config(page_title="SnapQuest", layout="wide")

# Add custom CSS for styling the font
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Georgia&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }

    </style>
    """, unsafe_allow_html=True)

selected = option_menu(menu_title="",
                       options=["Home", "Challenge", "Gallery", "Rules & Tips"],
                       icons=['house', 'lightning', 'images', 'question-circle'],
                       default_index=0,
                       orientation="horizontal")

if selected == "Home":
    home.run()

elif selected == "Challenge":
    challenge.run()
    
elif selected == "Gallery":
    gallery.run()

elif selected == "Rules & Tips":
    rules.run()
