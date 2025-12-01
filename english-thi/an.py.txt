import streamlit as st
import json
import random
from datetime import datetime
import pandas as pd

# Thiết lập trang
st.set_page_config(
    page_title="Bài Thi Tiếng Anh Bậc 2 - Sở Y Tế Gia Lai",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .mode-header {
        font-size: 2rem;
        color: #2e86ab;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #2e86ab;
        text-align: center;
    }
    .part-header {
        font-size: 1.8rem;
        color: #2e86ab;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #2e86ab;
    }
    .question-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2e86ab;
        margin-bottom: 1.5rem;
    }
    .correct-answer {
        background-color: #d4edda !important;
        border-left: 5px solid #28a745 !important;
    }
    .wrong-answer {
        background-color: #f8d7da !important;
        border-left: 5px solid #dc3545 !important;
    }
    .score-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
    }
    .timer {
        font-size: 1.5rem;
        font-weight: bold;
        color: #dc3545;
        text-align: center;
        padding: 10px;
        background: #fff3cd;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .test-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 2px solid #2e86ab;
    }
    .mock-test-card {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 2px solid #ff6b6b;
    }
    .stButton>button {
        width: 100%;
    }
    .stProgress > div > div > div > div {
        background-color: #28a745;
    }
    .mode-selector {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
    }
    .mode-button {
        margin: 0 1rem;
        padding: 1rem 2rem;
        border-radius: 10px;
        border: 2px solid #2e86ab;
        background: white;
        cursor: pointer;
        transition: all 0.3s;
    }
    .mode-button:hover {
        background: #2e86ab;
        color: white;
        transform: scale(1.05);
    }
    .mode-button.active {
        background: #2e86ab;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

class EnglishTestOnline:
    def __init__(self):
        self.load_all_questions()
        self.initialize_session_state()
    
    def initialize_session_state(self):
        """Khởi tạo trạng thái cho ứng dụng"""
        # Trạng thái chung
        if 'current_mode' not in st.session_state:
            st.session_state.current_mode = "practice"  # "practice" hoặc "mock_test"
        if 'answers' not in st.session_state:
            st.session_state.answers = {}
        if 'score' not in st.session_state:
            st.session_state.score = 0
        if 'show_explanation' not in st.session_state:
            st.session_state.show_explanation = True
        
        # Trạng thái cho chế độ ôn tập
        if 'practice_completed' not in st.session_state:
            st.session_state.practice_completed = False
        if 'practice_start_time' not in st.session_state:
            st.session_state.practice_start_time = None
        
        # Trạng thái cho chế độ thi thử
        if 'mock_test_selected' not in st.session_state:
            st.session_state.mock_test_selected = None
        if 'mock_test_completed' not in st.session_state:
            st.session_state.mock_test_completed = False
        if 'mock_test_start_time' not in st.session_state:
            st.session_state.mock_test_start_time = None
        if 'mock_test_duration' not in st.session_state:
            st.session_state.mock_test_duration = 45 * 60  # 45 phút
        if 'mock_test_time_up' not in st.session_state:
            st.session_state.mock_test_time_up = False
        if 'current_mock_questions' not in st.session_state:
            st.session_state.current_mock_questions = []
        if 'mock_test_answers' not in st.session_state:
            st.session_state.mock_test_answers = {}
        
        # Tạo 4 đề thi thử khi khởi tạo
        if 'mock_tests' not in st.session_state:
            self.create_mock_tests()
    
    def load_all_questions(self):
        """Tải toàn bộ 120 câu hỏi"""
        
        # ===================== PART 1: 20 CÂU =====================
        self.part1_questions = [
            {
                "id": 1,
                "question": "'You should turn off the lights before going out', Mrs. Hoa said.",
                "translation": "'Con nên tắt đèn trước khi ra ngoài', bà Hoa nói.",
                "options": [
                    "A. Mrs. Hoa told to turn off the lights before going out.",
                    "B. Mrs. Hoa suggested to turn off the lights before going out.",
                    "C. Mrs. Hoa suggested turning off the lights before going out.",
                    "D. Mrs. Hoa asked to us that we should turn off the lights before going out."
                ],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'suggest + V-ing' là cấu trúc đúng. Các đáp án khác sai: A thiếu tân ngữ, B sai cấu trúc, D thừa 'to us'."
            },
            {
                "id": 2,
                "question": "You won't have a seat unless you book in advance.",
                "translation": "Bạn sẽ không có chỗ ngồi trừ khi bạn đặt trước.",
                "options": [
                    "A. You won't have a seat if you don't book in advance.",
                    "B. You will have a seat if you don't book in advance.",
                    "C. You didn't have a seat because you didn't book in advance.",
                    "D. You can't have a seat although you book in advance."
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'unless' = 'if not' (trừ khi = nếu không). Các đáp án khác sai nghĩa."
            },
            {
                "id": 3,
                "question": "This is the first time I've made such a stupid mistake.",
                "translation": "Đây là lần đầu tiên tôi mắc một sai lầm ngớ ngẩn như vậy.",
                "options": [
                    "A. I had never made a stupid mistake.",
                    "B. I first made a stupid mistake.",
                    "C. Never before have I made such a stupid mistake.",
                    "D. The first mistake I made was a stupid one."
                ],
                "answer": "C",
                "explanation": "Đáp án C đúng vì đảo ngữ 'Never before have I...' diễn đạt ý 'chưa bao giờ trước đây' tương đương với 'this is the first time'."
            },
            {
                "id": 4,
                "question": "He said: 'I bought these books last week'.",
                "translation": "Anh ấy nói: 'Tôi đã mua những cuốn sách này tuần trước'.",
                "options": [
                    "A. He said he had bought those books the week before.",
                    "B. He said he bought these books last week.",
                    "C. He said he had bought these books last week.",
                    "D. He said he bought these books the week before."
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì trong câu tường thuật: 'these' → 'those', 'last week' → 'the week before', thì quá khứ → quá khứ hoàn thành."
            },
            {
                "id": 5,
                "question": "Mark can't wait to use his new computer-games console.",
                "translation": "Mark không thể đợi để sử dụng máy chơi game máy tính mới của anh ấy.",
                "options": [
                    "A. Mark is looking forward to using his new computer-games console.",
                    "B. Mark is not used to waiting for his new computer-games console.",
                    "C. Mark is patiently waiting to use his new computer-games console.",
                    "D. Mark is eagerly waiting to use his new computer-games console."
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'can't wait to do sth' = 'look forward to doing sth' (rất mong đợi làm gì)."
            },
            {
                "id": 6,
                "question": "Is it possible for me to come to your house at about 7p.m?",
                "translation": "Tôi có thể đến nhà bạn vào khoảng 7 giờ tối được không?",
                "options": [
                    "A. Must I come over to your house at about 7p.m?",
                    "B. Can I come to your house at about 7p.m?",
                    "C. Could I be come to your house at about 7p.m?",
                    "D. Will I come to your house at about 7p.m?"
                ],
                "answer": "B",
                "explanation": "Đáp án B đúng vì 'Is it possible for me to...' = 'Can I...' (Tôi có thể... không). C sai ngữ pháp, A và D sai ý nghĩa."
            },
            {
                "id": 7,
                "question": "The library stays open until seven o'clock.",
                "translation": "Thư viện mở cửa đến 7 giờ.",
                "options": [
                    "A. The library doesn't close until seven o'clock.",
                    "B. Not until seven o'clock does the library open.",
                    "C. Not until seven o'clock the library doesn't close.",
                    "D. Not until seven o'clock does the library stay close."
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'stays open until' = 'doesn't close until' (không đóng cửa cho đến khi)."
            },
            {
                "id": 8,
                "question": "Although my father's always busy, he often helps me with my homework.",
                "translation": "Mặc dù bố tôi luôn bận rộn, ông ấy thường giúp tôi làm bài tập về nhà.",
                "options": [
                    "A. My father's always busy because he often helps me with my homework.",
                    "B. My father's always busy, and he often helps me with my homework.",
                    "C. My father's always busy, so he often helps me with my homework.",
                    "D. My father's always busy, but he often helps me with my homework."
                ],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'Although' (mặc dù) thể hiện sự tương phản, tương đương với 'but' (nhưng)."
            },
            {
                "id": 9,
                "question": "We started cooking for the party four hours ago.",
                "translation": "Chúng tôi bắt đầu nấu ăn cho bữa tiệc bốn giờ trước.",
                "options": [
                    "A. We began to cook for the party for four hours.",
                    "B. We have been cooked for the party for four hours.",
                    "C. We have been cooking for the party for four hours.",
                    "D. We cooked for the party four hours ago."
                ],
                "answer": "C",
                "explanation": "Đáp án C đúng vì diễn tả hành động bắt đầu trong quá khứ và vẫn tiếp tục đến hiện tại (thì hiện tại hoàn thành tiếp diễn)."
            },
            {
                "id": 10,
                "question": "No one in the team can play better than John.",
                "translation": "Không ai trong đội có thể chơi tốt hơn John.",
                "options": [
                    "A. John as well as other players of the team plays very well.",
                    "B. John plays well but the others play better.",
                    "C. John is the best player of the team.",
                    "D. Everyone in the team, but John, plays very well."
                ],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'no one can play better than John' = 'John is the best player' (John là người chơi giỏi nhất)."
            },
            {
                "id": 11,
                "question": "Sorry, I took you someone else.",
                "translation": "Xin lỗi, tôi đã nhầm bạn với ai đó.",
                "options": [
                    "A. Sorry, I thought you were somebody else.",
                    "B. Sorry, I made a mistake in taking you to someone else.",
                    "C. Sorry, I took you instead of somebody else.",
                    "D. Sorry, I asked somebody to take you."
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'took you someone else' = 'thought you were somebody else' (nghĩ bạn là người khác)."
            },
            {
                "id": 12,
                "question": "Many think that Steve stole the money.",
                "translation": "Nhiều người nghĩ rằng Steve đã ăn cắp tiền.",
                "options": [
                    "A. Steve is thought to have stolen the money.",
                    "B. The money is thought to be stolen by Steve.",
                    "C. It was not Steve who stole the money.",
                    "D. Many people think the money is stolen by Steve."
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì đây là cấu trúc bị động với động từ tri giác: 'people think that S V' → 'S is thought to V'."
            },
            {
                "id": 13,
                "question": "I spent a long time getting over the disappointment of losing the match.",
                "translation": "Tôi đã mất nhiều thời gian để vượt qua sự thất vọng vì thua trận đấu.",
                "options": [
                    "A. It took me long to forget the disappointment of losing the match.",
                    "B. It took me long to stop disappointing you.",
                    "C. Getting over the disappointment took me a long time than the match.",
                    "D. Losing the match disappointed me too much."
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'spent time doing sth' = 'it took time to do sth' (mất bao nhiêu thời gian để làm gì)."
            },
            {
                "id": 14,
                "question": "His eel soup is better than any other soups I have ever eaten.",
                "translation": "Súp lươn của anh ấy ngon hơn bất kỳ món súp nào khác mà tôi từng ăn.",
                "options": [
                    "A. Of all the soups I have ever eaten, his eel soup is the best.",
                    "B. I have ever eaten many soups that are better than his eel soup.",
                    "C. His eel soup is good but I have ever eaten many others better.",
                    "D. His eel soup is the worst of all soups I have eaten."
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'better than any other' = 'the best of all' (tốt nhất trong tất cả)."
            },
            {
                "id": 15,
                "question": "I haven't visited my hometown for a few years.",
                "translation": "Tôi đã không về thăm quê hương được vài năm rồi.",
                "options": [
                    "A. I last visited my hometown a few years ago.",
                    "B. I was in my hometown for a few years.",
                    "C. I didn't visit my hometown a few years ago.",
                    "D. I have been in my hometown for a few years."
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'haven't visited for a few years' = 'last visited a few years ago' (lần cuối về thăm là vài năm trước)."
            },
            {
                "id": 16,
                "question": "He couldn't stand being eliminated from the contest.",
                "translation": "Anh ấy không thể chịu đựng được việc bị loại khỏi cuộc thi.",
                "options": [
                    "A. He didn't believe that he was thrown out from the contest.",
                    "B. Because he stood, he was eliminated from the contest.",
                    "C. He was eliminated from the contest because he was unable to stand.",
                    "D. He was unable to accept the failure in the contest."
                ],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'couldn't stand being eliminated' = 'was unable to accept the failure' (không thể chấp nhận thất bại)."
            },
            {
                "id": 17,
                "question": "He sang very badly. Everyone left the room.",
                "translation": "Anh ấy hát rất tệ. Mọi người rời khỏi phòng.",
                "options": [
                    "A. He sang so badly but everyone left the room.",
                    "B. He sang badly as a result of everyone leaving the room.",
                    "C. He sang very badly, so everyone left the room.",
                    "D. Everyone left the room, so he sang badly."
                ],
                "answer": "C",
                "explanation": "Đáp án C đúng vì thể hiện mối quan hệ nguyên nhân - kết quả: hát tệ → mọi người rời đi."
            },
            {
                "id": 18,
                "question": "Your birthday party was the last time I really enjoyed myself.",
                "translation": "Bữa tiệc sinh nhật của bạn là lần cuối cùng tôi thực sự vui vẻ.",
                "options": [
                    "A. Your last birthday party wasn't really enjoyed to me.",
                    "B. I didn't really enjoy myself at your birthday party.",
                    "C. I haven't really enjoyed myself since your birthday party.",
                    "D. I haven't been to your birthday party lastly as I really enjoyed myself."
                ],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'was the last time I enjoyed' = 'haven't enjoyed since' (chưa vui kể từ lần đó)."
            },
            {
                "id": 19,
                "question": "'I came back to my town last Sunday.' said Mr. Pitt.",
                "translation": "'Tôi đã trở về thị trấn của tôi vào Chủ nhật tuần trước.' ông Pitt nói.",
                "options": [
                    "A. Mr. Pitt said that I had come back to his town the Sunday before.",
                    "B. Mr. Pitt said that he came back to his town the Sunday before.",
                    "C. Mr. Pitt said that I had come back to his town last Sunday.",
                    "D. Mr. Pitt said that he had come back to his town the Sunday before."
                ],
                "answer": "D",
                "explanation": "Đáp án D đúng vì trong câu tường thuật: 'I' → 'he', 'last Sunday' → 'the Sunday before', thì quá khứ → quá khứ hoàn thành."
            },
            {
                "id": 20,
                "question": "Nick is lazy, so he is punished.",
                "translation": "Nick lười biếng, vì vậy anh ấy bị phạt.",
                "options": [
                    "A. Nick would not be punished if he were not lazy.",
                    "B. If Nick is not lazy, he would not be punished.",
                    "C. If Nick were lazy, he would be punished.",
                    "D. If Nick were not lazy, he would be punished."
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì đây là câu điều kiện loại 2 diễn tả điều kiện trái với hiện tại: 'is lazy' → 'were not lazy', 'is punished' → 'would not be punished'."
            }
        ]
        
        # ===================== PART 2: 20 CÂU (4 PASSAGES) =====================
        self.part2_passages = {
            "passage1": {
                "title": "The Beatles",
                "text": "In the 1960s, The Beatles were probably the most famous pop group in the whole world. Since then, there have been a great many groups that have achieved enormous fame, so it is perhaps difficult now to imagine how sensational The Beatles were at that time. They were four boys from the north of England and none of them had any training in music. They started by performing and recording songs by black Americans and they had some success with these songs. Then they started writing their own songs and that was when they became really popular. The Beatles changed pop music. They were the first pop group to achieve great success from songs they had written themselves. After that it became common for groups and singers to write their own songs. The Beatles did not have a long career. Their first hit record was in 1963 and they split up in 1970. They stopped doing live performances in 1966 because it had become too dangerous for them – their fans were so excited that they surrounded them and tried to take their clothes as souvenirs! However, today some of their songs remain as famous as they were when they first came out. Throughout the world many people can sing part of a Beatles song if you ask them.",
                "translation": "Vào những năm 1960, The Beatles có lẽ là nhóm nhạc pop nổi tiếng nhất trên toàn thế giới. Kể từ đó, đã có rất nhiều nhóm nhạc đạt được danh tiếng lớn, vì vậy có lẽ bây giờ khó có thể tưởng tượng được The Beatles đã gây chấn động như thế nào vào thời điểm đó. Họ là bốn chàng trai đến từ miền bắc nước Anh và không ai trong số họ được đào tạo về âm nhạc. Họ bắt đầu bằng việc biểu diễn và thu âm các bài hát của người Mỹ da đen và họ đã có một số thành công với những bài hát này. Sau đó họ bắt đầu viết các bài hát của riêng mình và đó là khi họ trở nên thực sự nổi tiếng. The Beatles đã thay đổi nhạc pop. Họ là nhóm nhạc pop đầu tiên đạt được thành công lớn từ những bài hát do chính họ sáng tác. Sau đó, việc các nhóm nhạc và ca sĩ tự viết bài hát của mình trở nên phổ biến. The Beatles không có sự nghiệp lâu dài. Đĩa đơn hit đầu tiên của họ là vào năm 1963 và họ tan rã vào năm 1970. Họ ngừng biểu diễn trực tiếp vào năm 1966 vì nó đã trở nên quá nguy hiểm đối với họ - người hâm mộ của họ quá phấn khích đến mức vây quanh họ và cố gắng lấy quần áo của họ làm kỷ vật! Tuy nhiên, ngày nay một số bài hát của họ vẫn nổi tiếng như khi chúng mới ra mắt. Trên khắp thế giới, nhiều người có thể hát một phần bài hát của The Beatles nếu bạn yêu cầu họ.",
                "questions": [
                    {
                        "id": 1,
                        "question": "The passage is mainly about ______",
                        "translation": "Đoạn văn chủ yếu nói về ______",
                        "options": [
                            "A. the Beatles' fame and success",
                            "B. how the Beatles became more successful than other groups",
                            "C. why the Beatles split up after 7 years", 
                            "D. many people's ability to sing a Beatles song"
                        ],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì toàn bộ đoạn văn tập trung vào sự nổi tiếng và thành công của The Beatles."
                    },
                    {
                        "id": 2,
                        "question": "The word 'sensational' is closest in meaning to ______",
                        "translation": "Từ 'sensational' gần nghĩa nhất với ______",
                        "options": [
                            "A. shocking",
                            "B. bad", 
                            "C. notorious",
                            "D. popular"
                        ],
                        "answer": "D",
                        "explanation": "Đáp án D đúng vì 'sensational' trong ngữ cảnh này có nghĩa là 'gây chấn động, rất nổi tiếng', gần nghĩa với 'popular'."
                    },
                    {
                        "id": 3,
                        "question": "What is NOT TRUE about the Beatles?",
                        "translation": "Điều nào KHÔNG ĐÚNG về The Beatles?",
                        "options": [
                            "A. They had a long stable career.",
                            "B. The members had no training in music.",
                            "C. They became famous when they wrote their own songs.",
                            "D. They changed pop music."
                        ],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì đoạn văn nói 'The Beatles did not have a long career' - sự nghiệp của họ không dài."
                    },
                    {
                        "id": 4,
                        "question": "The Beatles stopped their live performances because ______",
                        "translation": "The Beatles ngừng biểu diễn trực tiếp vì ______",
                        "options": [
                            "A. They were afraid of being hurt by fans.",
                            "B. They did not want to work with each other.",
                            "C. They spent more time writing their own songs.",
                            "D. They had earned enough money."
                        ],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì đoạn văn nói 'it had become too dangerous for them' - quá nguy hiểm cho họ do người hâm mộ quá cuồng nhiệt."
                    },
                    {
                        "id": 5,
                        "question": "The tone of the passage is that of ______",
                        "translation": "Giọng điệu của đoạn văn là ______",
                        "options": [
                            "A. neutral",
                            "B. criticism",
                            "C. admiration",
                            "D. pleasant"
                        ],
                        "answer": "C",
                        "explanation": "Đáp án C đúng vì đoạn văn thể hiện sự ngưỡng mộ đối với thành công và ảnh hưởng của The Beatles."
                    }
                ]
            },
            "passage2": {
                "title": "Orbis Organization",
                "text": "Orbis is an organization which helps blind people everywhere. It has built an eye hospital inside an aeroplane and flown it all over the world with an international medical team. Samantha Graham, a fourteen-year-old schoolgirl from England, went with the plane to Mongolia. Samantha tells a story of Eukhtuul, a young Mongolian girl.\n\n'Last year, when Eukhtuul was walking from home, she was attacked by boys with sticks and her eyes were badly damaged. Dr. Duffrey, an Orbis doctor, said that without an operation she would never see again. I thought about all the everyday things I do that she couldn't, things like reading school books, watching television, seeing friends, and I realized how lucky I am.'\n\n'The Orbis team agreed to operate on Eukhtuul and I was allowed to watch, together with some Mongolian medical students. I prayed the operation would be successful. The next day, I sat nervously with Eukhtuul while Dr. Duffrey removed her bandages. In six months, your sight will back to normal,' he said. Eukhtuul smiled, her mother cried, and I had to wipe away some tears, too!'\n\n'Now Eukhtuul wants to study hard to become a doctor. Her whole future has changed, thanks to simple operation. We should all think more about how much our sight means to us.'",
                "translation": "Orbis là một tổ chức giúp đỡ người mù ở khắp mọi nơi. Họ đã xây dựng một bệnh viện mắt bên trong một chiếc máy bay và bay nó đi khắp thế giới cùng với một đội ngũ y tế quốc tế. Samantha Graham, một nữ sinh 14 tuổi đến từ Anh, đã đi cùng chiếc máy bay đến Mông Cổ. Samantha kể câu chuyện về Eukhtuul, một cô gái trẻ người Mông Cổ.\n\n'Năm ngoái, khi Eukhtuul đang đi bộ từ nhà, cô bị một nhóm con trai tấn công bằng gậy và đôi mắt của cô bị tổn thương nặng. Bác sĩ Duffrey, một bác sĩ của Orbis, nói rằng nếu không có phẫu thuật, cô sẽ không bao giờ nhìn thấy nữa. Tôi nghĩ về tất cả những việc hàng ngày tôi làm mà cô ấy không thể làm, như đọc sách giáo khoa, xem tivi, gặp gỡ bạn bè, và tôi nhận ra mình may mắn thế nào.'\n\n'Đội ngũ Orbis đồng ý phẫu thuật cho Eukhtuul và tôi được phép xem, cùng với một số sinh viên y khoa Mông Cổ. Tôi cầu nguyện ca phẫu thuật sẽ thành công. Ngày hôm sau, tôi ngồi lo lắng bên Eukhtuul trong khi bác sĩ Duffrey tháo băng cho cô. Sau sáu tháng, thị lực của cháu sẽ trở lại bình thường,' bác sĩ nói. Eukhtuul mỉm cười, mẹ cô khóc, và tôi cũng phải lau đi vài giọt nước mắt!'\n\n'Bây giờ Eukhtuul muốn học tập chăm chỉ để trở thành bác sĩ. Toàn bộ tương lai của cô đã thay đổi, nhờ vào ca phẫu thuật đơn giản. Tất cả chúng ta nên suy nghĩ nhiều hơn về việc thị lực của chúng ta có ý nghĩa như thế nào.'",
                "questions": [
                    {
                        "id": 1,
                        "question": "What is the writer's main purpose in writing the passage?",
                        "translation": "Mục đích chính của tác giả khi viết đoạn văn là gì?",
                        "options": [
                            "A. To describe a dangerous trip.",
                            "B. To explain how sight can be lost.",
                            "C. To warn against playing with sticks.",
                            "D. To report a patient's cure."
                        ],
                        "answer": "D",
                        "explanation": "Đáp án D đúng vì đoạn văn tập trung kể về việc chữa trị thành công cho bệnh nhân Eukhtuul."
                    },
                    {
                        "id": 2,
                        "question": "After meeting Eukhtuul, Samantha felt _____.",
                        "translation": "Sau khi gặp Eukhtuul, Samantha cảm thấy _____.",
                        "options": [
                            "A. surprised by Eukhtuul's courage",
                            "B. grateful for her own sight",
                            "C. proud of the doctor's skill",
                            "D. angry about Eukhtuul's experience"
                        ],
                        "answer": "B",
                        "explanation": "Đáp án B đúng vì Samantha nói 'I realized how lucky I am' - cô nhận ra mình may mắn thế nào khi có thị lực."
                    },
                    {
                        "id": 3,
                        "question": "What is the result of Eukhtuul's operation?",
                        "translation": "Kết quả của ca phẫu thuật của Eukhtuul là gì?",
                        "options": [
                            "A. She can see better but won't have normal eyes",
                            "B. She will need another operation.",
                            "C. She can already see perfectly again",
                            "D. After some time she will see as well as before"
                        ],
                        "answer": "D",
                        "explanation": "Đáp án D đúng vì bác sĩ nói 'In six months, your sight will back to normal' (Sau 6 tháng, thị lực của cháu sẽ trở lại bình thường)."
                    },
                    {
                        "id": 4,
                        "question": "Which of the postcard Samantha wrote to an English friend?",
                        "translation": "Bưu thiếp nào Samantha viết cho một người bạn Anh?",
                        "options": [
                            "A. Make sure you take care of your eyes because they're more valuable than you realize.",
                            "B. I'm staying with my friend Eukhtuul while I'm sightseeing in Mongolia.",
                            "C. You may have to fly a long way to have an operation you need, but the journey will be worth it.",
                            "D. I have visited a Mongolia and watched local doctors do an operation."
                        ],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì phản ánh thông điệp chính của câu chuyện: chúng ta nên trân trọng thị lực của mình."
                    },
                    {
                        "id": 5,
                        "question": "What can a reader learn about in this passage?",
                        "translation": "Người đọc có thể học được gì từ đoạn văn này?",
                        "options": [
                            "A. The best way of studying medicine.",
                            "B. The international work of some eye doctors.",
                            "C. The difficulties of blind travelers.",
                            "D. The life of schoolchildren in Mongolia."
                        ],
                        "answer": "B",
                        "explanation": "Đáp án B đúng vì đoạn văn nói về công việc quốc tế của các bác sĩ mắt thuộc tổ chức Orbis."
                    }
                ]
            },
            "passage3": {
                "title": "Medical Information Recall",
                "text": "Did you know that on average we forget about 80% of the medical information a doctor might give us? This fascinating information came to light as a result of a study carried out by Utrecht University. What is even more interesting is that almost half of what we think we remember is wrong.\n\nWhy do you think this is? Well, it's not as complicated as you may think. You see, going to the doctor fills most people with anxiety and when we are really nervous and stressed we are more likely to focus on the diagnosis rather than the treatment. Therefore, we know what is wrong with us but have no idea what to do about it.\n\nHere are some good tips to keep in mind when seeing a doctor. Always write down any important information. What would be even better is, if your doctor agreed, to record your consultation. This way, you can replay the advice at home, where you are more likely to absorb it. If you believe the situation is serious or you're really worried, seek the help of a family member. Just ask them to accompany you to listen in. This way you can be absolutely sure about what the doctor has told you and avoid falling into the same trap that most people do.",
                "translation": "Bạn có biết rằng trung bình chúng ta quên khoảng 80% thông tin y tế mà bác sĩ có thể cung cấp cho chúng ta không? Thông tin thú vị này đã được tiết lộ nhờ một nghiên cứu được thực hiện bởi Đại học Utrecht. Điều thậm chí còn thú vị hơn là gần một nửa những gì chúng ta nghĩ rằng mình nhớ là sai.\n\nTại sao bạn nghĩ điều này xảy ra? Thực ra, nó không phức tạp như bạn nghĩ. Bạn thấy đấy, việc đi khám bác sĩ khiến hầu hết mọi người lo lắng và khi chúng ta thực sự lo lắng và căng thẳng, chúng ta có xu hướng tập trung vào chẩn đoán hơn là điều trị. Do đó, chúng ta biết mình bị bệnh gì nhưng không biết phải làm gì về nó.\n\nDưới đây là một số mẹo hay cần ghi nhớ khi đi khám bác sĩ. Luôn ghi lại bất kỳ thông tin quan trọng nào. Sẽ tốt hơn nữa nếu bác sĩ của bạn đồng ý cho ghi âm buổi tư vấn. Bằng cách này, bạn có thể nghe lại lời khuyên ở nhà, nơi bạn có nhiều khả năng tiếp thu hơn. Nếu bạn tin rằng tình hình nghiêm trọng hoặc bạn thực sự lo lắng, hãy tìm sự giúp đỡ của một thành viên trong gia đình. Chỉ cần nhờ họ đi cùng để lắng nghe. Bằng cách này, bạn có thể hoàn toàn chắc chắn về những gì bác sĩ đã nói và tránh rơi vào cái bẫy giống như hầu hết mọi người.",
                "questions": [
                    {
                        "id": 1,
                        "question": "According to the passage, the information doctors give us ______.",
                        "translation": "Theo đoạn văn, thông tin bác sĩ cung cấp cho chúng ta ______.",
                        "options": [
                            "A. is mostly forgotten",
                            "B. is only 80% correct",
                            "C. is about 50% wrong",
                            "D. is usually not enough"
                        ],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì đoạn văn nói 'we forget about 80% of the medical information' - chúng ta quên khoảng 80% thông tin y tế."
                    },
                    {
                        "id": 2,
                        "question": "The word 'complicated' in the passage is opposite in meaning to ______.",
                        "translation": "Từ 'complicated' trong đoạn văn trái nghĩa với ______.",
                        "options": [
                            "A. good",
                            "B. quick",
                            "C. short",
                            "D. simple"
                        ],
                        "answer": "D",
                        "explanation": "Đáp án D đúng vì 'complicated' (phức tạp) trái nghĩa với 'simple' (đơn giản)."
                    },
                    {
                        "id": 3,
                        "question": "The author says that when people consult a doctor, ______.",
                        "translation": "Tác giả nói rằng khi mọi người tham khảo ý kiến bác sĩ, ______.",
                        "options": [
                            "A. they usually have a family member with them",
                            "B. they are interested in knowing what they should do",
                            "C. they always believe that their situation is serious",
                            "D. they only want to know what is wrong with them"
                        ],
                        "answer": "D",
                        "explanation": "Đáp án D đúng vì đoạn văn nói 'we are more likely to focus on the diagnosis rather than the treatment' - chúng ta tập trung vào chẩn đoán hơn là điều trị."
                    },
                    {
                        "id": 4,
                        "question": "The word 'absorb' in the passage is closest in meaning to ______.",
                        "translation": "Từ 'absorb' trong đoạn văn gần nghĩa nhất với ______.",
                        "options": [
                            "A. take in",
                            "B. inhale",
                            "C. swallow",
                            "D. digest"
                        ],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì 'absorb' trong ngữ cảnh này có nghĩa là 'tiếp thu, hiểu', tương đương với 'take in'."
                    },
                    {
                        "id": 5,
                        "question": "The author suggests recording the consultant in order to ______.",
                        "translation": "Tác giả đề xuất ghi âm buổi tư vấn để ______.",
                        "options": [
                            "A. refer to it later to better understand your condition",
                            "B. play it to your family members to get their opinions",
                            "C. replay it to write down any important information",
                            "D. use it as evidence against your doctor if necessary"
                        ],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì mục đích là 'you can replay the advice at home, where you are more likely to absorb it' - bạn có thể nghe lại lời khuyên để hiểu rõ hơn."
                    }
                ]
            },
            "passage4": {
                "title": "Saving Energy at Home",
                "text": "Saving energy means saving money. Home owners and renters know this basic fact, but they often don't know what kinds of adjustments they can make in their homes and apartments that will result in savings.\n\nFor those willing to spend some time and money to reap long-term energy savings, an energy audit is the way to go. An energy auditor will come into your home and assess its energy efficiency. The auditor will pinpoint areas of your home that use the most energy and offer solutions to lower your energy use and costs. Trained energy auditors know what to look for and can locate a variety of flaws that may be resulting in energy inefficiency, including inadequate insulation, construction flaws, and uneven heat distribution.\n\nThere are quicker and less costly measures that can be taken as well. One way to save money is to replace incandescent lights with fluorescents. This can result in a savings of more than 50% on your monthly lighting costs.\n\nWhen it's time to replace old appliances, it's wise to spend a bit more for an energy-efficient model, and be sure that you are taking advantage of energy-saving settings already on your current refrigerator, dishwasher, washing machine, or dryer.\n\nWindows provide another opportunity to cut your energy costs. Caulk old Windows that might be leaky to prevent drafts, and choose double-paned windows if you're building an addition or replacing old windows.\n\nMost areas of your home or apartment offer opportunities to save energy and money. The results are significant and are well worth the effort.",
                "translation": "Tiết kiệm năng lượng có nghĩa là tiết kiệm tiền. Chủ nhà và người thuê nhà biết sự thật cơ bản này, nhưng họ thường không biết những loại điều chỉnh nào họ có thể thực hiện trong nhà và căn hộ của mình để tiết kiệm.\n\nĐối với những người sẵn sàng dành thời gian và tiền bạc để thu được khoản tiết kiệm năng lượng lâu dài, kiểm toán năng lượng là cách để làm. Một kiểm toán viên năng lượng sẽ đến nhà bạn và đánh giá hiệu quả năng lượng của nó. Kiểm toán viên sẽ xác định các khu vực trong nhà bạn sử dụng nhiều năng lượng nhất và đưa ra giải pháp để giảm mức sử dụng năng lượng và chi phí của bạn. Các kiểm toán viên năng lượng được đào tạo biết phải tìm kiếm những gì và có thể xác định nhiều loại lỗi có thể dẫn đến kém hiệu quả năng lượng, bao gồm cách nhiệt không đầy đủ, lỗi xây dựng và phân phối nhiệt không đều.\n\nCũng có những biện pháp nhanh hơn và ít tốn kém hơn có thể được thực hiện. Một cách để tiết kiệm tiền là thay thế đèn sợi đốt bằng đèn huỳnh quang. Điều này có thể giúp tiết kiệm hơn 50% chi phí chiếu sáng hàng tháng của bạn.\n\nKhi đến lúc thay thế các thiết bị cũ, thật khôn ngoan khi chi thêm một chút cho một mẫu tiết kiệm năng lượng và đảm bảo rằng bạn đang tận dụng các cài đặt tiết kiệm năng lượng đã có trên tủ lạnh, máy rửa bát, máy giặt hoặc máy sấy hiện tại của bạn.\n\nCửa sổ cung cấp một cơ hội khác để cắt giảm chi phí năng lượng của bạn. Bịt kín các cửa sổ cũ có thể bị rò rỉ để ngăn gió lùa và chọn cửa sổ hai lớp nếu bạn đang xây thêm hoặc thay thế cửa sổ cũ.\n\nHầu hết các khu vực trong nhà hoặc căn hộ của bạn đều có cơ hội tiết kiệm năng lượng và tiền bạc. Kết quả là đáng kể và rất đáng để nỗ lực.",
                "questions": [
                    {
                        "id": 1,
                        "question": "Which two main organizational schemes can be identified in this passage?",
                        "translation": "Hai sơ đồ tổ chức chính nào có thể được xác định trong đoạn văn này?",
                        "options": [
                            "A. order by topic and cause and effect",
                            "B. hierarchical order and order by topic",
                            "C. hierarchical order and chronological order",
                            "D. chronological order and compare and contrast"
                        ],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì đoạn văn sắp xếp theo chủ đề và trình bày nguyên nhân - kết quả của việc tiết kiệm năng lượng."
                    },
                    {
                        "id": 2,
                        "question": "Which of the following ideas is NOT included in this passage?",
                        "translation": "Ý tưởng nào sau đây KHÔNG được đề cập trong đoạn văn này?",
                        "options": [
                            "A. Your local energy company will send an energy auditor at your request.",
                            "B. Double-paned windows can cut energy costs.",
                            "C. You can reduce your $130 monthly lighting costs to $65 by using fluorescent bulbs instead of incandescent.",
                            "D. Some appliances have energy-saving settings."
                        ],
                        "answer": "C",
                        "explanation": "Đáp án C đúng vì đoạn văn không đề cập cụ thể đến số tiền $130 hay $65, chỉ nói chung chung về việc tiết kiệm 50%."
                    },
                    {
                        "id": 3,
                        "question": "Which of the following best expresses the main idea of this passage?",
                        "translation": "Câu nào sau đây diễn đạt tốt nhất ý chính của đoạn văn này?",
                        "options": [
                            "A. There are many things a homeowner or renter can do to save energy and money.",
                            "B. Hiring an energy auditor will save energy and money.",
                            "C. Homeowners and renters don't know what they can do to save energy and money.",
                            "D. Replacing windows and light bulbs are well worth the effort and cost."
                        ],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì đây là ý chính xuyên suốt đoạn văn: có nhiều cách để chủ nhà hoặc người thuê nhà tiết kiệm năng lượng và tiền bạc."
                    },
                    {
                        "id": 4,
                        "question": "According to the passage, which of the following would an energy auditor NOT do?",
                        "translation": "Theo đoạn văn, kiểm toán viên năng lượng sẽ KHÔNG làm điều nào sau đây?",
                        "options": [
                            "A. Locate a variety of flaws that may result in energy inefficiency and fix them.",
                            "B. Look for problems with heat distribution.",
                            "C. Offer solutions to lower your energy costs.",
                            "D. Check for construction flaws."
                        ],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì kiểm toán viên chỉ 'pinpoint areas' (xác định khu vực) và 'offer solutions' (đề xuất giải pháp), không phải tự sửa chữa."
                    },
                    {
                        "id": 5,
                        "question": "According the passage, double-paned windows",
                        "translation": "Theo đoạn văn, cửa sổ hai lớp",
                        "options": [
                            "A. are energy efficient.",
                            "B. should only be used as replacement windows.",
                            "C. should only be used in new additions to homes.",
                            "D. will lower your heating costs by 50%."
                        ],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì đoạn văn khuyến nghị chọn cửa sổ hai lớp để tiết kiệm năng lượng, nghĩa là chúng hiệu quả năng lượng."
                    }
                ]
            }
        }
        
        # ===================== PART 3: 20 CÂU (4 PASSAGES) =====================
        self.part3_passages = [
            {
                "id": 1,
                "text": "Society has changed in many ways (1)____ the introduction of computers, and people's lives at home and at the office have been affected. Most people are working for fewer hours per week than they (2)____ to, and manufacturers and advertising agencies are becoming much more interested in how people spend this extra leisure time. One recent report stated that (3)____ the number of hobbies had not increased, each hobby had become more specialized. A second finding is that nowadays, many managers would rather (4)____ time with their families than stay late in the office every day. Home life is seen to be just as important as working. Some companies now (5)____ managers take their annual holidays even if they don't want to, because this leads to such an improvement in their performance if they have some rest.",
                "translation": "Xã hội đã thay đổi theo nhiều cách (1)____ việc giới thiệu máy tính, và cuộc sống của mọi người ở nhà và ở văn phòng đã bị ảnh hưởng. Hầu hết mọi người đang làm việc ít giờ hơn mỗi tuần so với họ (2)____, và các nhà sản xuất và các công ty quảng cáo đang trở nên quan tâm nhiều hơn đến cách mọi người sử dụng thời gian rảnh rỗi thêm này. Một báo cáo gần đây cho biết rằng (3)____ số lượng sở thích không tăng, mỗi sở thích đã trở nên chuyên biệt hơn. Một phát hiện thứ hai là ngày nay, nhiều nhà quản lý thích (4)____ thời gian với gia đình hơn là ở lại văn phòng muộn mỗi ngày. Cuộc sống gia đình được coi là quan trọng không kém làm việc. Một số công ty hiện nay (5)____ các nhà quản lý nghỉ phép hàng năm ngay cả khi họ không muốn, bởi vì điều này dẫn đến sự cải thiện đáng kể trong hiệu suất của họ nếu họ có một số thời gian nghỉ ngơi.",
                "questions": [
                    {
                        "id": 1,
                        "question": "Câu 1",
                        "options": ["A. for", "B. from", "C. at", "D. since"],
                        "answer": "D",
                        "explanation": "Đáp án D đúng vì 'since' + mốc thời gian (the introduction of computers)."
                    },
                    {
                        "id": 2,
                        "question": "Câu 2", 
                        "options": ["A. want", "B. used", "C. ought", "D. have"],
                        "answer": "B",
                        "explanation": "Đáp án B đúng vì 'used to' chỉ thói quen trong quá khứ (trước đây họ làm việc nhiều giờ hơn)."
                    },
                    {
                        "id": 3,
                        "question": "Câu 3",
                        "options": ["A. as", "B. although", "C. but", "D. because of"],
                        "answer": "B",
                        "explanation": "Đáp án B đúng vì 'although' (mặc dù) thể hiện sự tương phản: số lượng sở thích không tăng NHƯNG mỗi sở thích trở nên chuyên biệt hơn."
                    },
                    {
                        "id": 4,
                        "question": "Câu 4",
                        "options": ["A. spending", "B. spend", "C. spent", "D. to spend"],
                        "answer": "B",
                        "explanation": "Đáp án B đúng vì cấu trúc 'would rather + V(nguyên thể)' (thích làm gì hơn)."
                    },
                    {
                        "id": 5,
                        "question": "Câu 5",
                        "options": ["A. force", "B. have", "C. make", "D. cause"],
                        "answer": "C",
                        "explanation": "Đáp án C đúng vì 'make someone do something' (bắt ai làm gì) là cấu trúc phù hợp."
                    }
                ]
            },
            {
                "id": 2,
                "text": "Percy Ross was born in 1916 in Michigan. His parents has come to the USA from Latvia and Russia and the family were poor. But Percy soon showed a talent (6)______ business and made a fortune in the fur trade and auction business. Then disaster struck and he (7)______ all his money. But he soon made a fortune again - this time by (8)______ plastic bags. In 1969, he sold his plastic bag company for millions of dollars.\n\nRoss started giving money away in 1977: he gave $50,000 to 50 Vietnamese refugees so that they could make a new home in the USA. Then he held a Christmas party for 1,050 poor children in the American town of Minneapolis. Ross bought a bike for every one of the 1,050 children at the party.\n\nAfter these first experiences of giving money away, Ross decided to do it on a (9)______ basis. He started a newspaper column called 'Thanks a Million', and later a radio show, in order to give away his money. It took years, but Ross finally (10)______ in giving away his entire fortune.",
                "translation": "Percy Ross sinh năm 1916 tại Michigan. Cha mẹ ông đã đến Mỹ từ Latvia và Nga và gia đình rất nghèo. Nhưng Percy sớm bộc lộ tài năng (6)______ kinh doanh và kiếm được một gia tài trong ngành kinh doanh lông thú và đấu giá. Sau đó thảm họa ập đến và ông (7)______ tất cả số tiền của mình. Nhưng ông sớm kiếm được một gia tài một lần nữa - lần này bằng cách (8)______ túi nhựa. Năm 1969, ông đã bán công ty túi nhựa của mình với giá hàng triệu đô la.\n\nRoss bắt đầu cho tiền vào năm 1977: ông đã tặng 50.000 đô la cho 50 người tị nạn Việt Nam để họ có thể tạo dựng một mái ấm mới tại Mỹ. Sau đó, ông tổ chức một bữa tiệc Giáng sinh cho 1.050 trẻ em nghèo ở thị trấn Minneapolis của Mỹ. Ross đã mua một chiếc xe đạp cho mỗi đứa trẻ trong số 1.050 đứa trẻ tại bữa tiệc.\n\nSau những trải nghiệm đầu tiên này về việc cho tiền, Ross quyết định làm điều đó trên cơ sở (9)______. Ông bắt đầu một chuyên mục báo có tên 'Thanks a Million', và sau đó là một chương trình radio, để cho đi số tiền của mình. Phải mất nhiều năm, nhưng cuối cùng Ross đã (10)______ trong việc cho đi toàn bộ tài sản của mình.",
                "questions": [
                    {
                        "id": 6,
                        "question": "Câu 6",
                        "options": ["A. with", "B. for", "C. of", "D. on"],
                        "answer": "B",
                        "explanation": "Đáp án B đúng vì 'a talent for something' (tài năng về cái gì) là cụm từ cố định."
                    },
                    {
                        "id": 7,
                        "question": "Câu 7",
                        "options": ["A. threw", "B. sent", "C. lost", "D. wasted"],
                        "answer": "C",
                        "explanation": "Đáp án C đúng vì 'lost all his money' (mất hết tiền) là phù hợp với ngữ cảnh 'disaster struck' (thảm họa ập đến)."
                    },
                    {
                        "id": 8,
                        "question": "Câu 8",
                        "options": ["A. manufacturer", "B. manufactured", "C. manufacturing", "D. manufacture"],
                        "answer": "C",
                        "explanation": "Đáp án C đúng vì sau giới từ 'by' cần V-ing: 'by manufacturing plastic bags' (bằng cách sản xuất túi nhựa)."
                    },
                    {
                        "id": 9,
                        "question": "Câu 9",
                        "options": ["A. regular", "B. frequent", "C. occasional", "D. usual"],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì 'on a regular basis' (một cách thường xuyên, đều đặn) là cụm từ cố định."
                    },
                    {
                        "id": 10,
                        "question": "Câu 10",
                        "options": ["A. interested", "B. succeeded", "C. invested", "D. tried"],
                        "answer": "B",
                        "explanation": "Đáp án B đúng vì 'succeeded in doing something' (thành công trong việc làm gì) là cấu trúc đúng."
                    }
                ]
            },
            {
                "id": 3,
                "text": "The invention of the mobile phone has undoubtedly revolutionized the way people communicate and influenced every aspect of our lives. The issue is whether this technological innovation has (11)______ more harm than good. In order to (12)______ the question, we must first turn to the types of consumers. Presumably, most parents (13)______ are always worrying about their children's safety buy mobile phones for them to track their whereabouts. We can also assume that most teenagers want mobile phones to avoid missing out on social contact. In this context, the advantages are clear. (14)______, we cannot deny the fact that text messages have been used by bullies to intimidate fellow students. There is also (15)______ evidence that texting has affected literacy skills.",
                "translation": "Sự phát minh của điện thoại di động chắc chắn đã cách mạng hóa cách mọi người giao tiếp và ảnh hưởng đến mọi khía cạnh của cuộc sống chúng ta. Vấn đề là liệu sự đổi mới công nghệ này đã (11)______ nhiều tác hại hơn lợi ích hay không. Để (12)______ câu hỏi này, trước tiên chúng ta phải xem xét các loại người tiêu dùng. Có lẽ, hầu hết các bậc cha mẹ (13)______ luôn lo lắng về sự an toàn của con cái họ mua điện thoại di động cho chúng để theo dõi vị trí của chúng. Chúng ta cũng có thể cho rằng hầu hết thanh thiếu niên muốn có điện thoại di động để tránh bỏ lỡ các liên hệ xã hội. Trong bối cảnh này, những lợi ích là rõ ràng. (14)______, chúng ta không thể phủ nhận thực tế rằng tin nhắn văn bản đã được những kẻ bắt nạt sử dụng để đe dọa bạn học. Cũng có (15)______ bằng chứng rằng nhắn tin đã ảnh hưởng đến kỹ năng đọc viết.",
                "questions": [
                    {
                        "id": 11,
                        "question": "Câu 11",
                        "options": ["A. brought", "B. played", "C. made", "D. done"],
                        "answer": "D",
                        "explanation": "Đáp án D đúng vì 'do more harm than good' (gây nhiều tác hại hơn lợi ích) là thành ngữ cố định."
                    },
                    {
                        "id": 12,
                        "question": "Câu 12",
                        "options": ["A. answer", "B. address", "C. remedy", "D. put right"],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì 'answer the question' (trả lời câu hỏi) là phù hợp nhất với ngữ cảnh."
                    },
                    {
                        "id": 13,
                        "question": "Câu 13",
                        "options": ["A. what", "B. whom", "C. which", "D. who"],
                        "answer": "D",
                        "explanation": "Đáp án D đúng vì 'who' thay thế cho 'parents' (người) làm chủ ngữ trong mệnh đề quan hệ."
                    },
                    {
                        "id": 14,
                        "question": "Câu 14",
                        "options": ["A. Therefore", "B. Moreover", "C. However", "D. So that"],
                        "answer": "C",
                        "explanation": "Đáp án C đúng vì 'however' (tuy nhiên) thể hiện sự tương phản giữa lợi ích và tác hại."
                    },
                    {
                        "id": 15,
                        "question": "Câu 15",
                        "options": ["A. indisputable", "B. arguable", "C. doubtless", "D. unhesitating"],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì 'indisputable evidence' (bằng chứng không thể chối cãi) là phù hợp với ngữ cảnh."
                    }
                ]
            },
            {
                "id": 4,
                "text": "(16)______ breakfast Americans will eat cereal with milk which are often mixed (17)______ in a bowl, a glass of orange juice, and toasted bread or muffin with jam, butter, or margarine. Another common breakfast meal is scrambled eggs or an omelet with potatoes and breakfast meat (bacon or sausage). People who are on (18)______ eat just a cup of yogurt. Lunch and dinner are more (19)______ When eating at a formal dinner, you may be overwhelmed by the number of utensils. How do you tell the difference between a salad fork, a butter fork, and a dessert fork? Most Americans do not know the answer (20)______. But knowing which fork or spoon to use first is simple: use the outermost utensils first and the utensils closest to the plate last.",
                "translation": "(16)______ bữa sáng người Mỹ sẽ ăn ngũ cốc với sữa thường được trộn (17)______ trong một cái bát, một ly nước cam, và bánh mì nướng hoặc bánh nướng xốp với mứt, bơ, hoặc bơ thực vật. Một bữa sáng phổ biến khác là trứng bác hoặc trứng ốp la với khoai tây và thịt ăn sáng (thịt xông khói hoặc xúc xích). Những người đang (18)______ chỉ ăn một cốc sữa chua. Bữa trưa và bữa tối thì (19)______ hơn. Khi ăn một bữa tối trang trọng, bạn có thể bị choáng ngợp bởi số lượng dụng cụ ăn uống. Làm thế nào để bạn phân biệt giữa nĩa salad, nĩa bơ và nĩa tráng miệng? Hầu hết người Mỹ không biết câu trả lời (20)______. Nhưng biết nĩa hoặc thìa nào sử dụng trước rất đơn giản: sử dụng dụng cụ ngoài cùng đầu tiên và dụng cụ gần đĩa nhất cuối cùng.",
                "questions": [
                    {
                        "id": 16,
                        "question": "Câu 16",
                        "options": ["A. With", "B. In", "C. At", "D. For"],
                        "answer": "D",
                        "explanation": "Đáp án D đúng vì 'for breakfast' (cho bữa sáng) là cụm từ chỉ bữa ăn."
                    },
                    {
                        "id": 17,
                        "question": "Câu 17",
                        "options": ["A. others", "B. each other", "C. one another", "D. together"],
                        "answer": "D",
                        "explanation": "Đáp án D đúng vì 'mixed together' (trộn lẫn với nhau) là phù hợp nhất trong ngữ cảnh này."
                    },
                    {
                        "id": 18,
                        "question": "Câu 18",
                        "options": ["A. diet", "B. holiday", "C. engagement", "D. duty"],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì 'on a diet' (ăn kiêng) là cụm từ cố định."
                    },
                    {
                        "id": 19,
                        "question": "Câu 19",
                        "options": ["A. varied", "B. vary", "C. variety", "D. variously"],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì cần tính từ 'varied' (đa dạng) để bổ nghĩa cho danh từ 'lunch and dinner'."
                    },
                    {
                        "id": 20,
                        "question": "Câu 20",
                        "options": ["A. either", "B. too", "C. so", "D. neither"],
                        "answer": "A",
                        "explanation": "Đáp án A đúng vì 'either' dùng trong câu phủ định: 'do not know the answer either' (cũng không biết câu trả lời)."
                    }
                ]
            }
        ]
        
        # ===================== PART 4: 60 CÂU =====================
        self.part4_questions = [
            {
                "id": 1,
                "question": "I ______ my sister in December as planned.",
                "translation": "Tôi ______ gặp chị gái tôi vào tháng 12 như kế hoạch.",
                "options": ["A. will see", "B. have seen", "C. am going to see", "D. see"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'am going to' diễn tả kế hoạch đã được lập từ trước."
            },
            {
                "id": 2,
                "question": "He seems quite ______ with his new job.",
                "translation": "Anh ấy có vẻ khá ______ với công việc mới của mình.",
                "options": ["A. satisfied", "B. satisfy", "C. satisfying", "D. satisfies"],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'satisfied' là tính từ ở dạng bị động: cảm thấy hài lòng."
            },
            {
                "id": 3,
                "question": "- 'How was the game show last night?' - '______'",
                "translation": "- 'Chương trình trò chơi tối qua thế nào?' - '______'",
                "options": [
                    "A. Great. I gained more knowledge about biology.",
                    "B. Just talking about it.",
                    "C. It showed at 8 o'clock.",
                    "D. I think it wasn't a good game."
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì đây là câu trả lời trực tiếp và đầy đủ cho câu hỏi về cảm nhận."
            },
            {
                "id": 4,
                "question": "Internet cafes allow you ______ your web-based email account.",
                "translation": "Quán cà phê internet cho phép bạn ______ tài khoản email dựa trên web của bạn.",
                "options": ["A. be accessed", "B. accessing", "C. access", "D. to access"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì cấu trúc 'allow someone to do something' (cho phép ai làm gì)."
            },
            {
                "id": 5,
                "question": "- Where is Jimmy? - He is ______ work. He is busy ______ his monthly report.",
                "translation": "- Jimmy đâu? - Anh ấy đang ______ làm việc. Anh ấy đang bận ______ báo cáo hàng tháng của mình.",
                "options": ["A. in / about", "B. at / with", "C. to / through", "D. on / for"],
                "answer": "B",
                "explanation": "Đáp án B đúng vì 'at work' (đang làm việc) và 'busy with something' (bận với cái gì)."
            },
            {
                "id": 6,
                "question": "Are you looking forward ______ on your vacation?",
                "translation": "Bạn có mong đợi ______ vào kỳ nghỉ của mình không?",
                "options": ["A. going", "B. to going", "C. to go", "D. you go"],
                "answer": "B",
                "explanation": "Đáp án B đúng vì 'look forward to + V-ing' (mong đợi làm gì)."
            },
            {
                "id": 7,
                "question": "______ is the controller of the body.",
                "translation": "______ là bộ điều khiển của cơ thể.",
                "options": [
                    "A. Nervous System",
                    "B. Digestive System", 
                    "C. Skeletal System",
                    "D. Circulatory System"
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì hệ thần kinh (Nervous System) điều khiển mọi hoạt động của cơ thể."
            },
            {
                "id": 8,
                "question": "It is thought that Google ______ cars may transform the way we move around cities in the future.",
                "translation": "Người ta nghĩ rằng xe hơi ______ của Google có thể thay đổi cách chúng ta di chuyển quanh các thành phố trong tương lai.",
                "options": ["A. motionless", "B. driver", "C. driverless", "D. driving"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'driverless cars' (xe không người lái) là công nghệ của Google."
            },
            {
                "id": 9,
                "question": "Do you get ______ if your parents ask you to help out in your free time?",
                "translation": "Bạn có cảm thấy ______ nếu bố mẹ yêu cầu bạn giúp đỡ trong thời gian rảnh không?",
                "options": ["A. boring", "B. exciting", "C. annoyed", "D. annoying"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'annoyed' (bực mình, khó chịu) mô tả cảm xúc của người bị làm phiền."
            },
            {
                "id": 10,
                "question": "I ______ buy a new car, so I'm saving as much money as possible.",
                "translation": "Tôi ______ mua một chiếc xe hơi mới, vì vậy tôi đang tiết kiệm càng nhiều tiền càng tốt.",
                "options": ["A. am going to", "B. will be", "C. can", "D. will"],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'am going to' diễn tả kế hoạch đã được quyết định từ trước."
            },
            {
                "id": 11,
                "question": "YouTube ______ to become the world most popular video-sharing website since 2005.",
                "translation": "YouTube ______ trở thành trang web chia sẻ video phổ biến nhất thế giới từ năm 2005.",
                "options": ["A. grows", "B. grew", "C. have grown", "D. has grown"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì thì hiện tại hoàn thành với 'since 2005': 'has grown'."
            },
            {
                "id": 12,
                "question": "We are talking about the writer ______ latest book is one of the best-sellers this year.",
                "translation": "Chúng tôi đang nói về nhà văn ______ cuốn sách mới nhất là một trong những sách bán chạy nhất năm nay.",
                "options": ["A. whom", "B. who", "C. whose", "D. which"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'whose' là đại từ quan hệ chỉ sở hữu: 'cuốn sách của nhà văn'."
            },
            {
                "id": 13,
                "question": "Your job is likely to include welcoming guests and receiving ______ for our Charity Centre.",
                "translation": "Công việc của bạn có thể bao gồm chào đón khách và nhận ______ cho Trung tâm Từ thiện của chúng tôi.",
                "options": ["A. donated", "B. donate", "C. donors", "D. donations"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'receiving donations' (nhận quyên góp) là phù hợp với ngữ cảnh từ thiện."
            },
            {
                "id": 14,
                "question": "______ is the member of a family who earns the money that the family needs.",
                "translation": "______ là thành viên trong gia đình kiếm tiền mà gia đình cần.",
                "options": ["A. Homemaker", "B. Husband", "C. Women", "D. Breadwinner"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'breadwinner' (người trụ cột) là người kiếm tiền nuôi gia đình."
            },
            {
                "id": 15,
                "question": "If you ______ the doctor's advice, you won't get well.",
                "translation": "Nếu bạn ______ lời khuyên của bác sĩ, bạn sẽ không khỏi bệnh.",
                "options": ["A. don't listen", "B. take", "C. ignore", "D. follow"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'ignore the doctor's advice' (phớt lờ lời khuyên của bác sĩ) dẫn đến không khỏi bệnh."
            },
            {
                "id": 16,
                "question": "The father typically works outside the home while the mother is ______ domestic duties such as homemaking and raising children.",
                "translation": "Người cha thường làm việc bên ngoài gia đình trong khi người mẹ ______ các nhiệm vụ gia đình như nội trợ và nuôi dạy con cái.",
                "options": ["A. aware of", "B. capable of", "C. suitable for", "D. responsible for"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'responsible for' (chịu trách nhiệm về) là phù hợp nhất."
            },
            {
                "id": 17,
                "question": "The more polite you appear to be, ______ your partner will be.",
                "translation": "Bạn càng tỏ ra lịch sự, ______ đối tác của bạn sẽ càng.",
                "options": ["A. the happiest", "B. the more happily", "C. the happier", "D. the most happily"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì cấu trúc so sánh kép: 'The more + adj, the more + adj'."
            },
            {
                "id": 18,
                "question": "John made me ______ a lot with his hilarious jokes.",
                "translation": "John khiến tôi ______ rất nhiều với những câu chuyện cười vui nhộn của anh ấy.",
                "options": ["A. laugh", "B. laughed", "C. laughing", "D. to laugh"],
                "answer": "A",
                "explanation": "Đáp án A đúng vì cấu trúc 'make someone do something' (khiến ai làm gì) + V nguyên thể."
            },
            {
                "id": 19,
                "question": "Only humans produce ______ tears.",
                "translation": "Chỉ con người sản xuất nước mắt ______.",
                "options": ["A. false", "B. emotional", "C. crocodile", "D. feel"],
                "answer": "B",
                "explanation": "Đáp án B đúng vì 'emotional tears' (nước mắt cảm xúc) là đặc trưng chỉ có ở con người."
            },
            {
                "id": 20,
                "question": "Treat others the way you want ______",
                "translation": "Đối xử với người khác theo cách bạn muốn ______",
                "options": ["A. to treat", "B. to be treat", "C. to be treated", "D. treating"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'want to be treated' (muốn được đối xử) ở dạng bị động."
            },
            {
                "id": 21,
                "question": "Her husband is very kind. He always cares about her and never puts all of the housework______ her.",
                "translation": "Chồng cô ấy rất tử tế. Anh ấy luôn quan tâm đến cô và không bao giờ đổ hết việc nhà ______ cô.",
                "options": ["A. in", "B. on", "C. about", "D. with"],
                "answer": "B",
                "explanation": "Đáp án B đúng vì 'put something on someone' (đổ cái gì lên ai, bắt ai làm cái gì)."
            },
            {
                "id": 22,
                "question": "Don't phone me between 6.00 and 9.00 tonight. I ______ then.",
                "translation": "Đừng gọi điện cho tôi từ 6.00 đến 9.00 tối nay. Tôi ______ lúc đó.",
                "options": ["A. will study", "B. am studying", "C. will be studying", "D. study"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì thì tương lai tiếp diễn 'will be studying' diễn tả hành động đang diễn ra tại một thời điểm cụ thể trong tương lai."
            },
            {
                "id": 23,
                "question": "American Idol began in 2002, ______ quickly became the most popular entertainment series with viewers in the hundreds of millions.",
                "translation": "American Idol bắt đầu vào năm 2002, ______ nhanh chóng trở thành loạt phim giải trí phổ biến nhất với hàng trăm triệu người xem.",
                "options": ["A. so", "B. but", "C. or", "D. and"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'and' (và) nối hai mệnh đề có quan hệ bổ sung."
            },
            {
                "id": 24,
                "question": "After eating dinner, I have to do the ______ and then do my homework every day.",
                "translation": "Sau khi ăn tối, tôi phải làm ______ và sau đó làm bài tập về nhà mỗi ngày.",
                "options": ["A. wash-up", "B. washing-ups", "C. washing-up", "D. washings-up"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'the washing-up' (việc rửa bát) là danh từ không đếm được."
            },
            {
                "id": 25,
                "question": "He asked me why ______ to the meeting.",
                "translation": "Anh ấy hỏi tôi tại sao ______ cuộc họp.",
                "options": ["A. you didn't come", "B. I hadn't come", "C. didn't I come", "D. don't I come"],
                "answer": "B",
                "explanation": "Đáp án B đúng vì trong câu tường thuật: thì quá khứ hoàn thành 'hadn't come' và đổi 'you' → 'I'."
            },
            {
                "id": 26,
                "question": "I'm responsible for cooking dinner as my mother usually works______.",
                "translation": "Tôi chịu trách nhiệm nấu bữa tối vì mẹ tôi thường làm việc ______.",
                "options": ["A. lately", "B. later", "C. early", "D. late"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'works late' (làm việc muộn) là phù hợp với ngữ cảnh."
            },
            {
                "id": 27,
                "question": "He passed his exams ______.",
                "translation": "Anh ấy đã vượt qua các kỳ thi của mình ______.",
                "options": ["A. successes", "B. successful", "C. successfully", "D. success"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì cần trạng từ 'successfully' (một cách thành công) để bổ nghĩa cho động từ 'passed'."
            },
            {
                "id": 28,
                "question": "All forms of discrimination against all women and girls ______ immediately everywhere.",
                "translation": "Mọi hình thức phân biệt đối xử đối với tất cả phụ nữ và trẻ em gái ______ ngay lập tức ở mọi nơi.",
                "options": ["A. must be taken away", "B. must be followed", "C. must be allowed", "D. must be ended"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'discrimination must be ended' (phân biệt đối xử phải được chấm dứt) là phù hợp."
            },
            {
                "id": 29,
                "question": "Paddle-wheel machine helps to clean the wastewater before ______ it for farming.",
                "translation": "Máy bánh xe guồng giúp làm sạch nước thải trước khi ______ nó cho nông nghiệp.",
                "options": ["A. recycling", "B. reducing", "C. rearranging", "D. reusing"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'reusing water' (tái sử dụng nước) là phù hợp với ngữ cảnh."
            },
            {
                "id": 30,
                "question": "Today my mother can't help ______ the cooking because she is ill.",
                "translation": "Hôm nay mẹ tôi không thể giúp ______ nấu ăn vì bà ốm.",
                "options": ["A. for", "B. with", "C. of", "D. in"],
                "answer": "B",
                "explanation": "Đáp án B đúng vì 'can't help with something' (không thể giúp việc gì)."
            },
            {
                "id": 31,
                "question": "My teacher assigned us a writing task about______ of our favorite singers.",
                "translation": "Giáo viên của tôi giao cho chúng tôi một bài tập viết về ______ của ca sĩ yêu thích của chúng tôi.",
                "options": ["A. biography", "B. biodiversity", "C. biology", "D. biochemist"],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'biography' (tiểu sử) là phù hợp với ngữ cảnh viết về ca sĩ."
            },
            {
                "id": 32,
                "question": "I'd like ______ all of you to enjoy my party on this Friday.",
                "translation": "Tôi muốn ______ tất cả các bạn tham gia bữa tiệc của tôi vào thứ Sáu này.",
                "options": ["A. inviting", "B. invite", "C. not invite", "D. to invite"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'would like to do something' (muốn làm gì)."
            },
            {
                "id": 33,
                "question": "Volunteers become well ______ of the problems facing the world.",
                "translation": "Tình nguyện viên trở nên ______ tốt về các vấn đề mà thế giới đang đối mặt.",
                "options": ["A. concerned", "B. interested", "C. aware", "D. helpful"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'aware of' (nhận thức về) là phù hợp nhất."
            },
            {
                "id": 34,
                "question": "They had a global ______ hit with their album concept about 'The dark side of the Moon'.",
                "translation": "Họ đã có một bản hit ______ toàn cầu với khái niệm album về 'Mặt tối của Mặt trăng'.",
                "options": ["A. top", "B. popular", "C. smash", "D. song"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'smash hit' (bản hit lớn) là thành ngữ chỉ sản phẩm rất thành công."
            },
            {
                "id": 35,
                "question": "My parents let my sister ______ camping with her friends in the mountain.",
                "translation": "Bố mẹ tôi để chị tôi ______ cắm trại với bạn bè trên núi.",
                "options": ["A. to go", "B. going", "C. not go", "D. go"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'let someone do something' (để ai làm gì) + V nguyên thể."
            },
            {
                "id": 36,
                "question": "Maria: 'Thanks for the lovely evening.' Diana: '______.'",
                "translation": "Maria: 'Cảm ơn vì buổi tối tuyệt vời.' Diana: '______.'",
                "options": [
                    "A. Oh, that's right", 
                    "B. I'm glad you enjoyed it",
                    "C. Yes, it's really great John", 
                    "D. No, it's not good"
                ],
                "answer": "B",
                "explanation": "Đáp án B đúng vì đây là câu trả lời lịch sự khi ai đó cảm ơn về một bữa tiệc."
            },
            {
                "id": 37,
                "question": "- 'What are you arguing about?' - '______'",
                "translation": "- 'Các bạn đang tranh cãi về cái gì vậy?' - '______'",
                "options": ["A. Well, I think she's right.", "B. That doesn't matter.", "C. Nothing.", "D. Yes, we are"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'Nothing' (Không có gì) là cách trả lời phổ biến khi không muốn nói về cuộc tranh cãi."
            },
            {
                "id": 38,
                "question": "Their massive salaries let them afford to give ______ huge amounts to charities.",
                "translation": "Mức lương khổng lồ của họ cho phép họ có đủ khả năng để ______ số tiền lớn cho các tổ chức từ thiện.",
                "options": ["A. hack", "B. off", "C. away", "D. up"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'give away' (cho đi, tặng) là phù hợp với ngữ cảnh từ thiện."
            },
            {
                "id": 39,
                "question": "I was enjoying my book, but I stopped ______ a program on TV.",
                "translation": "Tôi đang thích thú với cuốn sách của mình, nhưng tôi đã dừng lại ______ một chương trình trên TV.",
                "options": ["A. reading to watch", "B. reading for to watch", "C. to read to watch", "D. to read for watching"],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'stop doing something to do something else' (dừng làm việc này để làm việc khác)."
            },
            {
                "id": 40,
                "question": "It is ______ to work in this city with so much noise and pollution.",
                "translation": "______ để làm việc ở thành phố này với quá nhiều tiếng ồn và ô nhiễm.",
                "options": ["A. health", "B. healthy", "C. healthful", "D. unhealthy"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'unhealthy' (không tốt cho sức khỏe) phù hợp với ngữ cảnh ô nhiễm và tiếng ồn."
            },
            {
                "id": 41,
                "question": "Hoang ______ his email four times a week in order not to miss anything important.",
                "translation": "Hoang ______ email của anh ấy bốn lần một tuần để không bỏ lỡ bất cứ điều gì quan trọng.",
                "options": ["A. is checking", "B. will check", "C. checks", "D. check"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì thì hiện tại đơn 'checks' diễn tả thói quen."
            },
            {
                "id": 42,
                "question": "Van Cao is one of the most well-known ______ in Viet Nam.",
                "translation": "Văn Cao là một trong những ______ nổi tiếng nhất ở Việt Nam.",
                "options": ["A. singers", "B. musicians", "C. authors", "D. actors"],
                "answer": "B",
                "explanation": "Đáp án B đúng vì Văn Cao là nhạc sĩ (musician), không phải ca sĩ."
            },
            {
                "id": 43,
                "question": "These games are challenging, ______ it's not easy to spend little time playing them.",
                "translation": "Những trò chơi này đầy thử thách, ______ không dễ dàng để dành ít thời gian chơi chúng.",
                "options": ["A. so", "B. and", "C. for", "D. or"],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'so' (vì vậy) thể hiện quan hệ nguyên nhân - kết quả."
            },
            {
                "id": 44,
                "question": "Mrs. Huyen is ______ with what her son did.",
                "translation": "Bà Huyền ______ với những gì con trai bà đã làm.",
                "options": ["A. disappointed", "B. disappoint", "C. disappointment", "D. disappointing"],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'disappointed with' (thất vọng với) là tính từ chỉ cảm xúc."
            },
            {
                "id": 45,
                "question": "I am going to have a short rest as I ______ a headache.",
                "translation": "Tôi sẽ nghỉ ngơi một chút vì tôi ______ đau đầu.",
                "options": ["A. feel", "B. have", "C. suffer", "D. take"],
                "answer": "B",
                "explanation": "Đáp án B đúng vì 'have a headache' (bị đau đầu) là cụm từ thông dụng."
            },
            {
                "id": 46,
                "question": "Only the best ______ is recruited.",
                "translation": "Chỉ ______ tốt nhất được tuyển dụng.",
                "options": ["A. employee", "B. application", "C. candidate", "D. CV"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'candidate' (ứng viên) là người được tuyển dụng."
            },
            {
                "id": 47,
                "question": "He was offered the job despite his poor ______.",
                "translation": "Anh ấy được đề nghị công việc mặc dù ______ yếu của anh ấy.",
                "options": ["A. qualifications", "B. achievements", "C. preparations", "D. expressions"],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'qualifications' (trình độ, bằng cấp) phù hợp với ngữ cảnh tuyển dụng."
            },
            {
                "id": 48,
                "question": "The cashiers were asked to watch out ______ forged banknotes.",
                "translation": "Các nhân viên thu ngân được yêu cầu cảnh giác ______ tiền giả.",
                "options": ["A. for", "B. on", "C. to", "D. with"],
                "answer": "A",
                "explanation": "Đáp án A đúng vì 'watch out for something' (cảnh giác với cái gì)."
            },
            {
                "id": 49,
                "question": "A skilled ______ will help candidates feel relaxed.",
                "translation": "Một ______ có kỹ năng sẽ giúp ứng viên cảm thấy thoải mái.",
                "options": ["A. interviewing", "B. interviewee", "C. interviewer", "D. interview"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'interviewer' (người phỏng vấn) là người giúp ứng viên thoải mái."
            },
            {
                "id": 50,
                "question": "He behaved ______ nothing had happened.",
                "translation": "Anh ấy cư xử ______ không có gì đã xảy ra.",
                "options": ["A. if", "B. as if", "C. before", "D. because"],
                "answer": "B",
                "explanation": "Đáp án B đúng vì 'as if' (như thể) diễn tả cách cư xử giả định."
            },
            {
                "id": 51,
                "question": "After working at the same company for thirty years, my grandfather was looking forward to his ______.",
                "translation": "Sau khi làm việc tại cùng một công ty trong ba mươi năm, ông tôi đang mong đợi ______ của mình.",
                "options": ["A. charity", "B. pension", "C. allowance", "D. overtime"],
                "answer": "B",
                "explanation": "Đáp án B đúng vì 'pension' (lương hưu) là phù hợp sau 30 năm làm việc."
            },
            {
                "id": 52,
                "question": "After three years working hard, he was ______.",
                "translation": "Sau ba năm làm việc chăm chỉ, anh ấy đã được ______.",
                "options": ["A. advanced", "B. raised", "C. promoted", "D. elevated"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'promoted' (thăng chức) là phù hợp sau thời gian làm việc chăm chỉ."
            },
            {
                "id": 53,
                "question": "People usually use more ______ language when they're in serious situations like interviews.",
                "translation": "Mọi người thường sử dụng ngôn ngữ ______ hơn khi họ ở trong những tình huống nghiêm túc như phỏng vấn.",
                "options": ["A. serious", "B. solemn", "C. formal", "D. informal"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'formal language' (ngôn ngữ trang trọng) dùng trong phỏng vấn."
            },
            {
                "id": 54,
                "question": "He has all the right ______ for the job.",
                "translation": "Anh ấy có tất cả ______ phù hợp cho công việc.",
                "options": ["A. degrees", "B. certificates", "C. qualifications", "D. diplomas"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'qualifications' (trình độ, năng lực) bao hàm cả bằng cấp và kỹ năng."
            },
            {
                "id": 55,
                "question": "Mary is talking to her mother. - Mary: 'I've made a lot of new friends' - Mary's mother: '______'.",
                "translation": "Mary đang nói chuyện với mẹ cô. - Mary: 'Con đã kết bạn được rất nhiều bạn mới' - Mẹ của Mary: '______'.",
                "options": [
                    "A. You are doing so well, dear.",
                    "B. I can't agree more with yours.",
                    "C. I feel so sorry for you, my girl.",
                    "D. You can never understand, dear."
                ],
                "answer": "A",
                "explanation": "Đáp án A đúng vì đây là lời khen, động viên phù hợp khi con chia sẻ tin tốt."
            },
            {
                "id": 56,
                "question": "The chairman didn't make any ______ upon the matter.",
                "translation": "Chủ tịch không đưa ra bất kỳ ______ nào về vấn đề này.",
                "options": ["A. evaluation", "B. investment", "C. opinion", "D. comment"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'make comment upon' (đưa ra nhận xét về) là cụm từ thông dụng."
            },
            {
                "id": 57,
                "question": "Don't you think you should apply for the job ______ writing?",
                "translation": "Bạn không nghĩ rằng bạn nên nộp đơn xin việc ______ văn bản sao?",
                "options": ["A. at", "B. with", "C. in", "D. for"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'in writing' (bằng văn bản) là thành ngữ."
            },
            {
                "id": 58,
                "question": "Finding a job in this time of economic crisis is becoming ______",
                "translation": "Tìm việc làm trong thời kỳ khủng hoảng kinh tế này đang trở nên ______",
                "options": ["A. as more difficult than", "B. more difficult than", "C. more and more difficult", "D. more than difficult"],
                "answer": "C",
                "explanation": "Đáp án C đúng vì 'more and more difficult' (ngày càng khó khăn hơn) diễn tả sự thay đổi tăng dần."
            },
            {
                "id": 59,
                "question": "Being a flight attendant is a ______ job. You may have to work long hours on long flights and not get enough sleep.",
                "translation": "Làm tiếp viên hàng không là một công việc ______. Bạn có thể phải làm việc nhiều giờ trên các chuyến bay dài và không ngủ đủ.",
                "options": ["A. tedious", "B. rewarding", "C. fascinating", "D. demanding"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'demanding job' (công việc đòi hỏi cao) phù hợp với mô tả làm việc nhiều giờ."
            },
            {
                "id": 60,
                "question": "I studied languages ______ I could work abroad.",
                "translation": "Tôi học ngôn ngữ ______ tôi có thể làm việc ở nước ngoài.",
                "options": ["A. so", "B. as", "C. if", "D. so that"],
                "answer": "D",
                "explanation": "Đáp án D đúng vì 'so that' (để mà) chỉ mục đích."
            }
        ]
    
    def create_mock_tests(self):
        """Tạo 4 đề thi thử, mỗi đề 30 câu trộn từ 4 phần"""
        st.session_state.mock_tests = {}
        
        for test_num in range(1, 5):
            # Tạo đề thi thứ test_num
            mock_test = []
            
            # Lấy ngẫu nhiên từ Part 1: 8 câu
            part1_sample = random.sample(self.part1_questions, 8)
            for q in part1_sample:
                mock_q = q.copy()
                mock_q['part'] = 1
                mock_q['original_id'] = q['id']
                mock_q['id'] = len(mock_test) + 1
                mock_test.append(mock_q)
            
            # Lấy ngẫu nhiên từ Part 2: 6 câu (từ các passage)
            part2_questions = []
            for passage in self.part2_passages.values():
                for q in passage['questions']:
                    q_copy = q.copy()
                    q_copy['part'] = 2
                    q_copy['passage_title'] = passage['title']
                    q_copy['passage_text'] = passage['text']
                    q_copy['passage_translation'] = passage['translation']
                    part2_questions.append(q_copy)
            
            part2_sample = random.sample(part2_questions, 6)
            for q in part2_sample:
                mock_q = q.copy()
                mock_q['id'] = len(mock_test) + 1
                mock_test.append(mock_q)
            
            # Lấy ngẫu nhiên từ Part 3: 6 câu (từ các passage)
            part3_questions = []
            for passage in self.part3_passages:
                for q in passage['questions']:
                    q_copy = q.copy()
                    q_copy['part'] = 3
                    q_copy['passage_text'] = passage['text']
                    q_copy['passage_translation'] = passage['translation']
                    part3_questions.append(q_copy)
            
            part3_sample = random.sample(part3_questions, 6)
            for q in part3_sample:
                mock_q = q.copy()
                mock_q['id'] = len(mock_test) + 1
                mock_test.append(mock_q)
            
            # Lấy ngẫu nhiên từ Part 4: 10 câu
            part4_sample = random.sample(self.part4_questions, 10)
            for q in part4_sample:
                mock_q = q.copy()
                mock_q['part'] = 4
                mock_q['original_id'] = q['id']
                mock_q['id'] = len(mock_test) + 1
                mock_test.append(mock_q)
            
            # Trộn lại các câu hỏi
            random.shuffle(mock_test)
            
            # Đánh lại ID từ 1 đến 30
            for i, q in enumerate(mock_test):
                q['id'] = i + 1
            
            st.session_state.mock_tests[f"test_{test_num}"] = {
                "name": f"Đề thi thử số {test_num}",
                "questions": mock_test,
                "duration": 45 * 60,  # 45 phút
                "total_questions": 30
            }
    
    def display_timer(self, duration, start_time, time_up_key):
        """Hiển thị đồng hồ đếm ngược"""
        if not st.session_state.get(time_up_key, False):
            elapsed_time = datetime.now() - start_time
            elapsed_seconds = elapsed_time.total_seconds()
            remaining_time = max(0, duration - elapsed_seconds)
            
            if remaining_time <= 0:
                st.session_state[time_up_key] = True
                st.warning("⏰ Thời gian làm bài đã hết!")
                st.rerun()
            
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            
            st.markdown(f"""
            <div class="timer">
                ⏰ Thời gian còn lại: {minutes:02d}:{seconds:02d}
            </div>
            """, unsafe_allow_html=True)
            
            # Hiển thị progress bar
            progress = (duration - remaining_time) / duration
            st.progress(progress)
    
    def display_sidebar(self):
        """Hiển thị thanh bên với thông tin và điều khiển"""
        with st.sidebar:
            st.image("https://img.icons8.com/color/96/000000/hospital-3.png", width=80)
            st.title("🏥 Sở Y Tế Gia Lai")
            st.markdown("**Bài Thi Tiếng Anh Bậc 2**")
            st.markdown("**Năm 2025**")
            
            st.markdown("---")
            
            # Chọn chế độ
            st.subheader("🎯 Chọn Chế Độ")
            mode_options = ["Ôn tập theo phần", "Thi thử 45 phút"]
            selected_mode = st.radio(
                "Chế độ học tập:",
                mode_options,
                index=0 if st.session_state.current_mode == "practice" else 1,
                key="mode_selector"
            )
            
            if selected_mode == "Ôn tập theo phần":
                st.session_state.current_mode = "practice"
            else:
                st.session_state.current_mode = "mock_test"
            
            st.markdown("---")
            
            # Thông tin tiến độ
            if st.session_state.current_mode == "practice":
                st.subheader("📊 Tiến Độ Ôn Tập")
                total_questions = 120
                answered = len(st.session_state.answers)
                progress_percent = (answered / total_questions) * 100 if total_questions > 0 else 0
                
                st.metric("Tổng số câu", total_questions)
                st.metric("Đã ôn tập", answered)
                st.metric("Còn lại", total_questions - answered)
                
                st.progress(progress_percent / 100)
                st.caption(f"Tiến độ: {progress_percent:.1f}%")
            
            elif st.session_state.current_mode == "mock_test":
                st.subheader("📊 Thông Tin Thi Thử")
                if st.session_state.mock_test_selected:
                    test_info = st.session_state.mock_tests[st.session_state.mock_test_selected]
                    answered = len(st.session_state.mock_test_answers)
                    total = test_info['total_questions']
                    
                    st.metric("Đề thi", test_info['name'])
                    st.metric("Số câu", total)
                    st.metric("Đã làm", answered)
                    st.metric("Còn lại", total - answered)
                    
                    progress_percent = (answered / total) * 100 if total > 0 else 0
                    st.progress(progress_percent / 100)
                    st.caption(f"Tiến độ: {progress_percent:.1f}%")
            
            st.markdown("---")
            
            # Cài đặt
            st.subheader("⚙️ Cài Đặt")
            st.session_state.show_explanation = st.checkbox(
                "Hiển thị giải thích", 
                value=st.session_state.show_explanation,
                help="Hiển thị giải thích tại sao đáp án đúng/sai"
            )
            
            st.markdown("---")
            
            # Nút điều khiển
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔄 Bắt đầu lại", use_container_width=True):
                    self.reset_all()
            with col2:
                if st.button("🏠 Về trang chủ", use_container_width=True):
                    self.go_to_home()
            
            st.markdown("---")
            
            # Hướng dẫn
            with st.expander("📖 Hướng dẫn sử dụng"):
                if st.session_state.current_mode == "practice":
                    st.markdown("""
                    **Chế độ Ôn tập:**
                    1. Ôn tập theo 4 phần riêng biệt
                    2. Mỗi phần có số lượng câu cố định
                    3. Có thể xem bản dịch và giải thích
                    4. Không giới hạn thời gian
                    """)
                else:
                    st.markdown("""
                    **Chế độ Thi thử:**
                    1. Chọn 1 trong 4 đề thi thử
                    2. Mỗi đề có 30 câu, thời gian 45 phút
                    3. Câu hỏi được trộn từ 4 phần
                    4. Tự động chấm điểm khi hết giờ
                    5. Xem kết quả chi tiết
                    """)
    
    def reset_all(self):
        """Reset toàn bộ bài thi"""
        for key in ['answers', 'mock_test_answers', 'mock_test_selected', 
                   'mock_test_completed', 'practice_completed', 'current_mock_questions']:
            if key in st.session_state:
                del st.session_state[key]
        st.session_state.current_mode = "practice"
        st.rerun()
    
    def go_to_home(self):
        """Quay về trang chủ"""
        st.session_state.mock_test_selected = None
        st.session_state.mock_test_completed = False
        st.session_state.practice_completed = False
        st.rerun()
    
    def display_practice_mode(self):
        """Hiển thị chế độ ôn tập theo phần"""
        if st.session_state.practice_completed:
            self.display_practice_results()
            return
        
        st.markdown('<div class="mode-header">📚 CHẾ ĐỘ ÔN TẬP THEO PHẦN</div>', unsafe_allow_html=True)
        st.info("**Ôn tập toàn bộ 120 câu hỏi theo 4 phần riêng biệt**")
        
        # Tabs cho các phần
        tab1, tab2, tab3, tab4 = st.tabs([
            "📝 PART 1 (20 câu)", 
            "📖 PART 2 (20 câu)", 
            "🔤 PART 3 (20 câu)", 
            "✍️ PART 4 (60 câu)"
        ])
        
        with tab1:
            self.display_part1()
        
        with tab2:
            self.display_part2()
        
        with tab3:
            self.display_part3()
        
        with tab4:
            self.display_part4()
        
        # Nút kết thúc ôn tập
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📊 XEM KẾT QUẢ ÔN TẬP", type="primary", use_container_width=True):
                st.session_state.practice_completed = True
                st.rerun()
    
    def display_part1(self):
        """Hiển thị Part 1: Chọn câu đồng nghĩa"""
        st.markdown('<div class="part-header">📝 PART 1: CHỌN CÂU ĐỒNG NGHĨA</div>', unsafe_allow_html=True)
        st.info("**Hướng dẫn:** Chọn câu có nghĩa tương đương với câu gốc. (20 câu)")
        
        for question in self.part1_questions:
            self.display_question(question, f"part1_{question['id']}")
    
    def display_part2(self):
        """Hiển thị Part 2: Đọc hiểu"""
        st.markdown('<div class="part-header">📖 PART 2: ĐỌC HIỂU</div>', unsafe_allow_html=True)
        st.info("**Hướng dẫn:** Đọc đoạn văn và trả lời câu hỏi. (20 câu)")
        
        for passage_key, passage_data in self.part2_passages.items():
            st.subheader(f"📄 {passage_data['title']}")
            
            # Hiển thị đoạn văn trong expander
            with st.expander("📖 Xem đoạn văn", expanded=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**📌 Tiếng Anh:**")
                    st.write(passage_data['text'])
                with col2:
                    st.markdown("**🇻🇳 Tiếng Việt:**")
                    st.write(passage_data['translation'])
            
            # Hiển thị câu hỏi
            for question in passage_data['questions']:
                self.display_question(question, f"part2_{passage_key}_{question['id']}")
    
    def display_part3(self):
        """Hiển thị Part 3: Điền từ"""
        st.markdown('<div class="part-header">🔤 PART 3: ĐIỀN TỪ</div>', unsafe_allow_html=True)
        st.info("**Hướng dẫn:** Chọn từ thích hợp để điền vào chỗ trống. (20 câu)")
        
        for passage in self.part3_passages:
            # Hiển thị đoạn văn
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**📌 Đoạn văn gốc:**")
                st.write(passage['text'])
            with col2:
                st.markdown("**🇻🇳 Bản dịch:**")
                st.write(passage['translation'])
            
            # Hiển thị câu hỏi
            for question in passage['questions']:
                self.display_question(question, f"part3_{passage['id']}_{question['id']}")
    
    def display_part4(self):
        """Hiển thị Part 4: Hoàn thành câu"""
        st.markdown('<div class="part-header">✍️ PART 4: HOÀN THÀNH CÂU</div>', unsafe_allow_html=True)
        st.info("**Hướng dẫn:** Chọn đáp án đúng để hoàn thành câu. (60 câu)")
        
        # Phân trang để tránh quá tải
        questions_per_page = 10
        total_pages = (len(self.part4_questions) + questions_per_page - 1) // questions_per_page
        
        page = st.selectbox("Chọn trang:", range(1, total_pages + 1), key="part4_page")
        
        start_idx = (page - 1) * questions_per_page
        end_idx = min(start_idx + questions_per_page, len(self.part4_questions))
        
        st.write(f"**Hiển thị câu {start_idx + 1} - {end_idx}**")
        
        for i in range(start_idx, end_idx):
            question = self.part4_questions[i]
            self.display_question(question, f"part4_{question['id']}")
    
    def display_question(self, question, question_key):
        """Hiển thị một câu hỏi và xử lý câu trả lời"""
        
        # Xác định class CSS dựa trên kết quả
        card_class = "question-card"
        if question_key in st.session_state.answers:
            user_answer = st.session_state.answers[question_key]
            if user_answer == question['answer']:
                card_class += " correct-answer"
            else:
                card_class += " wrong-answer"
        
        # Hiển thị câu hỏi trong card
        with st.container():
            st.markdown(f'<div class="{card_class}">', unsafe_allow_html=True)
            
            # Hiển thị câu hỏi
            st.markdown(f"**Câu {question['id']}:** {question['question']}")
            
            # Hiển thị bản dịch (nếu có)
            if 'translation' in question and question['translation']:
                with st.expander("💬 Xem bản dịch"):
                    st.write(question['translation'])
            
            # Hiển thị các lựa chọn
            options = question['options']
            user_answer = st.session_state.answers.get(question_key, "")
            
            # Tạo radio buttons
            selected_option = st.radio(
                f"Chọn đáp án cho câu {question['id']}:",
                options=[''] + ['A', 'B', 'C', 'D'],
                format_func=lambda x: {
                    '': 'Chọn đáp án...',
                    'A': options[0] if len(options) > 0 else 'A',
                    'B': options[1] if len(options) > 1 else 'B', 
                    'C': options[2] if len(options) > 2 else 'C',
                    'D': options[3] if len(options) > 3 else 'D'
                }[x],
                key=f"radio_{question_key}",
                index=0 if user_answer == "" else ['A','B','C','D'].index(user_answer) + 1,
                horizontal=True
            )
            
            # Lưu câu trả lời
            if selected_option != '':
                st.session_state.answers[question_key] = selected_option
            
            # Hiển thị giải thích nếu đã trả lời và có bật chế độ giải thích
            if (question_key in st.session_state.answers and 
                st.session_state.show_explanation and 
                'explanation' in question):
                
                user_answer = st.session_state.answers[question_key]
                correct_answer = question['answer']
                
                if user_answer == correct_answer:
                    st.success(f"✅ **Đúng!** {question['explanation']}")
                else:
                    st.error(f"❌ **Sai!** Đáp án đúng là **{correct_answer}**. {question['explanation']}")
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    def display_mock_test_mode(self):
        """Hiển thị chế độ thi thử"""
        if not st.session_state.mock_test_selected:
            self.display_mock_test_selection()
        elif not st.session_state.mock_test_completed:
            self.display_mock_test()
        else:
            self.display_mock_test_results()
    
    def display_mock_test_selection(self):
        """Hiển thị lựa chọn đề thi thử"""
        st.markdown('<div class="mode-header">🎯 CHẾ ĐỘ THI THỬ 45 PHÚT</div>', unsafe_allow_html=True)
        st.info("**Chọn 1 trong 4 đề thi thử, mỗi đề 30 câu, thời gian 45 phút**")
        
        st.markdown("### 📋 Danh sách đề thi thử:")
        
        cols = st.columns(2)
        for i, (test_key, test_info) in enumerate(st.session_state.mock_tests.items()):
            with cols[i % 2]:
                with st.container():
                    st.markdown(f'<div class="mock-test-card">', unsafe_allow_html=True)
                    st.markdown(f"### {test_info['name']}")
                    st.markdown(f"**Số câu:** {test_info['total_questions']} câu")
                    st.markdown(f"**Thời gian:** 45 phút")
                    st.markdown(f"**Cấu trúc:** Câu hỏi trộn từ 4 phần")
                    
                    if st.button(f"📝 Làm đề này", key=f"start_{test_key}", use_container_width=True):
                        st.session_state.mock_test_selected = test_key
                        st.session_state.mock_test_start_time = datetime.now()
                        st.session_state.current_mock_questions = test_info['questions']
                        st.session_state.mock_test_answers = {}
                        st.session_state.mock_test_completed = False
                        st.session_state.mock_test_time_up = False
                        st.rerun()
                    
                    st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 📊 Thống kê các đề thi:")
        
        # Hiển thị thông tin chi tiết về phân bổ câu hỏi
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Part 1", "8 câu", "Chọn câu đồng nghĩa")
        with col2:
            st.metric("Part 2", "6 câu", "Đọc hiểu")
        with col3:
            st.metric("Part 3", "6 câu", "Điền từ")
        with col4:
            st.metric("Part 4", "10 câu", "Hoàn thành câu")
    
    def display_mock_test(self):
        """Hiển thị đề thi thử"""
        if not st.session_state.mock_test_selected:
            return
        
        test_info = st.session_state.mock_tests[st.session_state.mock_test_selected]
        questions = st.session_state.current_mock_questions
        
        # Hiển thị thông tin đề thi
        st.markdown(f'<div class="mode-header">📝 {test_info["name"].upper()}</div>', unsafe_allow_html=True)
        st.info(f"**Thời gian:** 45 phút • **Số câu:** {test_info['total_questions']} • **Câu hỏi trộn từ 4 phần**")
        
        # Hiển thị đồng hồ đếm ngược
        self.display_timer(
            test_info['duration'], 
            st.session_state.mock_test_start_time,
            'mock_test_time_up'
        )
        
        # Hiển thị các câu hỏi
        for question in questions:
            self.display_mock_question(question)
        
        # Nút nộp bài
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🏁 NỘP BÀI THI", type="primary", use_container_width=True):
                st.session_state.mock_test_completed = True
                st.rerun()
    
    def display_mock_question(self, question):
        """Hiển thị một câu hỏi trong đề thi thử"""
        
        # Xác định class CSS dựa trên kết quả
        card_class = "question-card"
        question_key = f"mock_{question['id']}"
        
        if question_key in st.session_state.mock_test_answers:
            user_answer = st.session_state.mock_test_answers[question_key]
            if user_answer == question['answer']:
                card_class += " correct-answer"
            else:
                card_class += " wrong-answer"
        
        # Hiển thị câu hỏi trong card
        with st.container():
            st.markdown(f'<div class="{card_class}">', unsafe_allow_html=True)
            
            # Hiển thị thông tin phần
            part_label = ""
            if question['part'] == 1:
                part_label = "📝 Part 1: Chọn câu đồng nghĩa"
            elif question['part'] == 2:
                part_label = "📖 Part 2: Đọc hiểu"
            elif question['part'] == 3:
                part_label = "🔤 Part 3: Điền từ"
            else:
                part_label = "✍️ Part 4: Hoàn thành câu"
            
            st.markdown(f"**{part_label}**")
            
            # Hiển thị đoạn văn nếu là Part 2 hoặc 3
            if question['part'] in [2, 3] and 'passage_text' in question:
                with st.expander(f"📖 Xem đoạn văn (Câu {question['id']})"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**📌 Tiếng Anh:**")
                        st.write(question['passage_text'])
                    with col2:
                        st.markdown("**🇻🇳 Tiếng Việt:**")
                        st.write(question.get('passage_translation', ''))
            
            # Hiển thị câu hỏi
            st.markdown(f"**Câu {question['id']}:** {question['question']}")
            
            # Hiển thị bản dịch (nếu có)
            if 'translation' in question and question['translation']:
                with st.expander("💬 Xem bản dịch câu hỏi"):
                    st.write(question['translation'])
            
            # Hiển thị các lựa chọn
            options = question['options']
            user_answer = st.session_state.mock_test_answers.get(question_key, "")
            
            # Tạo radio buttons
            selected_option = st.radio(
                f"Chọn đáp án cho câu {question['id']}:",
                options=[''] + ['A', 'B', 'C', 'D'],
                format_func=lambda x: {
                    '': 'Chọn đáp án...',
                    'A': options[0] if len(options) > 0 else 'A',
                    'B': options[1] if len(options) > 1 else 'B', 
                    'C': options[2] if len(options) > 2 else 'C',
                    'D': options[3] if len(options) > 3 else 'D'
                }[x],
                key=f"mock_radio_{question_key}",
                index=0 if user_answer == "" else ['A','B','C','D'].index(user_answer) + 1,
                horizontal=True
            )
            
            # Lưu câu trả lời
            if selected_option != '':
                st.session_state.mock_test_answers[question_key] = selected_option
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    def display_mock_test_results(self):
        """Hiển thị kết quả đề thi thử"""
        if not st.session_state.mock_test_selected:
            return
        
        test_info = st.session_state.mock_tests[st.session_state.mock_test_selected]
        questions = st.session_state.current_mock_questions
        
        # Tính điểm
        score = 0
        total_questions = len(questions)
        answered_questions = len(st.session_state.mock_test_answers)
        
        for question in questions:
            question_key = f"mock_{question['id']}"
            if question_key in st.session_state.mock_test_answers:
                if st.session_state.mock_test_answers[question_key] == question['answer']:
                    score += 1
        
        percentage = (score / total_questions * 100) if total_questions > 0 else 0
        
        # Tính thời gian làm bài
        if st.session_state.mock_test_start_time:
            time_elapsed = datetime.now() - st.session_state.mock_test_start_time
            minutes = int(time_elapsed.total_seconds() // 60)
            seconds = int(time_elapsed.total_seconds() % 60)
            time_str = f"{minutes:02d}:{seconds:02d}"
        else:
            time_str = "Không xác định"
        
        # Hiển thị kết quả
        st.markdown('<div class="score-card">', unsafe_allow_html=True)
        st.markdown("## 🎊 KẾT QUẢ THI THỬ")
        st.markdown(f"# {score}/{total_questions}")
        st.markdown(f"### {percentage:.1f}%")
        st.markdown(f"**⏰ Thời gian làm bài:** {time_str}")
        
        # Đánh giá
        if answered_questions == 0:
            evaluation = "📝 CHƯA LÀM BÀI"
            color = "gray"
        elif percentage >= 90:
            evaluation = "🎉 XUẤT SẮC"
            color = "green"
        elif percentage >= 80:
            evaluation = "👍 GIỎI" 
            color = "lightgreen"
        elif percentage >= 70:
            evaluation = "💪 KHÁ"
            color = "orange"
        elif percentage >= 60:
            evaluation = "📚 TRUNG BÌNH"
            color = "yellow"
        else:
            evaluation = "🔔 CẦN CỐ GẮNG"
            color = "red"
        
        st.markdown(f'<h3 style="color: {color};">{evaluation}</h3>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Thống kê chi tiết theo phần
        st.subheader("📈 Thống kê chi tiết theo phần")
        
        part_stats = {1: {'correct': 0, 'total': 0, 'name': 'Part 1'},
                      2: {'correct': 0, 'total': 0, 'name': 'Part 2'},
                      3: {'correct': 0, 'total': 0, 'name': 'Part 3'},
                      4: {'correct': 0, 'total': 0, 'name': 'Part 4'}}
        
        for question in questions:
            part = question['part']
            part_stats[part]['total'] += 1
            question_key = f"mock_{question['id']}"
            if question_key in st.session_state.mock_test_answers:
                if st.session_state.mock_test_answers[question_key] == question['answer']:
                    part_stats[part]['correct'] += 1
        
        cols = st.columns(4)
        for i, part_num in enumerate([1, 2, 3, 4]):
            with cols[i]:
                stats = part_stats[part_num]
                part_score = stats['correct']
                part_total = stats['total']
                part_percentage = (part_score / part_total * 100) if part_total > 0 else 0
                st.metric(
                    stats['name'], 
                    f"{part_score}/{part_total}", 
                    f"{part_percentage:.1f}%"
                )
        
        # Hiển thị câu sai
        st.markdown("---")
        st.subheader("📝 Xem lại các câu sai")
        
        wrong_answers = []
        for question in questions:
            question_key = f"mock_{question['id']}"
            if question_key in st.session_state.mock_test_answers:
                user_answer = st.session_state.mock_test_answers[question_key]
                correct_answer = question['answer']
                if user_answer != correct_answer:
                    wrong_answers.append({
                        'question_id': question['id'],
                        'question': question['question'],
                        'user_answer': user_answer,
                        'correct_answer': correct_answer,
                        'explanation': question.get('explanation', ''),
                        'part': question['part']
                    })
        
        if wrong_answers:
            for i, wrong in enumerate(wrong_answers[:10]):
                with st.expander(f"Câu {wrong['question_id']} (Part {wrong['part']}): Đáp án của bạn: {wrong['user_answer']}, Đáp án đúng: {wrong['correct_answer']}"):
                    st.write(f"**Câu hỏi:** {wrong['question']}")
                    st