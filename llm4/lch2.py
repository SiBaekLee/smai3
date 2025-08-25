from langchain.chains.llm import LLMChain
from langchain.model_laboratory import ModelLaboratory
from langchain_core.prompts import PromptTemplate

from MyLCH import getOpenAI
from MyLCH import getGenAI


if __name__ == '__main__':
    openllm = getOpenAI()
    genllm = getGenAI()

    model_lab = ModelLaboratory.from_llms([openllm, genllm])
    model_lab.compare("천안에 맛집 알려줘?")