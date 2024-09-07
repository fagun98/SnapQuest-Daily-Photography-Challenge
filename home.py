import streamlit as st

def run():
    st.title("Welcome to SnapQuest!")
    st.subheader("A Daily Photography Adventure")

    st.write("""
    Embark on a daily journey to enhance your photography skills. Every day, a new object is chosen for you to capture, helping you see the world through a fresh lens.
    """)
        
    st.write("**Get ready to click!** Head over to **Today's Challenge** to see what’s in store for you today.")

    # Add images for visual appeal
    col1, col2 = st.columns(2)
    
    with col1:
        st.image('constants/index_2.jpeg', caption="Capture the Moment", use_column_width=True)
    
    with col2:
        st.image('constants/index_1.jpeg', caption="Daily Challenge", use_column_width=True)
    
    st.write("Happy snapping and good luck on your daily photography adventure!")