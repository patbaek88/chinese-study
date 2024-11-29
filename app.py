import streamlit as st
from gtts import gTTS
from io import BytesIO
import os

# Function to generate a single TTS audio file for all phrases
def generate_combined_audio(phrases, lang):
    try:
        combined_audio = BytesIO()
        for phrase in phrases.values():
            text = phrase[lang]
            tts = gTTS(text=text, lang=lang)
            tts.write_to_fp(combined_audio)
        combined_audio.seek(0)
        return combined_audio
    except Exception as e:
        st.error(f"Error generating combined audio: {e}")
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

# Select a phrase
selected_phrase = st.selectbox("Choose a phrase:", list(phrases.keys()))

# Display the selected phrase in Chinese and Korean
st.write("### Chinese: ", phrases[selected_phrase]['zh'])
st.write("### Korean: ", phrases[selected_phrase]['ko'])

# Buttons to play individual audio
if st.button("Play in Chinese"):
    audio = gTTS(text=phrases[selected_phrase]['zh'], lang="zh-CN")
    audio_file = BytesIO()
    audio.write_to_fp(audio_file)
    audio_file.seek(0)
    st.audio(audio_file, format="audio/mp3")

if st.button("Play in Korean"):
    audio = gTTS(text=phrases[selected_phrase]['ko'], lang="ko")
    audio_file = BytesIO()
    audio.write_to_fp(audio_file)
    audio_file.seek(0)
    st.audio(audio_file, format="audio/mp3")

# Generate and play all phrases in one file
st.subheader("Play All Phrases")
lang = st.radio("Select Language for Combined Audio:", options=["zh", "ko"], format_func=lambda x: "Chinese" if x == "zh" else "Korean")

if st.button("Play All"):
    combined_audio = generate_combined_audio(phrases, lang)
    if combined_audio:
        st.audio(combined_audio, format="audio/mp3")
