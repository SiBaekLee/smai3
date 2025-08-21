import os
import time

import streamlit as st
from PIL import Image

from MyLLM import geminiModel


def save_uploadedfile(directory, file):
    # 1. 디렉토리가 없으면 생성
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2. 파일 저장 (이름 변경 없이 저장)
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    # 3. 저장 완료 메시지 출력
    st.success(f'저장 완료: {directory}에 {file.name} 저장되었습니다.')


# Sidebar
st.sidebar.markdown("Clicked Page 2")

# Page
st.title("Page 2 Image Upload")
file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])
if file:
    st.image(file)
    save_uploadedfile("img", file)

    text = st.text_area(label="질문입력:",
                        placeholder="질문을 입력 하세요")
    if st.button("SEND"):
        img = Image.open("img/"+file.name)
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



