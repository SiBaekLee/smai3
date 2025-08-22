import streamlit as st
from PIL import Image

from MyLLM import save_uploadedfile
from MyLLM import makeImage, progressBar

st.sidebar.markdown("Clicked Page 11")

st.title("Page 11")

text = st.text_area(label="질문입력:", placeholder="질문을 입력하세요")
name = st.text_input(label="이미지이름:", placeholder="이미지 이름을 입력하세요")


if st.button("SEND"):
    if text and name:
        st.info(text)
        mybar = progressBar("Operation in progress. Please wait.")
        makeImage(text,name)
        mybar.empty()

        with open("img/"+name, "rb") as file:
            st.download_button(
                label="파일다운로드",
                data=file,
                file_name="img/"+name,
                mime="image/jpg"
            )
            img = Image.open("img/"+name)
        st.image(img)
    else:
        st.info("다시 입력하세요")