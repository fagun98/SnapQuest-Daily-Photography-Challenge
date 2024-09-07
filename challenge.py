import streamlit as st
from utils import get_today_object,time_until_reset, format_time_remaining
from PIL import Image
import os

def run():
    today_object = get_today_object()

    st.title(f"Today's Challenge: **{today_object}**")
    st.subheader("Upload Your Best Shot")
    st.write(f"Capture your best photo of **'{today_object}'** and upload it below:")

    # Add a countdown timer for the next challenge
    time_remaining = time_until_reset()
    st.markdown(f"Time Left Until the Next Challenge Starts:{format_time_remaining(time_remaining)}")

    uploaded_files = st.file_uploader("Upload your photos", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

    if uploaded_files:
        st.write(f"Your uploads for '{today_object}':")
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            st.image(image, caption=uploaded_file.name, use_column_width=True)
            file_path = os.path.join(st.secrets["constants"]["today_object_dir"], uploaded_file.name)
            image.save(file_path)
    
    st.write("Once uploaded, you can view your photo in the **Gallery** tab.")