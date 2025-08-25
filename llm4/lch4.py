from langchain.agents import initialize_agent, load_tools, AgentType

from MyLCH import getOpenAI
from MyLCH import getGenAI


if __name__ == '__main__':
    openllm = getOpenAI()
    genllm = getGenAI()

    tools = load_tools(["wikipedia"], llm=openllm)

    agent = initialize_agent(
        tools,
        openllm,
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False
    )

    txt = "귀멸의 칼날 영화 주연이 누구야? 2025년 8월 25일 기준으로 몇개월이 지났어? 한국어로 답해줘."
    print(agent.run(txt))