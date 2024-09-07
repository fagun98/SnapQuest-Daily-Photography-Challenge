import streamlit as st
from PIL import Image
import os
from utils import get_today_object

TODAY_OBJECT_DIR = st.secrets["constants"]["today_object_dir"]

def run():
    st.title("Today's Gallery")
    st.subheader("Explore Photos Captured by Others")
    st.write(f"Photos submitted for today's challenge: **'{get_today_object()}'**")

    if not os.path.exists(TODAY_OBJECT_DIR):
        os.makedirs(TODAY_OBJECT_DIR)

    # Display today's photos in a Pinterest-style gallery
    image_files = [f for f in os.listdir(TODAY_OBJECT_DIR) if os.path.isfile(os.path.join(TODAY_OBJECT_DIR, f))]
    if image_files:
        cols = st.columns(4)
        for idx, image_file in enumerate(image_files):
            image_path = os.path.join(TODAY_OBJECT_DIR, image_file)
            with cols[idx % 4]:
                try:
                    st.image(Image.open(image_path), use_column_width=True)
                except Exception as e:
                    print(f"Debug-Log:{image_path}. \nThere was an error: {e}")
    else:
        st.write("No photos uploaded yet. Be the first to upload!")