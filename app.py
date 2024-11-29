import streamlit as st
from gtts import gTTS
import os

# Function to generate and play TTS audio
def play_tts(text, lang):
    try:
        # Generate audio
        tts = gTTS(text=text, lang=lang)
        audio_file = f"output_{lang}.mp3"
        tts.save(audio_file)
        # Play audio
        st.audio(audio_file, format="audio/mp3")
    except Exception as e:
        st.error(f"Error generating audio: {e}")

# Phrases dictionary
phrases = {
    "Can I have a menu?": {"zh": "可以给我菜单吗?", "ko": "메뉴판 주세요."},
    "I would like to order this.": {"zh": "我想点这个。", "ko": "이걸로 주문할게요."},
    "Do you have vegetarian dishes?": {"zh": "有素食菜吗?", "ko": "채식 요리 있어요?"},
    "Can I have water, please?": {"zh": "可以给我水吗?", "ko": "물 좀 주세요."},
    "How much is this?": {"zh": "这个多少钱?", "ko": "이거 얼마예요?"},
    "Can I have the bill?": {"zh": "可以给我账单吗?", "ko": "계산서 주세요."},
    "Is service included?": {"zh": "服务费包含了吗?", "ko": "서비스 포함인가요?"},
    "Do you accept credit cards?": {"zh": "你们接受信用卡吗?", "ko": "신용카드 받나요?"},
    "What is the specialty of the house?": {"zh": "这家餐厅的特色菜是什么?", "ko": "이 집의 추천 요리는 뭔가요?"},
    "Can I have a seat by the window?": {"zh": "可以坐窗边吗?", "ko": "창가 자리로 앉아도 되나요?"},
    "Can you recommend something?": {"zh": "你能推荐点什么吗?", "ko": "추천 메뉴 있나요?"},
    "Is this dish spicy?": {"zh": "这道菜辣吗?", "ko": "이 요리 매워요?"},
    "I am allergic to peanuts.": {"zh": "我对花生过敏。", "ko": "저는 땅콩 알레르기가 있어요."},
    "Can you make it less spicy?": {"zh": "可以做得不辣一点吗?", "ko": "덜 맵게 해주세요."},
    "Can I have more rice?": {"zh": "可以再给我一些米饭吗?", "ko": "밥 좀 더 주세요."},
    "Where is the restroom?": {"zh": "洗手间在哪里?", "ko": "화장실 어디에요?"},
    "Can I have some chopsticks?": {"zh": "可以给我筷子吗?", "ko": "젓가락 좀 주세요."},
    "Can I have a fork and knife?": {"zh": "可以给我叉子和刀吗?", "ko": "포크랑 나이프 주세요."},
    "What is this dish called?": {"zh": "这道菜叫什么名字?", "ko": "이 요리 이름이 뭐예요?"},
    "Can I have some napkins?": {"zh": "可以给我一些纸巾吗?", "ko": "냅킨 좀 주세요."},
    "Can I have a glass of wine?": {"zh": "可以给我一杯红酒吗?", "ko": "와인 한 잔 주세요."},
    "Is there Wi-Fi here?": {"zh": "这里有Wi-Fi吗?", "ko": "여기 와이파이 있나요?"},
    "Can I have some hot tea?": {"zh": "可以给我一杯热茶吗?", "ko": "뜨거운 차 한 잔 주세요."},
    "Do you have a kids' menu?": {"zh": "有儿童菜单吗?", "ko": "어린이 메뉴 있나요?"},
    "Is this gluten-free?": {"zh": "这是无麸质的吗?", "ko": "글루텐 프리인가요?"},
    "Can I have extra sauce?": {"zh": "可以多给点酱汁吗?", "ko": "소스 더 주실 수 있나요?"},
    "Can I change my order?": {"zh": "我可以更改订单吗?", "ko": "주문 변경할 수 있나요?"},
    "Do you have any desserts?": {"zh": "你们有甜点吗?", "ko": "디저트 있나요?"},
    "What drinks do you have?": {"zh": "你们有什么饮料?", "ko": "음료는 뭐 있나요?"},
    "Can I have a cold drink?": {"zh": "可以给我一杯冷饮吗?", "ko": "찬 음료 주세요."},
    "I am in a hurry.": {"zh": "我赶时间。", "ko": "저 좀 급해요."},
    "How long will it take?": {"zh": "需要多长时间?", "ko": "얼마나 걸리나요?"},
    "Can I have a takeaway?": {"zh": "可以打包吗?", "ko": "포장할 수 있나요?"},
    "Do you have any recommendations?": {"zh": "你有什么推荐的吗?", "ko": "추천 좀 해주세요."},
    "This is delicious!": {"zh": "这个很好吃!", "ko": "이거 정말 맛있어요!"},
    "I am full.": {"zh": "我吃饱了。", "ko": "배불러요."},
    "Do you have ice cream?": {"zh": "你们有冰淇淋吗?", "ko": "아이스크림 있나요?"},
    "Is there a local specialty?": {"zh": "这里有什么当地特色菜?", "ko": "지역 특산 요리 있나요?"},
    "Do you serve alcohol?": {"zh": "你们提供酒精饮料吗?", "ko": "주류 제공하나요?"},
    "Can I have some lemon water?": {"zh": "可以给我一些柠檬水吗?", "ko": "레몬 물 좀 주세요."},
    "Can I have a straw?": {"zh": "可以给我吸管吗?", "ko": "빨대 주세요."},
    "Can I have this to go?": {"zh": "可以打包这个吗?", "ko": "이거 포장해주세요."},
    "Can I pay by cash?": {"zh": "可以用现金支付吗?", "ko": "현금으로 계산 가능한가요?"},
    "What are the ingredients?": {"zh": "这道菜有什么成分?", "ko": "이 요리 재료가 뭐예요?"},
    "Do you have spicy sauce?": {"zh": "你们有辣酱吗?", "ko": "매운 소스 있나요?"},
}

# Streamlit app layout
st.title("Restaurant Phrases for Macau Travel")
st.subheader("Learn useful restaurant phrases in Chinese and Korean!")

# Select a phrase
selected_phrase = st.selectbox("Choose a phrase:", list(phrases.keys()))

# Display the selected phrase in Chinese and Korean
st.write("### Chinese: ", phrases[selected_phrase]['zh'])
st.write("### Korean: ", phrases[selected_phrase]['ko'])

# Buttons to play audio
if st.button("Play in Chinese"):
    play_tts(phrases[selected_phrase]['zh'], "zh")

if st.button("Play in Korean"):
    play_tts(phrases[selected_phrase]['ko'], "ko")
