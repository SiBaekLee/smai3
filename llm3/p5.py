import time

import streamlit as st
from PIL import Image

from MyLLM import save_carpturefile, geminiModel

st.sidebar.markdown("Clicked Page 5")

st.title("Page 5")

picture = st.camera_input("Take a picture")

if picture:
    st.info("이미지를 캡쳐했습니다")
    save_carpturefile("capture", picture, "temp.png", st)
    text = st.text_area(label="질문입력:", placeholder="질문을 입력 하세요")
    if st.button("SEND"):
        img = Image.open("capture/temp.png")
        model = geminiModel()
        # Progress Bar Start -----------------------------------------
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        # Progress Bar End -----------------------------------------
        response = model.generate_content( [ text , img ] )
        my_bar.empty()
        st.info(response.text)
