from langchain.chains.conversation.base import ConversationChain
from MyLCH import getOpenAI
from MyLCH import getGenAI


if __name__ == '__main__':
    openllm = getOpenAI()
    genllm = getGenAI()

    cc = ConversationChain(llm=openllm, verbose=True)

    while True:
        txt = input("입력하세요:")
        if txt == 'q':
            break
        print(cc.predict(input=txt))

    print("Bye.....")