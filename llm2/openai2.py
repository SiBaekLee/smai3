from myllm.myApi import geminiModel, openAiModel, openAiModelArg, makeMsg


def test():
    modelName = "gpt-4o"
    msg = makeMsg("한문장으로 요약", prompt)
    result = openAiModelArg(modelName, msg)
    print(result)

if __name__ == "__main__":
    prompt = "SK하이닉스에 대해서 알려줘"
    test()