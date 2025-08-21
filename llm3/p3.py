# -------------------------
# Streamlit UI
# -------------------------
import re
import streamlit as st

from myllm.myApi import geminiModel

st.set_page_config(page_title="Gemini 코드 생성기", page_icon="🤖")
st.title("🤖 Google Gemini 코드 생성기")

# 질문 입력
user_prompt = st.text_area(
    "질문을 입력하세요",
    height=150,
    placeholder="예: Hello World를 출력하는 프로그램을 만들어줘"
)

# 언어 선택 (라디오 버튼)
language = st.radio(
    "언어를 선택하세요",
    options=["java", "python", "c++"],
    index=1,
    horizontal=True
)

# SEND 버튼
send = st.button("🚀 SEND")

# -------------------------
# 실행 로직 (Gemini)
# -------------------------
if send:
    if not user_prompt.strip():
        st.warning("⚠️ 질문을 입력해 주세요.")
        st.stop()

    with st.spinner("Gemini가 코드를 생성 중입니다..."):
        try:
            # geminiModel()은 이미 정의되어 있다고 가정
            model = geminiModel()
            full_prompt = f"'{language}' 언어로 {user_prompt} 프로그램 코드를 작성해줘."
            response = model.generate_content(full_prompt)
            result_text = response.text
        except Exception as e:
            st.error(f"Gemini API 호출 실패: {e}")
            st.stop()

    # 코드 블록 추출 (```lang ... ```)
    code_blocks = re.findall(r"```(\w+)?\n(.*?)```", result_text, re.DOTALL)

    st.subheader("📦 Gemini 응답 코드")
    if code_blocks:
        for lang, code in code_blocks:
            st.code(code.strip(), language=lang if lang else language)
    else:
        # 코드 블록이 없으면 전체를 코드로 출력
        st.code(result_text.strip(), language=language)
