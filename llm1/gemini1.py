from myllm.myApi import geminiModel

def test(txt):
    model = geminiModel()
    response = model.generate_content(txt)
    return response.text

if __name__ == "__main__":
    while True:
        txt = input("질문을 입력하세요(q)")
        if txt == "q":
            break
        result = test(txt)
        print(result)