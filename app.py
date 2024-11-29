import streamlit as st
from gtts import gTTS
from io import BytesIO

# Function to generate and play all phrases in Korean and Chinese order
def generate_phrases_audio(phrases):
    try:
        combined_audio = BytesIO()
        for phrase, translations in phrases.items():
            # Add Korean audio
            korean_tts = gTTS(text=translations["ko"], lang="ko")
            korean_tts.write_to_fp(combined_audio)
            
            # Add Chinese audio
            chinese_tts = gTTS(text=translations["zh"], lang="zh-CN")
            chinese_tts.write_to_fp(combined_audio)

        combined_audio.seek(0)
        return combined_audio
    except Exception as e:
        st.error(f"Error generating audio: {e}")
        return None

# Phrases dictionary
phrases = {
    "Can I have a menu?": {"zh": "可以给我菜单吗?", "ko": "메뉴판 주세요."},
    "I would like to order this.": {"zh": "我想点这个。", "ko": "이걸로 주문할게요."},
    "Do you have vegetarian dishes?": {"zh": "有素食菜吗?", "ko": "채식 요리 있어요?"},
    "Can I have water, please?": {"zh": "可以给我水吗?", "ko": "물 좀 주세요."},
    "How much is this?": {"zh": "这个多少钱?", "ko": "이거 얼마예요?"},
    "Can I have the bill?": {"zh": "可以给我账单吗?", "ko": "계산서 주세요."},
    "Is this dish spicy?": {"zh": "这道菜辣吗?", "ko": "이 요리 매워요?"},
    "Can I have more rice?": {"zh": "可以再给我一些米饭吗?", "ko": "밥 좀 더 주세요."},
    "Where is the restroom?": {"zh": "洗手间在哪里?", "ko": "화장실 어디에요?"},
    "Can I have some napkins?": {"zh": "可以给我一些纸巾吗?", "ko": "냅킨 좀 주세요."},
}

# Streamlit app layout
st.title("Restaurant Phrases for Macau Travel")
st.subheader("Learn useful restaurant phrases in Chinese and Korean!")

# Play all phrases in "Korean → Chinese" order
if st.button("Play All Phrases (Korean → Chinese)"):
    combined_audio = generate_phrases_audio(phrases)
    if combined_audio:
        st.audio(combined_audio, format="audio/mp3")
