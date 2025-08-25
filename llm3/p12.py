import streamlit as st
from PIL import Image

from MyLLM import save_uploadedfile, progressBar, makeImages

# Sidebar
st.sidebar.markdown("Clicked Page 12")

# Page
st.title("Page 12")


text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")
name = st.text_input(label="이미지이름:",
                    placeholder="이미지 이름을 입력 하세요")
num = st.number_input(label="개수:",
                    placeholder="개수를 입력 하세요",
                    min_value=1, max_value=5, step=1)
if st.button("SEND"):
    if text and name and num:
        st.info(text)
        my_bar = progressBar("Operation in progress. Please wait.")
        makeImages(text, name, num)
        my_bar.empty()


        for i in range(0, num):
            with open(f"img/{name.split('.')[0]}_{i}.png", "rb") as file:
                st.download_button(
                    label=f"Download: {name.split('.')[0]}_{i}.png",
                    data=file,
                    file_name=f"img/{name.split('.')[0]}_{i}.png",
                    mime="image/png",
                )
            img = Image.open(f"img/{name.split('.')[0]}_{i}.png")
            st.image(img)
    else:
        st.info("다시 입력 하세요")