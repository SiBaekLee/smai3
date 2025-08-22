import streamlit as st

from MyLLM import save_uploadedfile, makeAudio, makeMsg, progressBar, openAiModelArg

# Sidebar
st.sidebar.markdown("Clicked Page 8")

# Page
st.title("Page 8")
system = st.text_input("SYSTEM",placeholder="system 을 입력")
text = st.text_input("질문 입력", placeholder="질문을 입력하세요")

if st.button("SEND"):
    if text and system:
        st.info(text)
        # 음성으로 플레이 하고
        makeAudio(text, "temp.mp3")
        st.audio("audio/temp.mp3", autoplay=True, width=1)
        # OpenAI 물어보고 결과를 받는다.
        msg = makeMsg(system, text)
        my_bar = progressBar("Operation in progress. Please wait.")
        result = openAiModelArg("gpt-4o", msg)
        my_bar.empty()
        # 결과를 음성으로 플레이 하고
        # 결과 내용을 화면에 출력 한다.
        st.info(result)
        makeAudio(result, "result.mp3")
        st.audio("audio/result.mp3", autoplay=True, width=1)

    else:
        st.audio("audio/retry.mp3", autoplay=True, width=1)
        st.info("입력 하세요")