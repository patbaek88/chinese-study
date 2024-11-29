import streamlit as st
import pyttsx3

# Text-to-speech initialization
def init_tts(language):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if language == 'zh':  # Chinese voice
        for voice in voices:
            if 'zh' in voice.id:
                engine.setProperty('voice', voice.id)
                break
    elif language == 'ko':  # Korean voice
        for voice in voices:
            if 'ko' in voice.id:
                engine.setProperty('voice', voice.id)
                break
    engine.setProperty('rate', 150)  # Adjust speed
    return engine

# Speak text
def speak_text(text, language):
    engine = init_tts(language)
    engine.say(text)
    engine.runAndWait()

# Dictionary for phrases
phrases = {
    "Can I have a menu?": {"zh": "可以给我菜单吗?", "ko": "메뉴판 주세요."},
    "I would like to order this.": {"zh": "我想点这个。", "ko": "이걸로 주문할게요."},
    "Do you have vegetarian dishes?": {"zh": "有素食菜吗?", "ko": "채식 요리 있어요?"},
    "Can I have water, please?": {"zh": "可以给我水吗?", "ko": "물 좀 주세요."},
    "How much is this?": {"zh": "这个多少钱?", "ko": "이거 얼마예요?"},
}

# Streamlit app
st.title("Useful Restaurant Phrases for Macau Travel")

# Select a phrase
st.subheader("Select a phrase to learn:")
selected_phrase = st.selectbox("Choose a phrase:", list(phrases.keys()))

# Display translations
st.write("### Chinese: ", phrases[selected_phrase]['zh'])
st.write("### Korean: ", phrases[selected_phrase]['ko'])

# Buttons for TTS
if st.button("Read in Chinese"):
    speak_text(phrases[selected_phrase]['zh'], 'zh')

if st.button("Read in Korean"):
    speak_text(phrases[selected_phrase]['ko'], 'ko')in 
