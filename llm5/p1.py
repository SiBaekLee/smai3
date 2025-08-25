import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools

from MyLCH import getOpenAI
from MyLCH import progressBar
from MyLCH import makeAudio

st.markdown("Page1")
st.sidebar.markdown("Clicked Page1")

text = st.text_area(label="질문입력:", placeholder="질문을 입력하세요")
if st.button("SEND"):
    if text:
        st.info(text)
        makeAudio(text,"temp.mp3")
        st.audio("audio/temp.mp3", autoplay=True)

        openllm = getOpenAI()
        tools = load_tools(["wikipedia"], llm=openllm)
        agent = initialize_agent(
            tools,
            openllm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False
        )
        my_bar = progressBar("Loading....")
        result = agent.run(text)
        st.info(result)
        makeAudio(result,"result.mp3")
        st.audio("audio/result.mp3", autoplay=True)
        my_bar.empty()
    else:
        st.info("질문을 입력하세요")

