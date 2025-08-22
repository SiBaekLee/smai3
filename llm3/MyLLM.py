import time

import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
#GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]


def geminiModel():
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")
    return model

def geminiTxt(txt):
    model = geminiModel()
    response = model.generate_content(txt)
    return response.text

def save_carpturefile(directory, picture, name, st):
    if picture is not None:
        if not os.path.exists(directory):
            os.makedirs(directory)
        # 2. 파일 저장 (이름 변경 없이 저장)
        with open(os.path.join(directory, name), 'wb') as file:
            file.write(picture.getvalue())
        # 3. 저장 완료 메시지 출력
        st.success(f'저장 완료: {directory}에 {name} 저장되었습니다.')

def save_uploadedfile(directory, file, st):
    # 1. 디렉토리가 없으면 생성
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2. 파일 저장 (이름 변경 없이 저장)
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    # 3. 저장 완료 메시지 출력
    st.success(f'저장 완료: {directory}에 {file.name} 저장되었습니다.')


def progressBar(txt):
    # Progress Bar Start -----------------------------------------
    progress_text = txt
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.08)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    return my_bar
    # Progress Bar End -----------------------------------------