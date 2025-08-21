import base64

from myllm.myApi import geminiModel, openAiModel, openAiModelArg, makeMsg

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def test(imgName, prompt):
    img = encode_image(imgName)
    model = openAiModel()
    response = model.chat.completions.create(
        model='gpt-4o',
        messages=[
            {"role": "system", "content": "당신은 한국인이고, 친절하고 꼼꼼한 서포터 입니다. 질문에 정성을 다해 답변합니다."},
            {"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/jpg;base64,{img}"}
                 }
            ]}
        ],
        temperature=0.0,
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    imgName = "img/amd.jpg"
    prompt = "이미지에 있는 반도체의 역할이 무엇인지 알려줘"
    test(imgName, prompt)