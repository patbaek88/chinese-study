import streamlit as st
from gtts import gTTS
import os

# Function to generate and save audio for all phrases in Korean and Chinese order
def save_phrases_audio(phrases, output_file="combined_audio.mp3"):
    try:
        with open(output_file, "wb") as f:
            for phrase, translations in phrases.items():
                # Add Korean audio
                korean_tts = gTTS(text=translations["ko"], lang="ko")
                korean_tts.write_to_fp(f)
                
                # Add Chinese audio
                chinese_tts = gTTS(text=translations["zh"], lang="zh-CN")
                chinese_tts.write_to_fp(f)
        return output_file
    except Exception as e:
        st.error(f"Error generating audio: {e}")
        return None

# Phrases dictionary
phrases = {
    "Can I have a menu?": {"zh": "可以给我菜单吗?", "ko": "메뉴판 주세요."},
    "I would like to order this.": {"zh": "我想点这个。", "ko": "이걸로 주문할게요."},
    # Add more phrases here...
}

# Streamlit app layout
st.title("Restaurant Phrases for Macau Travel")
st.subheader("Learn useful restaurant phrases in Chinese and Korean!")

# Play all phrases in "Korean → Chinese" order
if st.button("Generate and Download Audio"):
    output_file = save_phrases_audio(phrases)
    if output_file and os.path.exists(output_file):
        with open(output_file, "rb") as f:
            st.download_button(
                label="Download Combined Audio",
                data=f,
                file_name="combined_audio.mp3",
                mime="audio/mp3",
            )
