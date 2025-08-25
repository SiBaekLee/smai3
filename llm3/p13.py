import streamlit as st
from PIL import Image

from MyLLM import save_uploadedfile, cloneImage, progressBar

# Sidebar
st.sidebar.markdown("Clicked Page 13")

# Page
st.title("Page 13")

file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])

if file:
    st.image(file)
    save_uploadedfile("img", file, st )
    num = st.number_input(label="개수:",
                          placeholder="개수를 입력 하세요",
                          min_value=1, max_value=5, step=1)
    if st.button("SEND"):
        my_bar = progressBar("Operation in progress. Please wait.")
        cloneImage(file.name, num)
        my_bar.empty()
        for i in range(0, num):
            img = Image.open(f"img/{file.name.split('.')[0]}_clone_{i}.png")
            st.image(img)
else:
    st.info("입력 하세요")