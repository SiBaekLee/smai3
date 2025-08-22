import streamlit as st

from MyLLM import save_uploadedfile, save_carpturefile, encode_image, openAiModel, progressBar

st.sidebar.markdown("Clicked Page 10")

st.title("Page 10")

picture = st.camera_input("Take a picture")
if picture:
    st.info("이미지를 캡쳐했습니다")
    save_carpturefile("capture", picture, "capturetemp.png", st)
    text = st.text_area(label="질문입력:", placeholder="질문을 입력 하세요")

# OpenAI에게 물어 본다.
    if st.button("SEND"):
        base64img = encode_image("capture/capturetemp.png")
        model = openAiModel()
        my_bar = progressBar("Operation in progress. Please wait.")
        response = model.chat.completions.create(
            model='gpt-4o',
            messages=[
                {"role": "system", "content": "당신은 한국인이고, 친절하고 꼼꼼한 서포터 입니다. 질문에 정성을 다해 답변합니다."},
                {"role": "user", "content": [
                    {"type": "text", "text": text},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/jpg;base64,{base64img}"}
                     }
                ]}
            ],
            temperature=0.0,
        )
        my_bar.empty()

# 결과를 출력하고
# 음성으로 안내한다
        st.info(response.choices[0].message.content)