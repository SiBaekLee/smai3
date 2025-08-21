from myllm.myApi import geminiModel, openAiModel, openAiModelArg, makeMsg


def test(prompt):
    openModel = openAiModel()
    response = openModel.images.create_variation(
        model="dall-e-2",
        image=open(prompt, "rb"),
        n=3,
        size="1024x1024"
    )
    for n, data in enumerate(response.data):
        print(n)
        print(data.url)

if __name__ == "__main__":
    prompt = "img/amd.jpg"
    test(prompt)