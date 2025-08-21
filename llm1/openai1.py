from myllm.myApi import geminiModel, openAiModel, openAiModelArg, makeMsg


def test():
    response = openAiModelArg("gpt-4o",makeMsg("한국 선생님", "천안에 맛집 알려줘"))
    print(response)

if __name__ == "__main__":
    test()