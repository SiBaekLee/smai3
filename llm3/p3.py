# -------------------------
# Streamlit UI
# -------------------------
import re
import streamlit as st

from MyLLM import geminiTxt
from MyLLM import progressBar

st.title("Page 3 프로그램 작성기")

st.sidebar.markdown("Clicked Page 3")

text = st.text_area(label="질문입력:", placeholder="질문을 입력하세요")
selected_option = st.radio("언어를 선택하세요", ("java", "python", "c++"))

if st.button("SEND"):
    if text and selected_option:
        st.write(f"선택된 옵션: {selected_option}")
        st.info(text)
        my_bar = progressBar("Operation in progress. Please wait.")
        result = geminiTxt(f"{selected_option}로 다음 질문을 코딩해줘 {text}")
        my_bar.empty()
        st.code(result, language=selected_option)
    else:
        st.info("질문과 언어를 선택하세요")