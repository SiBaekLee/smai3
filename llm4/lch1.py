from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate

from MyLCH import getOpenAI
from MyLCH import getGenAI


def test(txt):
    txt = "카메라"
    template = "{product}를 홍보하기 위한 문구 만들어줘"
    prompt = PromptTemplate(
        input_variables=["product"],
        template=template
    )
    print(prompt.format(product=txt))

    openllm = getOpenAI()
    genllm = getGenAI()

    openchain = LLMChain(llm=openllm, prompt=prompt)
    genchain = LLMChain(llm=genllm, prompt=prompt)

    print(openchain.run("카메라"))
    print(genchain.run("카메라"))


if __name__ == '__main__':
    test("카메라")