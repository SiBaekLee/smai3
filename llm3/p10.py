import streamlit as st

from MyLLM import save_uploadedfile

st.sidebar.markdown("Clicked Page 10")

st.title("Page 10")

picture = st.camera_input("Take a picture")