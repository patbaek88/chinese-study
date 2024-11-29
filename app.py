import streamlit as st
from gtts import gTTS
from io import BytesIO
import os 
import pandas as pd
from pypinyin import lazy_pinyin, Style

# Function to generate Pinyin for Chinese text
def get_pinyin(chinese_text):
    return " ".join(lazy_pinyin(chinese_text, style=Style.TONE))


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
st.title("Restaurant Phrases for China Travel")
st.subheader("Phrases")


# Create a DataFrame to display phrases with Pinyin
df = pd.DataFrame([
    {
        "English": phrase,
        "Korean": translations["ko"],
        "Chinese": translations["zh"],
        "Pinyin": get_pinyin(translations["zh"]),
    }
    for phrase, translations in phrases.items()
])


# Display the phrases in a table
st.write("Here are the phrases:")
st.dataframe(df)

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

st.wirte("")
st.subheader("Words")

# Function to get Pinyin with tone marks
def get_pinyin(chinese_text):
    return " ".join(lazy_pinyin(chinese_text, style=Style.TONE))

# List of words commonly used in Chinese restaurants (Korean translation)
words = [
    ("메뉴", "菜单", "cài dān"),
    ("물", "水", "shuǐ"),
    ("밥", "米饭", "mǐ fàn"),
    ("수프", "汤", "tāng"),
    ("면", "面条", "miàn tiáo"),
    ("채식주의자", "素食", "sù shí"),
    ("매운", "辣", "là"),
    ("달콤한", "甜", "tián"),
    ("신", "酸", "suān"),
    ("짠", "咸", "xián"),
    ("쓴", "苦", "kǔ"),
    ("볶은", "炒", "chǎo"),
    ("찐", "蒸", "zhēng"),
    ("끓인", "煮", "zhǔ"),
    ("두부", "豆腐", "dòu fu"),
    ("소고기", "牛肉", "niú ròu"),
    ("돼지고기", "猪肉", "zhū ròu"),
    ("닭고기", "鸡肉", "jī ròu"),
    ("생선", "鱼", "yú"),
    ("새우", "虾", "xiā"),
    ("계란", "鸡蛋", "jī dàn"),
    ("소금", "盐", "yán"),
    ("후추", "胡椒", "hú jiāo"),
    ("생강", "姜", "jiāng"),
    ("마늘", "大蒜", "dà suàn"),
    ("양파", "洋葱", "yáng cōng"),
    ("오이", "黄瓜", "huáng guā"),
    ("토마토", "番茄", "fān qié"),
    ("당근", "胡萝卜", "hú luó bo"),
    ("청양고추", "青椒", "qīng jiāo"),
    ("죽", "粥", "zhōu"),
    ("빵", "包子", "bāo zi"),
    ("만두", "饺子", "jiǎo zi"),
    ("춘권", "春卷", "chūn juǎn"),
    ("훠궈", "火锅", "huǒ guō"),
    ("탕수육", "甜酸", "tián suān"),
    ("젓가락", "筷子", "kuài zi"),
    ("접시", "盘子", "pán zi"),
    ("그릇", "碗", "wǎn"),
    ("컵", "杯子", "bēi zi"),
    ("냅킨", "纸巾", "zhǐ jīn"),
    ("숟가락", "勺子", "sháo zi"),
    ("포크", "叉子", "chā zi"),
    ("계산서", "账单", "zhàng dān"),
    ("제발", "请", "qǐng"),
    ("감사합니다", "谢谢", "xiè xiè"),
    ("미안합니다", "对不起", "duì bù qǐ"),
    ("실례합니다", "对不起", "duì bù qǐ"),
    ("네", "是", "shì"),
    ("아니요", "不是", "bù shì"),
    ("이해하지 못해요", "我不懂", "wǒ bù dǒng"),
    ("얼마에요?", "多少钱?", "duō shǎo qián?"),
    ("계산서 주세요", "请给我账单", "qǐng gěi wǒ zhàng dān"),
    ("배불러요", "我饱了", "wǒ bǎo le"),
    ("매운가요?", "辣吗?", "là ma?"),
    ("더", "更多", "gèng duō"),
    ("덜", "更少", "gèng shǎo"),
    ("포장", "外卖", "wài mài"),
    ("식사", "堂食", "táng shí"),
    ("두 명", "两人桌", "liǎng rén zhuō"),
    ("채식 메뉴", "素菜", "sù cài"),
    ("주요 요리", "主菜", "zhǔ cài"),
    ("반찬", "配菜", "pèi cài"),
    ("디저트", "甜点", "tián diǎn"),
    ("전채", "开胃菜", "kāi wèi cài"),
    ("볶음밥", "炒饭", "chǎo fàn"),
    ("찐 생선", "蒸鱼", "zhēng yú"),
    ("닭날개", "鸡翅膀", "jī chì bǎng"),
    ("바삭한", "脆", "cuì"),
    ("맛있다", "好吃", "hǎo chī"),
    ("쓴 맛", "苦", "kǔ"),
    ("찐 요리", "炖", "dùn"),
    ("양념", "红烧", "hóng shāo"),
    ("구운", "烤", "kǎo"),
    ("굽다", "烤", "kǎo"),
    ("뜨거운", "热", "rè"),
    ("차가운", "冷", "lěng"),
    ("깨끗한", "干净", "gān jìng"),
    ("더러운", "脏", "zāng"),
    ("종업원", "服务员", "fú wù yuán"),
    ("레스토랑", "餐厅", "cān tīng"),
    ("주방", "厨房", "chú fáng"),
    ("주문하다", "点菜", "diǎn cài"),
    ("좋다", "好", "hǎo"),
    ("나쁘다", "不好", "bù hǎo"),
]

# Create a DataFrame with Korean, Chinese, and Pinyin
df = pd.DataFrame([
    {"Korean": word[0], "Chinese": word[1], "Pinyin": get_pinyin(word[1])}
    for word in words
])

# Display the DataFrame
st.write(df)
