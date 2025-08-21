from io import BytesIO

import requests
from PIL import Image

from myllm.myApi import geminiModel

def test(prompt, img):
    model = geminiModel()
    response = model.generate_content([prompt, img])
    print(response.text)

if __name__ == "__main__":
    image_url = "https://tse2.mm.bing.net/th/id/OIP.1zPPT47r7aKk9UZHl77Y3AHaHa?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"  # 실제 이미지 URL로 교체
    response_image = requests.get(image_url)
    img = Image.open(BytesIO(response_image.content))
    prompt = "이 이미지에 있는 음료의 영양성분과 칼로리 당함유 양을 알려줘"
    test(prompt, img)