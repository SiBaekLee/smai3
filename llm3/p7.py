import streamlit as st

from MyLLM import save_uploadedfile, makeMsg, openAiModelArg, progressBar

st.sidebar.markdown("Clicked Page 7")

st.title("Page 7")

system = st.text_input("SYSTEM",placeholder="system을 입력")
text = st.text_input("질문을 입력",placeholder="질문을 입력")

if st.button("SEND"):
    if system and text:
        st.info(f"{system} 에게 {text} 문의합니다.")
        msg = makeMsg(system,text)

        my_bar = progressBar("Operation in progress. Please wait.")
        result = openAiModelArg("gpt-4o",msg)
        my_bar.empty()

        st.info(result)
    else:
        st.info("입력하세요")
