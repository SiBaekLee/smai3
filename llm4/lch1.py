from langchain_core.prompts import PromptTemplate


def test(txt):
    template = "{product}를 홍보하기 위한 문구 만들어줘"
    prompt = PromptTemplate(
        input_variables=["product"],
        template=template
    )
    print(prompt.format(product=txt))

if __name__ == '__main__':
    test("카메라")