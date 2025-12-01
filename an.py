import streamlit as st
import random
import pandas as pd

# ========== DỮ LIỆU CÂU HỎI & ĐÁP ÁN (120 câu) ==========
questions_data = {
    "Part 1": {
        1: {
            "question": "You should turn off the lights before going out, Mrs. Hoa said.",
            "question_vi": "Bà Hoa nói: 'Con nên tắt đèn trước khi ra ngoài'.",
            "options": {
                "A": "Mrs. Hoa told to turn off the lights before going out.",
                "A_vi": "Bà Hoa bảo tắt đèn trước khi ra ngoài.",
                "B": "Mrs. Hoa suggested to turn off the lights before going out.",
                "B_vi": "Bà Hoa đề nghị tắt đèn trước khi ra ngoài.",
                "C": "Mrs. Hoa suggested turning off the lights before going out.",
                "C_vi": "Bà Hoa đề nghị tắt đèn trước khi ra ngoài.",
                "D": "Mrs. Hoa asked to us that we should turn off the lights before going out.",
                "D_vi": "Bà Hoa yêu cầu chúng tôi rằng chúng tôi nên tắt đèn trước khi ra ngoài."
            },
            "correct": "C",
            "explanation": "Suggest + V-ing is the correct structure for giving advice.",
            "explanation_vi": "Cấu trúc Suggest + V-ing dùng để đưa ra lời khuyên."
        },
        2: {
            "question": "You won't have a seat unless you book in advance.",
            "question_vi": "Bạn sẽ không có chỗ ngồi trừ khi bạn đặt trước.",
            "options": {
                "A": "You won't have a seat if you don't book in advance.",
                "A_vi": "Bạn sẽ không có chỗ ngồi nếu bạn không đặt trước.",
                "B": "You will have a seat if you don't book in advance.",
                "B_vi": "Bạn sẽ có chỗ ngồi nếu bạn không đặt trước.",
                "C": "You didn't have a seat because you didn't book in advance.",
                "C_vi": "Bạn đã không có chỗ ngồi vì bạn không đặt trước.",
                "D": "You can't have a seat although you book in advance.",
                "D_vi": "Bạn không thể có chỗ ngồi mặc dù bạn đặt trước."
            },
            "correct": "A",
            "explanation": "Unless = if not, so the meaning is the same.",
            "explanation_vi": "Unless có nghĩa là if not, vì vậy nghĩa của hai câu giống nhau."
        },
        3: {
            "question": "This is the first time I've made such a stupid mistake.",
            "question_vi": "Đây là lần đầu tiên tôi mắc một sai lầm ngớ ngẩn như vậy.",
            "options": {
                "A": "I had never made a stupid mistake.",
                "A_vi": "Tôi chưa bao giờ mắc một sai lầm ngớ ngẩn.",
                "B": "I first made a stupid mistake.",
                "B_vi": "Lần đầu tiên tôi mắc một sai lầm ngớ ngẩn.",
                "C": "Never before have I made such a stupid mistake.",
                "C_vi": "Trước đây tôi chưa bao giờ mắc một sai lầm ngớ ngẩn như vậy.",
                "D": "The first mistake I made was a stupid one.",
                "D_vi": "Sai lầm đầu tiên tôi mắc là một sai lầm ngớ ngẩn."
            },
            "correct": "C",
            "explanation": "Never before have I + past participle expresses the same meaning.",
            "explanation_vi": "Never before have I + quá khứ phân từ diễn đạt cùng ý nghĩa."
        },
        4: {
            "question": "He said: 'I bought these books last week'.",
            "question_vi": "Anh ấy nói: 'Tôi đã mua những cuốn sách này tuần trước'.",
            "options": {
                "A": "He said he had bought those books the week before.",
                "A_vi": "Anh ấy nói anh ấy đã mua những cuốn sách đó tuần trước đó.",
                "B": "He said he bought these books last week.",
                "B_vi": "Anh ấy nói anh ấy mua những cuốn sách này tuần trước.",
                "C": "He said he had bought these books last week.",
                "C_vi": "Anh ấy nói anh ấy đã mua những cuốn sách này tuần trước.",
                "D": "He said he bought these books the week before.",
                "D_vi": "Anh ấy nói anh ấy mua những cuốn sách này tuần trước đó."
            },
            "correct": "A",
            "explanation": "In reported speech, tense changes (bought → had bought) and time expression changes (last week → the week before).",
            "explanation_vi": "Trong câu gián tiếp, thì thay đổi (bought → had bought) và cụm từ thời gian thay đổi (last week → the week before)."
        },
        5: {
            "question": "Mark can't wait to use his new computer-games console.",
            "question_vi": "Mark không thể chờ đợi để sử dụng máy chơi game máy tính mới của mình.",
            "options": {
                "A": "Mark is looking forward to using his new computer-games console.",
                "A_vi": "Mark đang mong đợi được sử dụng máy chơi game máy tính mới của mình.",
                "B": "Mark is not used to waiting for his new computer-games console.",
                "B_vi": "Mark không quen với việc chờ đợi máy chơi game máy tính mới của mình.",
                "C": "Mark is patiently waiting to use his new computer-games console.",
                "C_vi": "Mark đang kiên nhẫn chờ đợi để sử dụng máy chơi game máy tính mới của mình.",
                "D": "Mark is eagerly waiting to use his new computer-games console.",
                "D_vi": "Mark đang háo hức chờ đợi để sử dụng máy chơi game máy tính mới của mình."
            },
            "correct": "A",
            "explanation": "Look forward to doing something expresses eagerness similar to can't wait to do something.",
            "explanation_vi": "Look forward to doing something diễn đạt sự háo hức tương tự như can't wait to do something."
        },
        6: {
            "question": "Is it possible for me to come to your house at about 7p.m?",
            "question_vi": "Liệu tôi có thể đến nhà bạn vào khoảng 7 giờ tối được không?",
            "options": {
                "A": "Must I come over to your house at about 7p.m?",
                "A_vi": "Tôi có phải đến nhà bạn vào khoảng 7 giờ tối không?",
                "B": "Can I come to your house at about 7p.m?",
                "B_vi": "Tôi có thể đến nhà bạn vào khoảng 7 giờ tối không?",
                "C": "Could I be come to your house at about 7p.m?",
                "C_vi": "Tôi có thể được đến nhà bạn vào khoảng 7 giờ tối không?",
                "D": "Will I come to your house at about 7p.m?",
                "D_vi": "Tôi sẽ đến nhà bạn vào khoảng 7 giờ tối phải không?"
            },
            "correct": "B",
            "explanation": "Can I is a polite way to ask for permission.",
            "explanation_vi": "Can I là cách lịch sự để xin phép."
        },
        7: {
            "question": "The library stays open until seven o'clock.",
            "question_vi": "Thư viện mở cửa đến 7 giờ.",
            "options": {
                "A": "The library doesn't close until seven o'clock.",
                "A_vi": "Thư viện không đóng cửa cho đến 7 giờ.",
                "B": "Not until seven o'clock does the library open.",
                "B_vi": "Mãi đến 7 giờ thư viện mới mở cửa.",
                "C": "Not until seven o'clock the library doesn't close.",
                "C_vi": "Mãi đến 7 giờ thư viện không đóng cửa.",
                "D": "Not until seven o'clock does the library stay close.",
                "D_vi": "Mãi đến 7 giờ thư viện vẫn đóng cửa."
            },
            "correct": "A",
            "explanation": "Stays open until means the same as doesn't close until.",
            "explanation_vi": "Stays open until có nghĩa giống như doesn't close until."
        },
        8: {
            "question": "Although my father's always busy, he often helps me with my homework.",
            "question_vi": "Mặc dù bố tôi luôn bận rộn, ông ấy thường giúp tôi làm bài tập về nhà.",
            "options": {
                "A": "My father's always busy because he often helps me with my homework.",
                "A_vi": "Bố tôi luôn bận rộn vì ông ấy thường giúp tôi làm bài tập về nhà.",
                "B": "My father's always busy, and he often helps me with my homework.",
                "B_vi": "Bố tôi luôn bận rộn, và ông ấy thường giúp tôi làm bài tập về nhà.",
                "C": "My father's always busy, so he often helps me with my homework.",
                "C_vi": "Bố tôi luôn bận rộn, vì vậy ông ấy thường giúp tôi làm bài tập về nhà.",
                "D": "My father's always busy, but he often helps me with my homework.",
                "D_vi": "Bố tôi luôn bận rộn, nhưng ông ấy thường giúp tôi làm bài tập về nhà."
            },
            "correct": "D",
            "explanation": "Although shows contrast, which can be replaced by but.",
            "explanation_vi": "Although thể hiện sự tương phản, có thể thay thế bằng but."
        },
        9: {
            "question": "We started cooking for the party four hours ago.",
            "question_vi": "Chúng tôi bắt đầu nấu ăn cho bữa tiệc từ bốn giờ trước.",
            "options": {
                "A": "We began to cook for the party for four hours.",
                "A_vi": "Chúng tôi bắt đầu nấu ăn cho bữa tiệc trong bốn giờ.",
                "B": "We have been cooked for the party for four hours.",
                "B_vi": "Chúng tôi đã được nấu ăn cho bữa tiệc trong bốn giờ.",
                "C": "We have been cooking for the party for four hours.",
                "C_vi": "Chúng tôi đã nấu ăn cho bữa tiệc được bốn giờ rồi.",
                "D": "We cooked for the party four hours ago.",
                "D_vi": "Chúng tôi đã nấu ăn cho bữa tiệc bốn giờ trước."
            },
            "correct": "C",
            "explanation": "The present perfect continuous tense indicates an action that started in the past and is still continuing.",
            "explanation_vi": "Thì hiện tại hoàn thành tiếp diễn chỉ hành động bắt đầu trong quá khứ và vẫn đang tiếp diễn."
        },
        10: {
            "question": "No one in the team can play better than John.",
            "question_vi": "Không ai trong đội có thể chơi tốt hơn John.",
            "options": {
                "A": "John as well as other players of the team plays very well.",
                "A_vi": "John cũng như các cầu thủ khác trong đội chơi rất tốt.",
                "B": "John plays well but the others play better.",
                "B_vi": "John chơi tốt nhưng những người khác chơi tốt hơn.",
                "C": "John is the best player of the team.",
                "C_vi": "John là cầu thủ giỏi nhất trong đội.",
                "D": "Everyone in the team, but John, plays very well.",
                "D_vi": "Mọi người trong đội, trừ John, đều chơi rất tốt."
            },
            "correct": "C",
            "explanation": "No one can play better than John means John is the best player.",
            "explanation_vi": "Không ai có thể chơi tốt hơn John có nghĩa John là cầu thủ giỏi nhất."
        },
        11: {
            "question": "Sorry, I took you someone else.",
            "question_vi": "Xin lỗi, tôi đã nhầm bạn với người khác.",
            "options": {
                "A": "Sorry, I thought you were somebody else.",
                "A_vi": "Xin lỗi, tôi đã nghĩ bạn là người khác.",
                "B": "Sorry, I made a mistake in taking you to someone else.",
                "B_vi": "Xin lỗi, tôi đã phạm sai lầm khi đưa bạn đến với người khác.",
                "C": "Sorry, I took you instead of somebody else.",
                "C_vi": "Xin lỗi, tôi đã lấy bạn thay vì người khác.",
                "D": "Sorry, I asked somebody to take you.",
                "D_vi": "Xin lỗi, tôi đã nhờ ai đó đưa bạn đi."
            },
            "correct": "A",
            "explanation": "Took you for someone else means mistook you for someone else.",
            "explanation_vi": "Took you for someone else có nghĩa là nhầm bạn với người khác."
        },
        12: {
            "question": "Many think that Steve stole the money.",
            "question_vi": "Nhiều người nghĩ rằng Steve đã ăn cắp tiền.",
            "options": {
                "A": "Steve is thought to have stolen the money.",
                "A_vi": "Steve được cho là đã ăn cắp tiền.",
                "B": "The money is thought to be stolen by Steve.",
                "B_vi": "Số tiền được cho là bị Steve ăn cắp.",
                "C": "It was not Steve who stole the money.",
                "C_vi": "Không phải Steve đã ăn cắp tiền.",
                "D": "Many people think the money is stolen by Steve.",
                "D_vi": "Nhiều người nghĩ rằng tiền bị Steve ăn cắp."
            },
            "correct": "A",
            "explanation": "Passive voice with infinitive perfect (to have stolen) for past action.",
            "explanation_vi": "Câu bị động với động từ nguyên thể hoàn thành (to have stolen) cho hành động trong quá khứ."
        },
        13: {
            "question": "I spent a long time getting over the disappointment of losing the match.",
            "question_vi": "Tôi đã mất nhiều thời gian để vượt qua sự thất vọng vì thua trận đấu.",
            "options": {
                "A": "It took me long to forget the disappointment of losing the match.",
                "A_vi": "Tôi đã mất nhiều thời gian để quên đi sự thất vọng vì thua trận đấu.",
                "B": "It took me long to stop disappointing you.",
                "B_vi": "Tôi đã mất nhiều thời gian để ngừng làm bạn thất vọng.",
                "C": "Getting over the disappointment took me a long time than the match.",
                "C_vi": "Vượt qua sự thất vọng tốn nhiều thời gian hơn trận đấu.",
                "D": "Losing the match disappointed me too much.",
                "D_vi": "Thua trận đấu đã làm tôi quá thất vọng."
            },
            "correct": "A",
            "explanation": "Spent a long time getting over means it took a long time to forget.",
            "explanation_vi": "Spent a long time getting over có nghĩa là mất nhiều thời gian để quên đi."
        },
        14: {
            "question": "His eel soup is better than any other soups I have ever eaten.",
            "question_vi": "Súp lươn của anh ấy ngon hơn bất kỳ món súp nào khác mà tôi từng ăn.",
            "options": {
                "A": "Of all the soups I have ever eaten, his eel soup is the best.",
                "A_vi": "Trong tất cả các món súp tôi từng ăn, súp lươn của anh ấy là ngon nhất.",
                "B": "I have ever eaten many soups that are better than his eel soup.",
                "B_vi": "Tôi đã từng ăn nhiều món súp ngon hơn súp lươn của anh ấy.",
                "C": "His eel soup is good but I have ever eaten many others better.",
                "C_vi": "Súp lươn của anh ấy ngon nhưng tôi đã từng ăn nhiều món khác ngon hơn.",
                "D": "His eel soup is the worst of all soups I have eaten.",
                "D_vi": "Súp lươn của anh ấy là tệ nhất trong tất cả các món súp tôi từng ăn."
            },
            "correct": "A",
            "explanation": "Better than any other means the best among all.",
            "explanation_vi": "Better than any other có nghĩa là tốt nhất trong tất cả."
        },
        15: {
            "question": "I haven't visited my hometown for a few years.",
            "question_vi": "Tôi đã không về thăm quê hương được vài năm rồi.",
            "options": {
                "A": "I last visited my hometown a few years ago.",
                "A_vi": "Lần cuối tôi về thăm quê hương là vài năm trước.",
                "B": "I was in my hometown for a few years.",
                "B_vi": "Tôi đã ở quê hương trong vài năm.",
                "C": "I didn't visit my hometown a few years ago.",
                "C_vi": "Tôi đã không về thăm quê hương vài năm trước.",
                "D": "I have been in my hometown for a few years.",
                "D_vi": "Tôi đã ở quê hương được vài năm rồi."
            },
            "correct": "A",
            "explanation": "Haven't visited for a few years means the last visit was a few years ago.",
            "explanation_vi": "Haven't visited for a few years có nghĩa là lần về thăm cuối cùng là vài năm trước."
        },
        16: {
            "question": "He couldn't stand being eliminated from the contest.",
            "question_vi": "Anh ấy không thể chịu đựng được việc bị loại khỏi cuộc thi.",
            "options": {
                "A": "He didn't believe that he was thrown out from the contest.",
                "A_vi": "Anh ấy không tin rằng mình bị đuổi khỏi cuộc thi.",
                "B": "Because he stood, he was eliminated from the contest.",
                "B_vi": "Bởi vì anh ấy đứng, anh ấy bị loại khỏi cuộc thi.",
                "C": "He was eliminated from the contest because he was unable to stand.",
                "C_vi": "Anh ấy bị loại khỏi cuộc thi vì không thể đứng được.",
                "D": "He was unable to accept the failure in the contest.",
                "D_vi": "Anh ấy không thể chấp nhận thất bại trong cuộc thi."
            },
            "correct": "D",
            "explanation": "Couldn't stand means couldn't accept or tolerate.",
            "explanation_vi": "Couldn't stand có nghĩa là không thể chấp nhận hoặc chịu đựng."
        },
        17: {
            "question": "He sang very badly. Everyone left the room.",
            "question_vi": "Anh ấy hát rất tệ. Mọi người rời khỏi phòng.",
            "options": {
                "A": "He sang so badly but everyone left the room.",
                "A_vi": "Anh ấy hát rất tệ nhưng mọi người rời khỏi phòng.",
                "B": "He sang badly as a result of everyone leaving the room.",
                "B_vi": "Anh ấy hát tệ do kết quả của việc mọi người rời khỏi phòng.",
                "C": "He sang very badly, so everyone left the room.",
                "C_vi": "Anh ấy hát rất tệ, vì vậy mọi người rời khỏi phòng.",
                "D": "Everyone left the room, so he sang badly.",
                "D_vi": "Mọi người rời khỏi phòng, vì vậy anh ấy hát tệ."
            },
            "correct": "C",
            "explanation": "The first sentence is the cause, the second is the result.",
            "explanation_vi": "Câu đầu là nguyên nhân, câu sau là kết quả."
        },
        18: {
            "question": "Your birthday party was the last time I really enjoyed myself.",
            "question_vi": "Bữa tiệc sinh nhật của bạn là lần cuối cùng tôi thực sự vui vẻ.",
            "options": {
                "A": "Your last birthday party wasn't really enjoyed to me.",
                "A_vi": "Bữa tiệc sinh nhật cuối cùng của bạn không thực sự làm tôi vui.",
                "B": "I didn't really enjoy myself at your birthday party.",
                "B_vi": "Tôi không thực sự vui vẻ tại bữa tiệc sinh nhật của bạn.",
                "C": "I haven't really enjoyed myself since your birthday party.",
                "C_vi": "Tôi đã không thực sự vui vẻ kể từ bữa tiệc sinh nhật của bạn.",
                "D": "I haven't been to your birthday party lastly as I really enjoyed myself.",
                "D_vi": "Tôi đã không đến bữa tiệc sinh nhật của bạn gần đây vì tôi thực sự vui vẻ."
            },
            "correct": "C",
            "explanation": "The last time I enjoyed myself means I haven't enjoyed myself since then.",
            "explanation_vi": "Lần cuối cùng tôi vui vẻ có nghĩa là tôi đã không vui vẻ kể từ đó."
        },
        19: {
            "question": "I came back to my town last Sunday, said Mr. Pitt.",
            "question_vi": "Ông Pitt nói: 'Tôi đã trở lại thị trấn của tôi vào Chủ nhật tuần trước'.",
            "options": {
                "A": "Mr. Pitt said that I had come back to his town the Sunday before.",
                "A_vi": "Ông Pitt nói rằng tôi đã trở lại thị trấn của ông ấy vào Chủ nhật trước đó.",
                "B": "Mr. Pitt said that he came back to his town the Sunday before.",
                "B_vi": "Ông Pitt nói rằng ông ấy trở lại thị trấn của mình vào Chủ nhật trước đó.",
                "C": "Mr. Pitt said that I had come back to his town last Sunday.",
                "C_vi": "Ông Pitt nói rằng tôi đã trở lại thị trấn của ông ấy vào Chủ nhật tuần trước.",
                "D": "Mr. Pitt said that he had come back to his town the Sunday before.",
                "D_vi": "Ông Pitt nói rằng ông ấy đã trở lại thị trấn của mình vào Chủ nhật trước đó."
            },
            "correct": "D",
            "explanation": "Reported speech: tense change (came → had come) and time change (last Sunday → the Sunday before).",
            "explanation_vi": "Câu gián tiếp: thay đổi thì (came → had come) và thay đổi thời gian (last Sunday → the Sunday before)."
        },
        20: {
            "question": "Nick is lazy, so he is punished.",
            "question_vi": "Nick lười biếng, vì vậy anh ấy bị phạt.",
            "options": {
                "A": "Nick would not be punished if he were not lazy.",
                "A_vi": "Nick sẽ không bị phạt nếu anh ấy không lười.",
                "B": "If Nick is not lazy, he would not be punished.",
                "B_vi": "Nếu Nick không lười, anh ấy sẽ không bị phạt.",
                "C": "If Nick were lazy, he would be punished.",
                "C_vi": "Nếu Nick lười, anh ấy sẽ bị phạt.",
                "D": "If Nick were not lazy, he would be punished.",
                "D_vi": "Nếu Nick không lười, anh ấy sẽ bị phạt."
            },
            "correct": "A",
            "explanation": "Second conditional for unreal present situation.",
            "explanation_vi": "Câu điều kiện loại 2 cho tình huống không có thật ở hiện tại."
        }
    },
    "Part 2": {
        1: {
            "question": "The passage is mainly about ______",
            "question_vi": "Đoạn văn chủ yếu nói về ______",
            "options": {
                "A": "the Beatles' fame and success",
                "A_vi": "sự nổi tiếng và thành công của the Beatles",
                "B": "how the Beatles became more successful than other groups",
                "B_vi": "cách the Beatles trở nên thành công hơn các nhóm khác",
                "C": "why the Beatles split up after 7 years",
                "C_vi": "tại sao the Beatles tan rã sau 7 năm",
                "D": "many people's ability to sing a Beatles song",
                "D_vi": "khả năng hát một bài hát của the Beatles của nhiều người"
            },
            "correct": "A",
            "explanation": "The passage focuses on the Beatles' rise to fame, their impact on pop music, and their enduring legacy.",
            "explanation_vi": "Đoạn văn tập trung vào sự nổi tiếng của the Beatles, ảnh hưởng của họ đến nhạc pop và di sản bền vững của họ."
        },
        2: {
            "question": "The word 'sensational' is closest in meaning to ______",
            "question_vi": "Từ 'sensational' gần nghĩa nhất với ______",
            "options": {
                "A": "shocking",
                "A_vi": "gây sốc",
                "B": "bad",
                "B_vi": "tồi tệ",
                "C": "notorious",
                "C_vi": "khét tiếng",
                "D": "popular",
                "D_vi": "nổi tiếng, phổ biến"
            },
            "correct": "D",
            "explanation": "In this context, 'sensational' means causing great public interest and excitement.",
            "explanation_vi": "Trong ngữ cảnh này, 'sensational' có nghĩa là gây ra sự quan tâm và phấn khích lớn của công chúng."
        },
        3: {
            "question": "What is NOT TRUE about the Beatles?",
            "question_vi": "Điều nào KHÔNG ĐÚNG về the Beatles?",
            "options": {
                "A": "They had a long stable career.",
                "A_vi": "Họ có một sự nghiệp dài ổn định.",
                "B": "The members had no training in music.",
                "B_vi": "Các thành viên không được đào tạo về âm nhạc.",
                "C": "They became famous when they wrote their own songs.",
                "C_vi": "Họ trở nên nổi tiếng khi viết bài hát của riêng mình.",
                "D": "They changed pop music.",
                "D_vi": "Họ đã thay đổi nhạc pop."
            },
            "correct": "A",
            "explanation": "The passage states that the Beatles did not have a long career (1963-1970).",
            "explanation_vi": "Đoạn văn nói rằng the Beatles không có sự nghiệp dài (1963-1970)."
        },
        4: {
            "question": "The Beatles stopped their live performances because ______",
            "question_vi": "The Beatles ngừng biểu diễn trực tiếp vì ______",
            "options": {
                "A": "They were afraid of being hurt by fans.",
                "A_vi": "Họ sợ bị người hâm mộ làm tổn thương.",
                "B": "They did not want to work with each other.",
                "B_vi": "Họ không muốn làm việc với nhau.",
                "C": "They spent more time writing their own songs.",
                "C_vi": "Họ dành nhiều thời gian hơn để viết bài hát của riêng mình.",
                "D": "They had earned enough money.",
                "D_vi": "Họ đã kiếm đủ tiền."
            },
            "correct": "A",
            "explanation": "The text says it became too dangerous due to overexcited fans.",
            "explanation_vi": "Bài đọc nói rằng việc biểu diễn trở nên quá nguy hiểm do người hâm mộ quá khích."
        },
        5: {
            "question": "The tone of the passage is that of ______",
            "question_vi": "Giọng điệu của đoạn văn là ______",
            "options": {
                "A": "neutral",
                "A_vi": "trung lập",
                "B": "criticism",
                "B_vi": "chỉ trích",
                "C": "admiration",
                "C_vi": "ngưỡng mộ",
                "D": "pleasant",
                "D_vi": "dễ chịu"
            },
            "correct": "C",
            "explanation": "The author admires the Beatles' achievements and impact.",
            "explanation_vi": "Tác giả ngưỡng mộ những thành tựu và ảnh hưởng của the Beatles."
        },
        6: {
            "question": "What is the writer's main purpose in writing the passage?",
            "question_vi": "Mục đích chính của tác giả khi viết đoạn văn là gì?",
            "options": {
                "A": "To describe a dangerous trip.",
                "A_vi": "Mô tả một chuyến đi nguy hiểm.",
                "B": "To explain how sight can be lost.",
                "B_vi": "Giải thích cách thị lực có thể bị mất.",
                "C": "To warn against playing with sticks.",
                "C_vi": "Cảnh báo không chơi với gậy.",
                "D": "To report a patient's cure.",
                "D_vi": "Báo cáo về việc chữa trị cho một bệnh nhân."
            },
            "correct": "D",
            "explanation": "The passage tells the story of Eukhtuul's successful eye operation.",
            "explanation_vi": "Đoạn văn kể câu chuyện về ca phẫu thuật mắt thành công của Eukhtuul."
        },
        7: {
            "question": "After meeting Eukhtuul, Samantha felt ______.",
            "question_vi": "Sau khi gặp Eukhtuul, Samantha cảm thấy ______.",
            "options": {
                "A": "surprised by Eukhtuul's courage",
                "A_vi": "ngạc nhiên bởi sự dũng cảm của Eukhtuul",
                "B": "grateful for her own sight",
                "B_vi": "biết ơn vì thị lực của chính mình",
                "C": "proud of the doctor's skill",
                "C_vi": "tự hào về kỹ năng của bác sĩ",
                "D": "angry about Eukhtuul's experience",
                "D_vi": "tức giận về trải nghiệm của Eukhtuul"
            },
            "correct": "B",
            "explanation": "Samantha realized how lucky she was to have her sight.",
            "explanation_vi": "Samantha nhận ra cô ấy may mắn thế nào khi có thị lực."
        },
        8: {
            "question": "What is the result of Eukhtuul's operation?",
            "question_vi": "Kết quả của ca phẫu thuật của Eukhtuul là gì?",
            "options": {
                "A": "She can see better but won't have normal eyes.",
                "A_vi": "Cô ấy có thể nhìn tốt hơn nhưng sẽ không có đôi mắt bình thường.",
                "B": "She will need another operation.",
                "B_vi": "Cô ấy sẽ cần một ca phẫu thuật khác.",
                "C": "She can already see perfectly again.",
                "C_vi": "Cô ấy đã có thể nhìn thấy hoàn hảo trở lại.",
                "D": "After some time she will see as well as before.",
                "D_vi": "Sau một thời gian cô ấy sẽ nhìn thấy tốt như trước đây."
            },
            "correct": "D",
            "explanation": "The doctor said 'In six months, your sight will back to normal'.",
            "explanation_vi": "Bác sĩ nói 'Sau 6 tháng, thị lực của em sẽ trở lại bình thường'."
        },
        9: {
            "question": "Which of the postcard Samantha wrote to an English friend?",
            "question_vi": "Samantha đã viết tấm bưu thiếp nào cho một người bạn Anh?",
            "options": {
                "A": "Make sure you take care of your eyes because they're more valuable than you realize.",
                "A_vi": "Hãy chắc chắn rằng bạn chăm sóc đôi mắt của mình vì chúng quý giá hơn bạn nhận ra.",
                "B": "I'm staying with my friend Eukhtuul while I'm sightseeing in Mongolia.",
                "B_vi": "Tôi đang ở với bạn tôi Eukhtuul trong khi tôi đi tham quan ở Mông Cổ.",
                "C": "You may have to fly a long way to have an operation you need, but the journey will be worth it.",
                "C_vi": "Bạn có thể phải bay một chặng đường dài để có ca phẫu thuật bạn cần, nhưng chuyến đi sẽ đáng giá.",
                "D": "I have visited a Mongolia and watched local doctors do an operation.",
                "D_vi": "Tôi đã đến thăm Mông Cổ và xem các bác sĩ địa phương thực hiện một ca phẫu thuật."
            },
            "correct": "A",
            "explanation": "The passage emphasizes the value of sight.",
            "explanation_vi": "Đoạn văn nhấn mạnh giá trị của thị lực."
        },
        10: {
            "question": "What can a reader learn about in this passage?",
            "question_vi": "Người đọc có thể tìm hiểu về điều gì trong đoạn văn này?",
            "options": {
                "A": "The best way of studying medicine.",
                "A_vi": "Cách tốt nhất để học y khoa.",
                "B": "The international work of some eye doctors.",
                "B_vi": "Công việc quốc tế của một số bác sĩ mắt.",
                "C": "The difficulties of blind travelers.",
                "C_vi": "Những khó khăn của du khách khiếm thị.",
                "D": "The life of schoolchildren in Mongolia.",
                "D_vi": "Cuộc sống của học sinh ở Mông Cổ."
            },
            "correct": "B",
            "explanation": "The passage describes Orbis, an organization that helps blind people worldwide.",
            "explanation_vi": "Đoạn văn mô tả Orbis, một tổ chức giúp đỡ người mù trên toàn thế giới."
        },
        11: {
            "question": "According to the passage, the information doctors give us ______.",
            "question_vi": "Theo đoạn văn, thông tin bác sĩ cung cấp cho chúng ta ______.",
            "options": {
                "A": "is mostly forgotten",
                "A_vi": "hầu hết bị quên",
                "B": "is only 80% correct",
                "B_vi": "chỉ đúng 80%",
                "C": "is about 50% wrong",
                "C_vi": "khoảng 50% sai",
                "D": "is usually not enough",
                "D_vi": "thường không đủ"
            },
            "correct": "A",
            "explanation": "The passage says we forget about 80% of medical information.",
            "explanation_vi": "Đoạn văn nói chúng ta quên khoảng 80% thông tin y tế."
        },
        12: {
            "question": "The word 'complicated' in the passage is opposite in meaning to ______.",
            "question_vi": "Từ 'complicated' trong đoạn văn trái nghĩa với ______.",
            "options": {
                "A": "good",
                "A_vi": "tốt",
                "B": "quick",
                "B_vi": "nhanh",
                "C": "short",
                "C_vi": "ngắn",
                "D": "simple",
                "D_vi": "đơn giản"
            },
            "correct": "D",
            "explanation": "Complicated means complex, so simple is the opposite.",
            "explanation_vi": "Complicated có nghĩa là phức tạp, vì vậy simple là trái nghĩa."
        },
        13: {
            "question": "The author says that when people consult a doctor, ______.",
            "question_vi": "Tác giả nói rằng khi người ta tham khảo ý kiến bác sĩ, ______.",
            "options": {
                "A": "they usually have a family member with them",
                "A_vi": "họ thường có một thành viên gia đình đi cùng",
                "B": "they are interested in knowing what they should do",
                "B_vi": "họ quan tâm đến việc biết họ nên làm gì",
                "C": "they always believe that their situation is serious",
                "C_vi": "họ luôn tin rằng tình huống của họ nghiêm trọng",
                "D": "they only want to know what is wrong with them",
                "D_vi": "họ chỉ muốn biết điều gì sai với họ"
            },
            "correct": "D",
            "explanation": "People focus on diagnosis rather than treatment when anxious.",
            "explanation_vi": "Mọi người tập trung vào chẩn đoán hơn là điều trị khi lo lắng."
        },
        14: {
            "question": "The word 'absorb' in the passage is closest in meaning to ______.",
            "question_vi": "Từ 'absorb' trong đoạn văn gần nghĩa nhất với ______.",
            "options": {
                "A": "take in",
                "A_vi": "tiếp thu",
                "B": "inhale",
                "B_vi": "hít vào",
                "C": "swallow",
                "C_vi": "nuốt",
                "D": "digest",
                "D_vi": "tiêu hóa"
            },
            "correct": "A",
            "explanation": "Absorb in this context means to take in or understand information.",
            "explanation_vi": "Absorb trong ngữ cảnh này có nghĩa là tiếp thu hoặc hiểu thông tin."
        },
        15: {
            "question": "The author suggests recording the consultant in order to ______.",
            "question_vi": "Tác giả đề nghị ghi âm buổi tư vấn để ______.",
            "options": {
                "A": "refer to it later to better understand your condition",
                "A_vi": "tham khảo sau này để hiểu rõ hơn về tình trạng của bạn",
                "B": "play it to your family members to get their opinions",
                "B_vi": "phát cho các thành viên gia đình để nhận ý kiến của họ",
                "C": "replay it to write down any important information",
                "C_vi": "phát lại để ghi chép bất kỳ thông tin quan trọng nào",
                "D": "use it as evidence against your doctor if necessary",
                "D_vi": "sử dụng nó làm bằng chứng chống lại bác sĩ nếu cần"
            },
            "correct": "A",
            "explanation": "Recording helps you understand the advice better at home.",
            "explanation_vi": "Ghi âm giúp bạn hiểu lời khuyên tốt hơn ở nhà."
        },
        16: {
            "question": "Which two main organizational schemes can be identified in this passage?",
            "question_vi": "Hai sơ đồ tổ chức chính nào có thể được xác định trong đoạn văn này?",
            "options": {
                "A": "order by topic and cause and effect",
                "A_vi": "theo chủ đề và nguyên nhân - kết quả",
                "B": "hierarchical order and order by topic",
                "B_vi": "thứ bậc và theo chủ đề",
                "C": "hierarchical order and chronological order",
                "C_vi": "thứ bậc và theo thời gian",
                "D": "chronological order and compare and contrast",
                "D_vi": "theo thời gian và so sánh - đối chiếu"
            },
            "correct": "A",
            "explanation": "The passage discusses different topics (energy audits, appliances, windows) and cause-effect relationships.",
            "explanation_vi": "Đoạn văn thảo luận các chủ đề khác nhau (kiểm toán năng lượng, thiết bị, cửa sổ) và mối quan hệ nguyên nhân - kết quả."
        },
        17: {
            "question": "Which of the following ideas is NOT included in this passage?",
            "question_vi": "Ý tưởng nào sau đây KHÔNG được bao gồm trong đoạn văn này?",
            "options": {
                "A": "Your local energy company will send an energy auditor at your request.",
                "A_vi": "Công ty năng lượng địa phương của bạn sẽ gửi một kiểm toán viên năng lượng theo yêu cầu của bạn.",
                "B": "Double-paned windows can cut energy costs.",
                "B_vi": "Cửa sổ hai lớp có thể cắt giảm chi phí năng lượng.",
                "C": "You can reduce your $130 monthly lighting costs to $65 by using fluorescent bulbs instead of incandescent.",
                "C_vi": "Bạn có thể giảm chi phí chiếu sáng hàng tháng $130 xuống $65 bằng cách sử dụng bóng đèn huỳnh quang thay vì bóng đèn sợi đốt.",
                "D": "Some appliances have energy-saving settings.",
                "D_vi": "Một số thiết bị có cài đặt tiết kiệm năng lượng."
            },
            "correct": "C",
            "explanation": "The passage mentions saving 50% on lighting costs but doesn't give specific dollar amounts.",
            "explanation_vi": "Đoạn văn đề cập đến việc tiết kiệm 50% chi phí chiếu sáng nhưng không đưa ra số tiền cụ thể."
        },
        18: {
            "question": "Which of the following best expresses the main idea of this passage?",
            "question_vi": "Câu nào sau đây diễn đạt tốt nhất ý chính của đoạn văn?",
            "options": {
                "A": "There are many things a homeowner or renter can do to save energy and money.",
                "A_vi": "Có nhiều điều chủ nhà hoặc người thuê có thể làm để tiết kiệm năng lượng và tiền bạc.",
                "B": "Hiring an energy auditor will save energy and money.",
                "B_vi": "Thuê một kiểm toán viên năng lượng sẽ tiết kiệm năng lượng và tiền bạc.",
                "C": "Homeowners and renters don't know what they can do to save energy and money.",
                "C_vi": "Chủ nhà và người thuê không biết họ có thể làm gì để tiết kiệm năng lượng và tiền bạc.",
                "D": "Replacing windows and light bulbs are well worth the effort and cost.",
                "D_vi": "Thay thế cửa sổ và bóng đèn rất đáng công sức và chi phí."
            },
            "correct": "A",
            "explanation": "The main idea is that there are various ways to save energy and money at home.",
            "explanation_vi": "Ý chính là có nhiều cách khác nhau để tiết kiệm năng lượng và tiền bạc tại nhà."
        },
        19: {
            "question": "According to the passage, which of the following would an energy auditor NOT do?",
            "question_vi": "Theo đoạn văn, kiểm toán viên năng lượng sẽ KHÔNG làm điều nào sau đây?",
            "options": {
                "A": "Locate a variety of flaws that may result in energy inefficiency and fix them.",
                "A_vi": "Xác định các lỗi khác nhau có thể dẫn đến kém hiệu quả năng lượng và sửa chúng.",
                "B": "Look for problems with heat distribution.",
                "B_vi": "Tìm kiếm các vấn đề với phân phối nhiệt.",
                "C": "Offer solutions to lower your energy costs.",
                "C_vi": "Đề xuất giải pháp để giảm chi phí năng lượng của bạn.",
                "D": "Check for construction flaws.",
                "D_vi": "Kiểm tra các lỗi xây dựng."
            },
            "correct": "A",
            "explanation": "Auditors identify problems but don't fix them; they offer solutions.",
            "explanation_vi": "Kiểm toán viên xác định vấn đề nhưng không sửa chúng; họ đề xuất giải pháp."
        },
        20: {
            "question": "According the passage, double-paned windows",
            "question_vi": "Theo đoạn văn, cửa sổ hai lớp",
            "options": {
                "A": "are energy efficient.",
                "A_vi": "tiết kiệm năng lượng.",
                "B": "should only be used as replacement windows.",
                "B_vi": "chỉ nên được sử dụng như cửa sổ thay thế.",
                "C": "should only be used in new additions to homes.",
                "C_vi": "chỉ nên được sử dụng trong các phần mới của nhà.",
                "D": "will lower your heating costs by 50%.",
                "D_vi": "sẽ giảm chi phí sưởi ấm của bạn 50%."
            },
            "correct": "A",
            "explanation": "Double-paned windows are mentioned as energy-efficient.",
            "explanation_vi": "Cửa sổ hai lớp được đề cập là tiết kiệm năng lượng."
        }
    },
    "Part 3": {
        1: {
            "question": "Society has changed in many ways (1)____ the introduction of computers, and people's lives at home and at the office have been affected.",
            "question_vi": "Xã hội đã thay đổi theo nhiều cách (1)____ việc giới thiệu máy tính, và cuộc sống của mọi người ở nhà và tại văn phòng đã bị ảnh hưởng.",
            "options": {
                "A": "for",
                "A_vi": "cho",
                "B": "from",
                "B_vi": "từ",
                "C": "at",
                "C_vi": "ở tại",
                "D": "since",
                "D_vi": "kể từ"
            },
            "correct": "D",
            "explanation": "Since indicates a point in time when the change started.",
            "explanation_vi": "Since chỉ một mốc thời gian khi sự thay đổi bắt đầu."
        },
        2: {
            "question": "Most people are working for fewer hours per week than they (2)____ to",
            "question_vi": "Hầu hết mọi người đang làm việc ít giờ mỗi tuần hơn họ (2)____",
            "options": {
                "A": "want",
                "A_vi": "muốn",
                "B": "used",
                "B_vi": "đã từng",
                "C": "ought",
                "C_vi": "nên",
                "D": "have",
                "D_vi": "có"
            },
            "correct": "B",
            "explanation": "Used to refers to past habits.",
            "explanation_vi": "Used to đề cập đến thói quen trong quá khứ."
        },
        3: {
            "question": "One recent report stated that (3)____ the number of hobbies had not increased, each hobby had become more specialized.",
            "question_vi": "Một báo cáo gần đây tuyên bố rằng (3)____ số lượng sở thích đã không tăng, mỗi sở thích đã trở nên chuyên môn hóa hơn.",
            "options": {
                "A": "as",
                "A_vi": "như, bởi vì",
                "B": "although",
                "B_vi": "mặc dù",
                "C": "but",
                "C_vi": "nhưng",
                "D": "because of",
                "D_vi": "bởi vì"
            },
            "correct": "B",
            "explanation": "Although shows contrast between two ideas.",
            "explanation_vi": "Although thể hiện sự tương phản giữa hai ý tưởng."
        },
        4: {
            "question": "Nowadays, many managers would rather (4)____ time with their families than stay late in the office every day.",
            "question_vi": "Ngày nay, nhiều nhà quản lý thà (4)____ thời gian với gia đình hơn là ở lại muộn tại văn phòng mỗi ngày.",
            "options": {
                "A": "spending",
                "A_vi": "tiêu, dành (V-ing)",
                "B": "spend",
                "B_vi": "tiêu, dành (V-inf)",
                "C": "spent",
                "C_vi": "đã tiêu, đã dành (V2/V3)",
                "D": "to spend",
                "D_vi": "để tiêu, để dành (to V)"
            },
            "correct": "B",
            "explanation": "Would rather is followed by a bare infinitive.",
            "explanation_vi": "Would rather được theo sau bởi động từ nguyên thể không 'to'."
        },
        5: {
            "question": "Some companies now (5)____ managers take their annual holidays even if they don't want to",
            "question_vi": "Một số công ty hiện nay (5)____ các nhà quản lý nghỉ phép hàng năm ngay cả khi họ không muốn",
            "options": {
                "A": "force",
                "A_vi": "ép buộc",
                "B": "have",
                "B_vi": "có",
                "C": "make",
                "C_vi": "khiến, bắt",
                "D": "cause",
                "D_vi": "gây ra"
            },
            "correct": "C",
            "explanation": "Make someone do something means to force or cause someone to do something.",
            "explanation_vi": "Make someone do something có nghĩa là bắt hoặc khiến ai đó làm gì."
        },
        6: {
            "question": "But Percy soon showed a talent (6)______ business and made a fortune in the fur trade and auction business.",
            "question_vi": "Nhưng Percy sớm thể hiện tài năng (6)______ kinh doanh và kiếm được một gia tài trong kinh doanh buôn bán lông thú và đấu giá.",
            "options": {
                "A": "with",
                "A_vi": "với",
                "B": "for",
                "B_vi": "cho, về",
                "C": "of",
                "C_vi": "của",
                "D": "on",
                "D_vi": "trên"
            },
            "correct": "B",
            "explanation": "Talent for something is the correct preposition.",
            "explanation_vi": "Talent for something là giới từ chính xác."
        },
        7: {
            "question": "Then disaster struck and he (7)______ all his money.",
            "question_vi": "Rồi thảm họa ập đến và anh ấy (7)______ tất cả tiền của mình.",
            "options": {
                "A": "threw",
                "A_vi": "ném",
                "B": "sent",
                "B_vi": "gửi",
                "C": "lost",
                "C_vi": "mất",
                "D": "wasted",
                "D_vi": "lãng phí"
            },
            "correct": "C",
            "explanation": "Lost means no longer having something, especially money.",
            "explanation_vi": "Lost có nghĩa là không còn có cái gì đó, đặc biệt là tiền."
        },
        8: {
            "question": "But he soon made a fortune again - this time by (8)______ plastic bags.",
            "question_vi": "Nhưng anh ấy sớm kiếm được một gia tài một lần nữa - lần này bằng cách (8)______ túi nhựa.",
            "options": {
                "A": "manufacturer",
                "A_vi": "nhà sản xuất",
                "B": "manufactured",
                "B_vi": "đã sản xuất",
                "C": "manufacturing",
                "C_vi": "sản xuất",
                "D": "manufacture",
                "D_vi": "sản xuất (động từ nguyên thể)"
            },
            "correct": "C",
            "explanation": "By + V-ing indicates the means or method.",
            "explanation_vi": "By + V-ing chỉ phương tiện hoặc phương pháp."
        },
        9: {
            "question": "After these first experiences of giving money away, Ross decided to do it on a (9)______ basis.",
            "question_vi": "Sau những trải nghiệm đầu tiên này của việc cho tiền, Ross quyết định làm điều đó trên cơ sở (9)______.",
            "options": {
                "A": "regular",
                "A_vi": "thường xuyên",
                "B": "frequent",
                "B_vi": "thường xuyên",
                "C": "occasional",
                "C_vi": "thỉnh thoảng",
                "D": "usual",
                "D_vi": "thông thường"
            },
            "correct": "A",
            "explanation": "On a regular basis means regularly or consistently.",
            "explanation_vi": "On a regular basis có nghĩa là thường xuyên hoặc đều đặn."
        },
        10: {
            "question": "It took years, but Ross finally (10)______ in giving away his entire fortune.",
            "question_vi": "Mất nhiều năm, nhưng cuối cùng Ross (10)______ trong việc cho đi toàn bộ gia tài của mình.",
            "options": {
                "A": "interested",
                "A_vi": "quan tâm",
                "B": "succeeded",
                "B_vi": "thành công",
                "C": "invested",
                "C_vi": "đầu tư",
                "D": "tried",
                "D_vi": "cố gắng"
            },
            "correct": "B",
            "explanation": "Succeed in doing something means to achieve the desired aim.",
            "explanation_vi": "Succeed in doing something có nghĩa là đạt được mục tiêu mong muốn."
        },
        11: {
            "question": "In order to (12)______ the question, we must first turn to the types of consumers.",
            "question_vi": "Để (12)______ câu hỏi, chúng ta phải trước tiên xem xét các loại người tiêu dùng.",
            "options": {
                "A": "answer",
                "A_vi": "trả lời",
                "B": "address",
                "B_vi": "giải quyết, đề cập",
                "C": "remedy",
                "C_vi": "khắc phục",
                "D": "put right",
                "D_vi": "sửa chữa"
            },
            "correct": "B",
            "explanation": "Address a question means to deal with or discuss it.",
            "explanation_vi": "Address a question có nghĩa là giải quyết hoặc thảo luận nó."
        },
        12: {
            "question": "Presumably, most parents (13)______ are always worrying about their children's safety buy mobile phones for them to track their whereabouts.",
            "question_vi": "Có lẽ, hầu hết các bậc cha mẹ (13)______ luôn lo lắng về sự an toàn của con cái mua điện thoại di động cho chúng để theo dõi vị trí của chúng.",
            "options": {
                "A": "what",
                "A_vi": "cái gì",
                "B": "whom",
                "B_vi": "ai (tân ngữ)",
                "C": "which",
                "C_vi": "cái nào",
                "D": "who",
                "D_vi": "ai (chủ ngữ)"
            },
            "correct": "D",
            "explanation": "Who is used for people as the subject of the relative clause.",
            "explanation_vi": "Who được sử dụng cho người làm chủ ngữ của mệnh đề quan hệ."
        },
        13: {
            "question": "(14)______, we cannot deny the fact that text messages have been used by bullies to intimidate fellow students.",
            "question_vi": "(14)______, chúng ta không thể phủ nhận thực tế rằng tin nhắn văn bản đã được sử dụng bởi những kẻ bắt nạt để đe dọa bạn học.",
            "options": {
                "A": "Therefore",
                "A_vi": "Vì vậy",
                "B": "Moreover",
                "B_vi": "Hơn nữa",
                "C": "However",
                "C_vi": "Tuy nhiên",
                "D": "So that",
                "D_vi": "Để mà"
            },
            "correct": "C",
            "explanation": "However introduces a contrasting idea.",
            "explanation_vi": "However giới thiệu một ý tưởng tương phản."
        },
        14: {
            "question": "There is also (15)______ evidence that texting has affected literacy skills.",
            "question_vi": "Cũng có (15)______ bằng chứng rằng nhắn tin đã ảnh hưởng đến kỹ năng đọc viết.",
            "options": {
                "A": "indisputable",
                "A_vi": "không thể tranh cãi",
                "B": "arguable",
                "B_vi": "có thể tranh luận",
                "C": "doubtless",
                "C_vi": "không nghi ngờ",
                "D": "unhesitating",
                "D_vi": "không do dự"
            },
            "correct": "A",
            "explanation": "Indisputable evidence means evidence that cannot be doubted.",
            "explanation_vi": "Indisputable evidence có nghĩa là bằng chứng không thể nghi ngờ."
        },
        15: {
            "question": "(16)______ breakfast Americans will eat cereal with milk which are often mixed (17)______ in a bowl, a glass of orange juice, and toasted bread or muffin with jam, butter, or margarine.",
            "question_vi": "(16)______ bữa sáng người Mỹ sẽ ăn ngũ cốc với sữa thường được trộn (17)______ trong một cái bát, một ly nước cam, và bánh mì nướng hoặc bánh nướng xốp với mứt, bơ, hoặc bơ thực vật.",
            "options": {
                "A": "With",
                "A_vi": "Với",
                "B": "In",
                "B_vi": "Trong",
                "C": "At",
                "C_vi": "Tại",
                "D": "For",
                "D_vi": "Cho"
            },
            "correct": "D",
            "explanation": "For breakfast means as part of the morning meal.",
            "explanation_vi": "For breakfast có nghĩa là như một phần của bữa ăn sáng."
        },
        16: {
            "question": "cereal with milk which are often mixed (17)______ in a bowl",
            "question_vi": "ngũ cốc với sữa thường được trộn (17)______ trong một cái bát",
            "options": {
                "A": "others",
                "A_vi": "những cái khác",
                "B": "each other",
                "B_vi": "nhau (hai đối tượng)",
                "C": "one another",
                "C_vi": "nhau (nhiều đối tượng)",
                "D": "together",
                "D_vi": "cùng nhau"
            },
            "correct": "D",
            "explanation": "Mixed together means combined into one mixture.",
            "explanation_vi": "Mixed together có nghĩa là kết hợp thành một hỗn hợp."
        },
        17: {
            "question": "People who are on (18)______ eat just a cup of yogurt.",
            "question_vi": "Người đang (18)______ chỉ ăn một cốc sữa chua.",
            "options": {
                "A": "diet",
                "A_vi": "ăn kiêng",
                "B": "holiday",
                "B_vi": "kỳ nghỉ",
                "C": "engagement",
                "C_vi": "hẹn ước, cam kết",
                "D": "duty",
                "D_vi": "nhiệm vụ"
            },
            "correct": "A",
            "explanation": "On a diet means following a special eating plan.",
            "explanation_vi": "On a diet có nghĩa là theo một kế hoạch ăn uống đặc biệt."
        },
        18: {
            "question": "Lunch and dinner are more (19)______.",
            "question_vi": "Bữa trưa và bữa tối thì (19)______ hơn.",
            "options": {
                "A": "varied",
                "A_vi": "đa dạng",
                "B": "vary",
                "B_vi": "thay đổi (động từ)",
                "C": "variety",
                "C_vi": "sự đa dạng (danh từ)",
                "D": "variously",
                "D_vi": "một cách đa dạng (trạng từ)"
            },
            "correct": "A",
            "explanation": "More varied means having greater diversity.",
            "explanation_vi": "More varied có nghĩa là có sự đa dạng lớn hơn."
        },
        19: {
            "question": "Most Americans do not know the answer (20)______.",
            "question_vi": "Hầu hết người Mỹ không biết câu trả lời (20)______.",
            "options": {
                "A": "either",
                "A_vi": "cũng không",
                "B": "too",
                "B_vi": "cũng (khẳng định)",
                "C": "so",
                "C_vi": "vì vậy",
                "D": "neither",
                "D_vi": "cũng không (đứng đầu câu)"
            },
            "correct": "A",
            "explanation": "Either is used in negative sentences to mean also.",
            "explanation_vi": "Either được sử dụng trong câu phủ định để có nghĩa là cũng."
        },
        20: {
            "question": "The issue is whether this technological innovation has (11)______ more harm than good.",
            "question_vi": "Vấn đề là liệu sự đổi mới công nghệ này đã (11)______ nhiều tác hại hơn lợi ích hay không.",
            "options": {
                "A": "brought",
                "A_vi": "mang lại",
                "B": "played",
                "B_vi": "chơi",
                "C": "made",
                "C_vi": "làm",
                "D": "done",
                "D_vi": "làm"
            },
            "correct": "A",
            "explanation": "Bring harm is a common collocation.",
            "explanation_vi": "Bring harm là một cụm từ thông dụng."
        }
    },
    "Part 4": {
        1: {
            "question": "I ______ my sister in December as planned.",
            "question_vi": "Tôi ______ chị gái tôi vào tháng 12 như đã lên kế hoạch.",
            "options": {
                "A": "will see",
                "A_vi": "sẽ gặp",
                "B": "have seen",
                "B_vi": "đã gặp",
                "C": "am going to see",
                "C_vi": "sẽ gặp (có kế hoạch)",
                "D": "see",
                "D_vi": "gặp"
            },
            "correct": "C",
            "explanation": "Be going to is used for plans and intentions.",
            "explanation_vi": "Be going to được dùng cho kế hoạch và dự định."
        },
        2: {
            "question": "He seems quite ______ with his new job.",
            "question_vi": "Anh ấy có vẻ khá ______ với công việc mới của mình.",
            "options": {
                "A": "satisfied",
                "A_vi": "hài lòng",
                "B": "satisfy",
                "B_vi": "làm hài lòng (động từ)",
                "C": "satisfying",
                "C_vi": "làm hài lòng (tính từ chủ động)",
                "D": "satisfies",
                "D_vi": "làm hài lòng (động từ chia ngôi thứ 3 số ít)"
            },
            "correct": "A",
            "explanation": "After 'seem', we use an adjective. 'Satisfied' describes how he feels.",
            "explanation_vi": "Sau 'seem', chúng ta dùng tính từ. 'Satisfied' mô tả cảm giác của anh ấy."
        },
        3: {
            "question": "- 'How was the game show last night?' - '______'",
            "question_vi": "- 'Chương trình trò chơi tối qua thế nào?' - '______'",
            "options": {
                "A": "Great. I gained more knowledge about biology.",
                "A_vi": "Tuyệt. Tôi đã thu thập thêm kiến thức về sinh học.",
                "B": "Just talking about it.",
                "B_vi": "Chỉ đang nói về nó thôi.",
                "C": "It showed at 8 o'clock.",
                "C_vi": "Nó chiếu lúc 8 giờ.",
                "D": "I think it wasn't a good game.",
                "D_vi": "Tôi nghĩ nó không phải là một trò chơi hay."
            },
            "correct": "A",
            "explanation": "This is an appropriate response to a question about a game show's quality.",
            "explanation_vi": "Đây là phản hồi phù hợp với câu hỏi về chất lượng của một chương trình trò chơi."
        },
        4: {
            "question": "Internet cafes allow you ______ your web-based email account.",
            "question_vi": "Quán cà phê Internet cho phép bạn ______ tài khoản email dựa trên web của bạn.",
            "options": {
                "A": "be accessed",
                "A_vi": "được truy cập",
                "B": "accessing",
                "B_vi": "truy cập (V-ing)",
                "C": "access",
                "C_vi": "truy cập (V-inf)",
                "D": "to access",
                "D_vi": "để truy cập (to V)"
            },
            "correct": "D",
            "explanation": "'Allow someone to do something' is the correct structure.",
            "explanation_vi": "'Allow someone to do something' là cấu trúc chính xác."
        },
        5: {
            "question": "- Where is Jimmy? - He is ______ work. He is busy ______ his monthly report.",
            "question_vi": "- Jimmy ở đâu? - Anh ấy ______ làm việc. Anh ấy đang bận ______ báo cáo hàng tháng của mình.",
            "options": {
                "A": "in / about",
                "A_vi": "ở trong / về",
                "B": "at / with",
                "B_vi": "ở tại / với",
                "C": "to / through",
                "C_vi": "đến / qua",
                "D": "on / for",
                "D_vi": "trên / cho"
            },
            "correct": "B",
            "explanation": "'At work' means at the workplace. 'Busy with something' is the correct preposition.",
            "explanation_vi": "'At work' có nghĩa là ở nơi làm việc. 'Busy with something' là cấu trúc giới từ chính xác."
        },
        6: {
            "question": "Are you looking forward ______ on your vacation?",
            "question_vi": "Bạn có mong đợi ______ trong kỳ nghỉ của mình không?",
            "options": {
                "A": "going",
                "A_vi": "đi (V-ing)",
                "B": "to going",
                "B_vi": "đến việc đi (to + V-ing)",
                "C": "to go",
                "C_vi": "để đi (to + V-inf)",
                "D": "you go",
                "D_vi": "bạn đi"
            },
            "correct": "B",
            "explanation": "Look forward to + V-ing is the correct structure.",
            "explanation_vi": "Look forward to + V-ing là cấu trúc chính xác."
        },
        7: {
            "question": "______ is the controller of the body.",
            "question_vi": "______ là bộ điều khiển của cơ thể.",
            "options": {
                "A": "Nervous System",
                "A_vi": "Hệ thần kinh",
                "B": "Digestive System",
                "B_vi": "Hệ tiêu hóa",
                "C": "Skeletal System",
                "C_vi": "Hệ xương",
                "D": "Circulatory System",
                "D_vi": "Hệ tuần hoàn"
            },
            "correct": "A",
            "explanation": "The nervous system controls body functions.",
            "explanation_vi": "Hệ thần kinh điều khiển các chức năng cơ thể."
        },
        8: {
            "question": "It is thought that Google ______ cars may transform the way we move around cities in the future.",
            "question_vi": "Người ta nghĩ rằng ô tô ______ của Google có thể thay đổi cách chúng ta di chuyển quanh các thành phố trong tương lai.",
            "options": {
                "A": "motionless",
                "A_vi": "bất động",
                "B": "driver",
                "B_vi": "tài xế",
                "C": "driverless",
                "C_vi": "không người lái",
                "D": "driving",
                "D_vi": "lái xe"
            },
            "correct": "C",
            "explanation": "Driverless cars are autonomous vehicles.",
            "explanation_vi": "Xe không người lái là phương tiện tự động."
        },
        9: {
            "question": "Do you get ______ if your parents ask you to help out in your free time?",
            "question_vi": "Bạn có cảm thấy ______ nếu bố mẹ yêu cầu bạn giúp đỡ vào thời gian rảnh không?",
            "options": {
                "A": "boring",
                "A_vi": "nhàm chán (tính từ chủ động)",
                "B": "exciting",
                "B_vi": "thú vị",
                "C": "annoyed",
                "C_vi": "khó chịu (tính từ bị động)",
                "D": "annoying",
                "D_vi": "gây khó chịu (tính từ chủ động)"
            },
            "correct": "C",
            "explanation": "Get annoyed means become irritated or angry.",
            "explanation_vi": "Get annoyed có nghĩa là trở nên khó chịu hoặc tức giận."
        },
        10: {
            "question": "I ______ buy a new car, so I'm saving as much money as possible.",
            "question_vi": "Tôi ______ mua một chiếc xe hơi mới, vì vậy tôi đang tiết kiệm càng nhiều tiền càng tốt.",
            "options": {
                "A": "am going to",
                "A_vi": "sẽ (có kế hoạch)",
                "B": "will be",
                "B_vi": "sẽ là",
                "C": "can",
                "C_vi": "có thể",
                "D": "will",
                "D_vi": "sẽ (quyết định tại thời điểm nói)"
            },
            "correct": "A",
            "explanation": "Be going to indicates a planned future action.",
            "explanation_vi": "Be going to chỉ một hành động tương lai có kế hoạch."
        },
        11: {
            "question": "YouTube ______ to become the world most popular video-sharing website since 2005.",
            "question_vi": "YouTube ______ trở thành trang web chia sẻ video phổ biến nhất thế giới kể từ năm 2005.",
            "options": {
                "A": "grows",
                "A_vi": "phát triển (hiện tại đơn)",
                "B": "grew",
                "B_vi": "đã phát triển (quá khứ đơn)",
                "C": "have grown",
                "C_vi": "đã phát triển (hiện tại hoàn thành)",
                "D": "has grown",
                "D_vi": "đã phát triển (hiện tại hoàn thành, ngôi thứ 3 số ít)"
            },
            "correct": "D",
            "explanation": "Since 2005 requires present perfect tense. YouTube is singular.",
            "explanation_vi": "Since 2005 đòi hỏi thì hiện tại hoàn thành. YouTube là số ít."
        },
        12: {
            "question": "We are talking about the writer ______ latest book is one of the best-sellers this year.",
            "question_vi": "Chúng ta đang nói về nhà văn ______ cuốn sách mới nhất là một trong những sách bán chạy nhất năm nay.",
            "options": {
                "A": "whom",
                "A_vi": "người mà (tân ngữ)",
                "B": "who",
                "B_vi": "người mà (chủ ngữ)",
                "C": "whose",
                "C_vi": "của người mà (sở hữu)",
                "D": "which",
                "D_vi": "cái mà (vật)"
            },
            "correct": "C",
            "explanation": "Whose shows possession (the writer's latest book).",
            "explanation_vi": "Whose thể hiện sở hữu (cuốn sách mới nhất của nhà văn)."
        },
        13: {
            "question": "Your job is likely to include welcoming guests and receiving ______ for our Charity Centre.",
            "question_vi": "Công việc của bạn có khả năng bao gồm chào đón khách và nhận ______ cho Trung tâm Từ thiện của chúng tôi.",
            "options": {
                "A": "donated",
                "A_vi": "được quyên góp (quá khứ phân từ)",
                "B": "donate",
                "B_vi": "quyên góp (động từ)",
                "C": "donors",
                "C_vi": "người quyên góp (danh từ)",
                "D": "donations",
                "D_vi": "sự quyên góp, vật quyên góp (danh từ)"
            },
            "correct": "D",
            "explanation": "Receiving donations means accepting gifts or contributions.",
            "explanation_vi": "Receiving donations có nghĩa là nhận quà tặng hoặc đóng góp."
        },
        14: {
            "question": "______ is the member of a family who earns the money that the family needs.",
            "question_vi": "______ là thành viên của gia đình người kiếm tiền mà gia đình cần.",
            "options": {
                "A": "Homemaker",
                "A_vi": "Người nội trợ",
                "B": "Husband",
                "B_vi": "Người chồng",
                "C": "Women",
                "C_vi": "Phụ nữ",
                "D": "Breadwinner",
                "D_vi": "Trụ cột gia đình"
            },
            "correct": "D",
            "explanation": "Breadwinner is the person who earns money to support the family.",
            "explanation_vi": "Breadwinner là người kiếm tiền để hỗ trợ gia đình."
        },
        15: {
            "question": "If you ______ the doctor's advice, you won't get well.",
            "question_vi": "Nếu bạn ______ lời khuyên của bác sĩ, bạn sẽ không khỏe lại.",
            "options": {
                "A": "don't listen",
                "A_vi": "không lắng nghe",
                "B": "take",
                "B_vi": "lấy, uống",
                "C": "ignore",
                "C_vi": "phớt lờ",
                "D": "follow",
                "D_vi": "tuân theo"
            },
            "correct": "C",
            "explanation": "Ignore means to pay no attention to something.",
            "explanation_vi": "Ignore có nghĩa là không chú ý đến điều gì đó."
        },
        16: {
            "question": "The father typically works outside the home while the mother is ______ domestic duties such as homemaking and raising children.",
            "question_vi": "Người cha thường làm việc bên ngoài nhà trong khi người mẹ ______ các nhiệm vụ gia đình như nội trợ và nuôi dạy con cái.",
            "options": {
                "A": "aware of",
                "A_vi": "nhận thức về",
                "B": "capable of",
                "B_vi": "có khả năng",
                "C": "suitable for",
                "C_vi": "phù hợp với",
                "D": "responsible for",
                "D_vi": "chịu trách nhiệm về"
            },
            "correct": "D",
            "explanation": "Responsible for means having the duty of doing something.",
            "explanation_vi": "Responsible for có nghĩa là có nhiệm vụ làm điều gì đó."
        },
        17: {
            "question": "The more polite you appear to be, ______ your partner will be.",
            "question_vi": "Bạn càng tỏ ra lịch sự, ______ đối tác của bạn sẽ càng.",
            "options": {
                "A": "the happiest",
                "A_vi": "hạnh phúc nhất",
                "B": "the more happily",
                "B_vi": "càng hạnh phúc hơn (trạng từ)",
                "C": "the happier",
                "C_vi": "càng hạnh phúc hơn (tính từ)",
                "D": "the most happily",
                "D_vi": "hạnh phúc nhất (trạng từ)"
            },
            "correct": "C",
            "explanation": "The + comparative adjective... the + comparative adjective structure.",
            "explanation_vi": "Cấu trúc The + tính từ so sánh hơn... the + tính từ so sánh hơn."
        },
        18: {
            "question": "John made me ______ a lot with his hilarious jokes.",
            "question_vi": "John làm tôi ______ rất nhiều với những câu chuyện cười hài hước của anh ấy.",
            "options": {
                "A": "laugh",
                "A_vi": "cười (V-inf)",
                "B": "laughed",
                "B_vi": "đã cười (V2/V3)",
                "C": "laughing",
                "C_vi": "cười (V-ing)",
                "D": "to laugh",
                "D_vi": "để cười (to V)"
            },
            "correct": "A",
            "explanation": "Make + someone + bare infinitive (without to).",
            "explanation_vi": "Make + someone + động từ nguyên thể không 'to'."
        },
        19: {
            "question": "Only humans produce ______ tears.",
            "question_vi": "Chỉ con người sản xuất nước mắt ______.",
            "options": {
                "A": "false",
                "A_vi": "giả",
                "B": "emotional",
                "B_vi": "cảm xúc",
                "C": "crocodile",
                "C_vi": "cá sấu (giả dối)",
                "D": "feel",
                "D_vi": "cảm giác"
            },
            "correct": "B",
            "explanation": "Emotional tears are tears caused by emotions.",
            "explanation_vi": "Nước mắt cảm xúc là nước mắt gây ra bởi cảm xúc."
        },
        20: {
            "question": "Treat others the way you want ______",
            "question_vi": "Đối xử với người khác theo cách bạn muốn ______",
            "options": {
                "A": "to treat",
                "A_vi": "đối xử (chủ động)",
                "B": "to be treat",
                "B_vi": "được đối xử (sai chính tả)",
                "C": "to be treated",
                "C_vi": "được đối xử (bị động)",
                "D": "treating",
                "D_vi": "đối xử (V-ing)"
            },
            "correct": "C",
            "explanation": "Passive infinitive (to be treated) is needed because you want to receive the treatment.",
            "explanation_vi": "Động từ nguyên thể bị động (to be treated) cần thiết vì bạn muốn nhận sự đối xử."
        },
        21: {
            "question": "Her husband is very kind. He always cares about her and never puts all of the housework ______ her.",
            "question_vi": "Chồng cô ấy rất tốt bụng. Anh ấy luôn quan tâm đến cô ấy và không bao giờ đặt tất cả việc nhà ______ cô ấy.",
            "options": {
                "A": "in",
                "A_vi": "trong",
                "B": "on",
                "B_vi": "trên",
                "C": "about",
                "C_vi": "về",
                "D": "with",
                "D_vi": "với"
            },
            "correct": "B",
            "explanation": "Put something on someone means to make someone responsible for something.",
            "explanation_vi": "Put something on someone có nghĩa là làm cho ai đó chịu trách nhiệm về việc gì."
        },
        22: {
            "question": "Don't phone me between 6.00 and 9.00 tonight. I ______ then.",
            "question_vi": "Đừng gọi điện cho tôi giữa 6.00 và 9.00 tối nay. Tôi ______ lúc đó.",
            "options": {
                "A": "will study",
                "A_vi": "sẽ học",
                "B": "am studying",
                "B_vi": "đang học (hiện tại tiếp diễn)",
                "C": "will be studying",
                "C_vi": "sẽ đang học (tương lai tiếp diễn)",
                "D": "study",
                "D_vi": "học (hiện tại đơn)"
            },
            "correct": "C",
            "explanation": "Future continuous tense for an action in progress at a specific future time.",
            "explanation_vi": "Thì tương lai tiếp diễn cho hành động đang diễn ra tại một thời điểm cụ thể trong tương lai."
        },
        23: {
            "question": "American Idol began in 2002, ______ quickly became the most popular entertainment series with viewers in the hundreds of millions.",
            "question_vi": "American Idol bắt đầu vào năm 2002, ______ nhanh chóng trở thành series giải trí phổ biến nhất với người xem hàng trăm triệu.",
            "options": {
                "A": "so",
                "A_vi": "vì vậy",
                "B": "but",
                "B_vi": "nhưng",
                "C": "or",
                "C_vi": "hoặc",
                "D": "and",
                "D_vi": "và"
            },
            "correct": "D",
            "explanation": "And connects two related ideas.",
            "explanation_vi": "And kết nối hai ý tưởng liên quan."
        },
        24: {
            "question": "After eating dinner, I have to do the ______ and then do my homework every day.",
            "question_vi": "Sau khi ăn tối, tôi phải làm ______ và sau đó làm bài tập về nhà mỗi ngày.",
            "options": {
                "A": "wash-up",
                "A_vi": "rửa ráy",
                "B": "washing-ups",
                "B_vi": "việc rửa bát (sai số nhiều)",
                "C": "washing-up",
                "C_vi": "việc rửa bát",
                "D": "washings-up",
                "D_vi": "việc rửa bát (sai số nhiều)"
            },
            "correct": "C",
            "explanation": "Washing-up means washing dishes after a meal.",
            "explanation_vi": "Washing-up có nghĩa là rửa bát sau bữa ăn."
        },
        25: {
            "question": "He asked me why ______ to the meeting.",
            "question_vi": "Anh ấy hỏi tôi tại sao ______ đến cuộc họp.",
            "options": {
                "A": "you didn't come",
                "A_vi": "bạn đã không đến",
                "B": "I hadn't come",
                "B_vi": "tôi đã không đến",
                "C": "didn't I come",
                "C_vi": "tôi đã không đến (sai cấu trúc)",
                "D": "don't I come",
                "D_vi": "tôi không đến (sai thì)"
            },
            "correct": "B",
            "explanation": "Reported question: why + subject + verb (past perfect for past action).",
            "explanation_vi": "Câu hỏi gián tiếp: why + chủ ngữ + động từ (quá khứ hoàn thành cho hành động quá khứ)."
        },
        26: {
            "question": "I'm responsible for cooking dinner as my mother usually works ______.",
            "question_vi": "Tôi chịu trách nhiệm nấu bữa tối vì mẹ tôi thường làm việc ______.",
            "options": {
                "A": "lately",
                "A_vi": "gần đây",
                "B": "later",
                "B_vi": "muộn hơn",
                "C": "early",
                "C_vi": "sớm",
                "D": "late",
                "D_vi": "muộn"
            },
            "correct": "D",
            "explanation": "Work late means work until late in the day.",
            "explanation_vi": "Work late có nghĩa là làm việc đến muộn trong ngày."
        },
        27: {
            "question": "He passed his exams ______.",
            "question_vi": "Anh ấy đã vượt qua kỳ thi của mình ______.",
            "options": {
                "A": "successes",
                "A_vi": "những thành công (danh từ số nhiều)",
                "B": "successful",
                "B_vi": "thành công (tính từ)",
                "C": "successfully",
                "C_vi": "một cách thành công (trạng từ)",
                "D": "success",
                "D_vi": "thành công (danh từ)"
            },
            "correct": "C",
            "explanation": "Adverb (successfully) modifies the verb (passed).",
            "explanation_vi": "Trạng từ (successfully) bổ nghĩa cho động từ (passed)."
        },
        28: {
            "question": "All forms of discrimination against all women and girls ______ immediately everywhere.",
            "question_vi": "Mọi hình thức phân biệt đối xử đối với tất cả phụ nữ và trẻ em gái ______ ngay lập tức ở mọi nơi.",
            "options": {
                "A": "must be taken away",
                "A_vi": "phải được lấy đi",
                "B": "must be followed",
                "B_vi": "phải được theo sau",
                "C": "must be allowed",
                "C_vi": "phải được cho phép",
                "D": "must be ended",
                "D_vi": "phải được chấm dứt"
            },
            "correct": "D",
            "explanation": "End discrimination means stop discrimination.",
            "explanation_vi": "End discrimination có nghĩa là chấm dứt phân biệt đối xử."
        },
        29: {
            "question": "Paddle-wheel machine helps to clean the wastewater before ______ it for farming.",
            "question_vi": "Máy bánh xe guồng giúp làm sạch nước thải trước khi ______ nó cho nông nghiệp.",
            "options": {
                "A": "recycling",
                "A_vi": "tái chế",
                "B": "reducing",
                "B_vi": "giảm",
                "C": "rearranging",
                "C_vi": "sắp xếp lại",
                "D": "reusing",
                "D_vi": "tái sử dụng"
            },
            "correct": "D",
            "explanation": "Reusing means using again.",
            "explanation_vi": "Reusing có nghĩa là sử dụng lại."
        },
        30: {
            "question": "Today my mother can't help ______ the cooking because she is ill.",
            "question_vi": "Hôm nay mẹ tôi không thể giúp ______ nấu ăn vì bà ấy bị ốm.",
            "options": {
                "A": "for",
                "A_vi": "cho",
                "B": "with",
                "B_vi": "với",
                "C": "of",
                "C_vi": "của",
                "D": "in",
                "D_vi": "trong"
            },
            "correct": "B",
            "explanation": "Help with something means assist in doing something.",
            "explanation_vi": "Help with something có nghĩa là hỗ trợ làm điều gì đó."
        },
        31: {
            "question": "My teacher assigned us a writing task about ______ of our favorite singers.",
            "question_vi": "Giáo viên của tôi giao cho chúng tôi một nhiệm vụ viết về ______ của ca sĩ yêu thích của chúng tôi.",
            "options": {
                "A": "biography",
                "A_vi": "tiểu sử",
                "B": "biodiversity",
                "B_vi": "đa dạng sinh học",
                "C": "biology",
                "C_vi": "sinh học",
                "D": "biochemist",
                "D_vi": "nhà hóa sinh"
            },
            "correct": "A",
            "explanation": "Biography is the story of a person's life.",
            "explanation_vi": "Biography là câu chuyện về cuộc đời của một người."
        },
        32: {
            "question": "I'd like ______ all of you to enjoy my party on this Friday.",
            "question_vi": "Tôi muốn ______ tất cả các bạn thưởng thức bữa tiệc của tôi vào thứ Sáu này.",
            "options": {
                "A": "inviting",
                "A_vi": "mời (V-ing)",
                "B": "invite",
                "B_vi": "mời (V-inf)",
                "C": "not invite",
                "C_vi": "không mời",
                "D": "to invite",
                "D_vi": "để mời (to V)"
            },
            "correct": "D",
            "explanation": "Would like + to + infinitive.",
            "explanation_vi": "Would like + to + động từ nguyên thể."
        },
        33: {
            "question": "Volunteers become well ______ of the problems facing the world.",
            "question_vi": "Tình nguyện viên trở nên ______ tốt về các vấn đề mà thế giới đang đối mặt.",
            "options": {
                "A": "concerned",
                "A_vi": "quan tâm",
                "B": "interested",
                "B_vi": "quan tâm, thích thú",
                "C": "aware",
                "C_vi": "nhận thức",
                "D": "helpful",
                "D_vi": "hữu ích"
            },
            "correct": "C",
            "explanation": "Become aware of means become conscious of.",
            "explanation_vi": "Become aware of có nghĩa là trở nên nhận thức về."
        },
        34: {
            "question": "They had a global ______ hit with their album concept about 'The dark side of the Moon'.",
            "question_vi": "Họ đã có một bản hit ______ toàn cầu với khái niệm album về 'Mặt tối của Mặt trăng'.",
            "options": {
                "A": "top",
                "A_vi": "đứng đầu",
                "B": "popular",
                "B_vi": "phổ biến",
                "C": "smash",
                "C_vi": "đột phá, thành công lớn",
                "D": "song",
                "D_vi": "bài hát"
            },
            "correct": "C",
            "explanation": "Smash hit means a very successful song or performance.",
            "explanation_vi": "Smash hit có nghĩa là một bài hát hoặc màn trình diễn rất thành công."
        },
        35: {
            "question": "My parents let my sister ______ camping with her friends in the mountain.",
            "question_vi": "Bố mẹ tôi để chị tôi ______ cắm trại với bạn bè của cô ấy trên núi.",
            "options": {
                "A": "to go",
                "A_vi": "để đi (to V)",
                "B": "going",
                "B_vi": "đi (V-ing)",
                "C": "not go",
                "C_vi": "không đi",
                "D": "go",
                "D_vi": "đi (V-inf)"
            },
            "correct": "D",
            "explanation": "Let + someone + bare infinitive (without to).",
            "explanation_vi": "Let + someone + động từ nguyên thể không 'to'."
        },
        36: {
            "question": "Maria: 'Thanks for the lovely evening.' Diana: '______.'",
            "question_vi": "Maria: 'Cảm ơn vì buổi tối tuyệt vời.' Diana: '______.'",
            "options": {
                "A": "Oh, that's right",
                "A_vi": "Ồ, đúng vậy",
                "B": "I'm glad you enjoyed it",
                "B_vi": "Tôi vui vì bạn thích nó",
                "C": "Yes, it's really great John",
                "C_vi": "Vâng, nó thực sự tuyệt vời John",
                "D": "No, it's not good",
                "D_vi": "Không, nó không tốt"
            },
            "correct": "B",
            "explanation": "Appropriate response to thanks for an event.",
            "explanation_vi": "Phản hồi thích hợp với lời cảm ơn cho một sự kiện."
        },
        37: {
            "question": "- 'What are you arguing about?' - '______'",
            "question_vi": "- 'Các bạn đang tranh luận về cái gì vậy?' - '______'",
            "options": {
                "A": "Well, I think she's right.",
                "A_vi": "Chà, tôi nghĩ cô ấy đúng.",
                "B": "That doesn't matter.",
                "B_vi": "Điều đó không quan trọng.",
                "C": "Nothing.",
                "C_vi": "Không có gì.",
                "D": "Yes, we are",
                "D_vi": "Vâng, chúng tôi đang tranh luận"
            },
            "correct": "C",
            "explanation": "Common response to avoid discussing the argument.",
            "explanation_vi": "Phản hồi phổ biến để tránh thảo luận về cuộc tranh luận."
        },
        38: {
            "question": "Their massive salaries let them afford to give ______ huge amounts to charities.",
            "question_vi": "Mức lương khổng lồ của họ cho phép họ đủ khả năng để ______ số tiền lớn cho các tổ chức từ thiện.",
            "options": {
                "A": "hack",
                "A_vi": "hack",
                "B": "off",
                "B_vi": "tắt",
                "C": "away",
                "C_vi": "đi",
                "D": "up",
                "D_vi": "lên"
            },
            "correct": "C",
            "explanation": "Give away means donate or give for free.",
            "explanation_vi": "Give away có nghĩa là quyên góp hoặc cho miễn phí."
        },
        39: {
            "question": "I was enjoying my book, but I stopped ______ a program on TV.",
            "question_vi": "Tôi đang thích thú với cuốn sách của mình, nhưng tôi đã dừng lại ______ một chương trình trên TV.",
            "options": {
                "A": "reading to watch",
                "A_vi": "đọc để xem",
                "B": "reading for to watch",
                "B_vi": "đọc để xem (sai cấu trúc)",
                "C": "to read to watch",
                "C_vi": "để đọc để xem",
                "D": "to read for watching",
                "D_vi": "để đọc cho việc xem"
            },
            "correct": "A",
            "explanation": "Stop + V-ing + to + V means cease one activity to start another.",
            "explanation_vi": "Stop + V-ing + to + V có nghĩa là dừng một hoạt động để bắt đầu một hoạt động khác."
        },
        40: {
            "question": "It is ______ to work in this city with so much noise and pollution.",
            "question_vi": "Thật là ______ để làm việc ở thành phố này với quá nhiều tiếng ồn và ô nhiễm.",
            "options": {
                "A": "health",
                "A_vi": "sức khỏe (danh từ)",
                "B": "healthy",
                "B_vi": "khỏe mạnh",
                "C": "healthful",
                "C_vi": "tốt cho sức khỏe",
                "D": "unhealthy",
                "D_vi": "không tốt cho sức khỏe"
            },
            "correct": "D",
            "explanation": "Unhealthy means not good for health.",
            "explanation_vi": "Unhealthy có nghĩa là không tốt cho sức khỏe."
        },
        41: {
            "question": "Hoang ______ his email four times a week in order not to miss anything important.",
            "question_vi": "Hoàng ______ email của anh ấy bốn lần một tuần để không bỏ lỡ bất cứ điều gì quan trọng.",
            "options": {
                "A": "is checking",
                "A_vi": "đang kiểm tra",
                "B": "will check",
                "B_vi": "sẽ kiểm tra",
                "C": "checks",
                "C_vi": "kiểm tra (thói quen)",
                "D": "check",
                "D_vi": "kiểm tra (nguyên thể)"
            },
            "correct": "C",
            "explanation": "Present simple for habitual actions.",
            "explanation_vi": "Hiện tại đơn cho hành động thói quen."
        },
        42: {
            "question": "Van Cao is one of the most well-known ______ in Viet Nam.",
            "question_vi": "Văn Cao là một trong những ______ nổi tiếng nhất ở Việt Nam.",
            "options": {
                "A": "singers",
                "A_vi": "ca sĩ",
                "B": "musicians",
                "B_vi": "nhạc sĩ",
                "C": "authors",
                "C_vi": "tác giả",
                "D": "actors",
                "D_vi": "diễn viên"
            },
            "correct": "B",
            "explanation": "Van Cao is a famous composer (musician).",
            "explanation_vi": "Văn Cao là một nhà soạn nhạc (nhạc sĩ) nổi tiếng."
        },
        43: {
            "question": "These games are challenging, ______ it's not easy to spend little time playing them.",
            "question_vi": "Những trò chơi này đầy thách thức, ______ không dễ dàng để dành ít thời gian chơi chúng.",
            "options": {
                "A": "so",
                "A_vi": "vì vậy",
                "B": "and",
                "B_vi": "và",
                "C": "for",
                "C_vi": "vì",
                "D": "or",
                "D_vi": "hoặc"
            },
            "correct": "A",
            "explanation": "So shows result or consequence.",
            "explanation_vi": "So thể hiện kết quả hoặc hậu quả."
        },
        44: {
            "question": "Mrs. Huyen is ______ with what her son did.",
            "question_vi": "Bà Huyền ______ với những gì con trai bà đã làm.",
            "options": {
                "A": "disappointed",
                "A_vi": "thất vọng",
                "B": "disappoint",
                "B_vi": "làm thất vọng (động từ)",
                "C": "disappointment",
                "C_vi": "sự thất vọng (danh từ)",
                "D": "disappointing",
                "D_vi": "gây thất vọng (tính từ chủ động)"
            },
            "correct": "A",
            "explanation": "Be disappointed with something means feel unhappy because something is not as good as expected.",
            "explanation_vi": "Be disappointed with something có nghĩa là cảm thấy không vui vì điều gì đó không tốt như mong đợi."
        },
        45: {
            "question": "I am going to have a short rest as I ______ a headache.",
            "question_vi": "Tôi sẽ nghỉ ngơi một chút vì tôi ______ đau đầu.",
            "options": {
                "A": "feel",
                "A_vi": "cảm thấy",
                "B": "have",
                "B_vi": "có",
                "C": "suffer",
                "C_vi": "chịu đựng",
                "D": "take",
                "D_vi": "lấy"
            },
            "correct": "B",
            "explanation": "Have a headache is the common expression.",
            "explanation_vi": "Have a headache là cách diễn đạt phổ biến."
        },
        46: {
            "question": "Only the best ______ is recruited.",
            "question_vi": "Chỉ có ______ tốt nhất được tuyển dụng.",
            "options": {
                "A": "employee",
                "A_vi": "nhân viên",
                "B": "application",
                "B_vi": "đơn xin việc",
                "C": "candidate",
                "C_vi": "ứng viên",
                "D": "CV",
                "D_vi": "sơ yếu lý lịch"
            },
            "correct": "C",
            "explanation": "Candidate is a person who applies for a job.",
            "explanation_vi": "Candidate là người nộp đơn xin việc."
        },
        47: {
            "question": "He was offered the job despite his poor ______.",
            "question_vi": "Anh ấy được đề nghị công việc mặc dù ______ kém của mình.",
            "options": {
                "A": "qualifications",
                "A_vi": "bằng cấp, trình độ",
                "B": "achievements",
                "B_vi": "thành tựu",
                "C": "preparations",
                "C_vi": "sự chuẩn bị",
                "D": "expressions",
                "D_vi": "biểu hiện, cách diễn đạt"
            },
            "correct": "A",
            "explanation": "Qualifications refer to skills, education, or experience.",
            "explanation_vi": "Qualifications đề cập đến kỹ năng, giáo dục hoặc kinh nghiệm."
        },
        48: {
            "question": "The cashiers were asked to watch out ______ forged banknotes.",
            "question_vi": "Các nhân viên thu ngân được yêu cầu cảnh giác ______ tiền giả.",
            "options": {
                "A": "for",
                "A_vi": "cho",
                "B": "on",
                "B_vi": "trên",
                "C": "to",
                "C_vi": "đến",
                "D": "with",
                "D_vi": "với"
            },
            "correct": "A",
            "explanation": "Watch out for means be alert to danger.",
            "explanation_vi": "Watch out for có nghĩa là cảnh giác với nguy hiểm."
        },
        49: {
            "question": "A skilled ______ will help candidates feel relaxed.",
            "question_vi": "Một ______ có kỹ năng sẽ giúp các ứng viên cảm thấy thoải mái.",
            "options": {
                "A": "interviewing",
                "A_vi": "phỏng vấn (danh động từ)",
                "B": "interviewee",
                "B_vi": "người được phỏng vấn",
                "C": "interviewer",
                "C_vi": "người phỏng vấn",
                "D": "interview",
                "D_vi": "cuộc phỏng vấn"
            },
            "correct": "C",
            "explanation": "Interviewer is the person who asks questions in an interview.",
            "explanation_vi": "Interviewer là người đặt câu hỏi trong một cuộc phỏng vấn."
        },
        50: {
            "question": "He behaved ______ nothing had happened.",
            "question_vi": "Anh ấy cư xử ______ không có gì đã xảy ra.",
            "options": {
                "A": "if",
                "A_vi": "nếu",
                "B": "as if",
                "B_vi": "như thể",
                "C": "before",
                "C_vi": "trước khi",
                "D": "because",
                "D_vi": "bởi vì"
            },
            "correct": "B",
            "explanation": "As if introduces a manner clause suggesting something unreal.",
            "explanation_vi": "As if giới thiệu một mệnh đề cách thức gợi ý điều gì đó không thực."
        },
        51: {
            "question": "After working at the same company for thirty years, my grandfather was looking forward to his ______.",
            "question_vi": "Sau khi làm việc tại cùng một công ty trong ba mươi năm, ông tôi đã mong đợi ______ của mình.",
            "options": {
                "A": "charity",
                "A_vi": "từ thiện",
                "B": "pension",
                "B_vi": "lương hưu",
                "C": "allowance",
                "C_vi": "trợ cấp",
                "D": "overtime",
                "D_vi": "làm thêm giờ"
            },
            "correct": "B",
            "explanation": "Pension is money paid regularly to a retired person.",
            "explanation_vi": "Pension là tiền được trả thường xuyên cho một người đã nghỉ hưu."
        },
        52: {
            "question": "After three years working hard, he was ______.",
            "question_vi": "Sau ba năm làm việc chăm chỉ, anh ấy đã được ______.",
            "options": {
                "A": "advanced",
                "A_vi": "tiến bộ, thăng tiến",
                "B": "raised",
                "B_vi": "nâng lên, tăng lên",
                "C": "promoted",
                "C_vi": "thăng chức",
                "D": "elevated",
                "D_vi": "nâng cao"
            },
            "correct": "C",
            "explanation": "Promoted means given a higher position or rank.",
            "explanation_vi": "Promoted có nghĩa là được cho một vị trí hoặc cấp bậc cao hơn."
        },
        53: {
            "question": "People usually use more ______ language when they're in serious situations like interviews.",
            "question_vi": "Mọi người thường sử dụng ngôn ngữ ______ hơn khi họ ở trong những tình huống nghiêm túc như phỏng vấn.",
            "options": {
                "A": "serious",
                "A_vi": "nghiêm túc",
                "B": "solemn",
                "B_vi": "trang nghiêm",
                "C": "formal",
                "C_vi": "trang trọng",
                "D": "informal",
                "D_vi": "không trang trọng"
            },
            "correct": "C",
            "explanation": "Formal language is used in official or serious contexts.",
            "explanation_vi": "Ngôn ngữ trang trọng được sử dụng trong các ngữ cảnh chính thức hoặc nghiêm túc."
        },
        54: {
            "question": "He has all the right ______ for the job.",
            "question_vi": "Anh ấy có tất cả ______ phù hợp cho công việc.",
            "options": {
                "A": "degrees",
                "A_vi": "bằng cấp",
                "B": "certificates",
                "B_vi": "chứng chỉ",
                "C": "qualifications",
                "C_vi": "trình độ, năng lực",
                "D": "diplomas",
                "D_vi": "văn bằng"
            },
            "correct": "C",
            "explanation": "Qualifications include skills, knowledge, and experience.",
            "explanation_vi": "Qualifications bao gồm kỹ năng, kiến thức và kinh nghiệm."
        },
        55: {
            "question": "Mary: 'I've made a lot of new friends.' Mary's mother: '______'",
            "question_vi": "Mary: 'Con đã kết bạn được rất nhiều bạn mới.' Mẹ của Mary: '______'",
            "options": {
                "A": "You are doing so well, dear.",
                "A_vi": "Con đang làm rất tốt, con yêu.",
                "B": "I can't agree more with yours.",
                "B_vi": "Mẹ không thể đồng ý hơn với con.",
                "C": "I feel so sorry for you, my girl.",
                "C_vi": "Mẹ cảm thấy rất tiếc cho con, con gái của mẹ.",
                "D": "You can never understand, dear.",
                "D_vi": "Con không bao giờ có thể hiểu được, con yêu."
            },
            "correct": "A",
            "explanation": "Positive and encouraging response.",
            "explanation_vi": "Phản hồi tích cực và khích lệ."
        },
        56: {
            "question": "The chairman didn't make any ______ upon the matter.",
            "question_vi": "Chủ tịch đã không đưa ra bất kỳ ______ nào về vấn đề này.",
            "options": {
                "A": "evaluation",
                "A_vi": "đánh giá",
                "B": "investment",
                "B_vi": "đầu tư",
                "C": "opinion",
                "C_vi": "ý kiến",
                "D": "comment",
                "D_vi": "bình luận"
            },
            "correct": "D",
            "explanation": "Make a comment on something is a common phrase.",
            "explanation_vi": "Make a comment on something là một cụm từ phổ biến."
        },
        57: {
            "question": "Don't you think you should apply for the job ______ writing?",
            "question_vi": "Bạn không nghĩ rằng bạn nên nộp đơn xin việc ______ văn bản sao?",
            "options": {
                "A": "at",
                "A_vi": "tại",
                "B": "with",
                "B_vi": "với",
                "C": "in",
                "C_vi": "trong",
                "D": "for",
                "D_vi": "cho"
            },
            "correct": "C",
            "explanation": "In writing means in written form.",
            "explanation_vi": "In writing có nghĩa là bằng văn bản."
        },
        58: {
            "question": "Finding a job in this time of economic crisis is becoming ______",
            "question_vi": "Tìm việc làm trong thời kỳ khủng hoảng kinh tế này đang trở nên ______",
            "options": {
                "A": "as more difficult than",
                "A_vi": "như khó hơn so với",
                "B": "more difficult than",
                "B_vi": "khó hơn so với",
                "C": "more and more difficult",
                "C_vi": "ngày càng khó khăn hơn",
                "D": "more than difficult",
                "D_vi": "hơn là khó"
            },
            "correct": "C",
            "explanation": "More and more difficult indicates increasing difficulty.",
            "explanation_vi": "More and more difficult chỉ sự khó khăn ngày càng tăng."
        },
        59: {
            "question": "Being a flight attendant is a ______ job. You may have to work long hours on long flights and not get enough sleep.",
            "question_vi": "Là một tiếp viên hàng không là một công việc ______. Bạn có thể phải làm việc nhiều giờ trên các chuyến bay dài và không có đủ giấc ngủ.",
            "options": {
                "A": "tedious",
                "A_vi": "tẻ nhạt",
                "B": "rewarding",
                "B_vi": "đáng giá, bổ ích",
                "C": "fascinating",
                "C_vi": "hấp dẫn",
                "D": "demanding",
                "D_vi": "đòi hỏi cao"
            },
            "correct": "D",
            "explanation": "Demanding means requiring a lot of effort or time.",
            "explanation_vi": "Demanding có nghĩa là đòi hỏi nhiều nỗ lực hoặc thời gian."
        },
        60: {
            "question": "I studied languages ______ I could work abroad.",
            "question_vi": "Tôi đã học ngôn ngữ ______ tôi có thể làm việc ở nước ngoài.",
            "options": {
                "A": "so",
                "A_vi": "vì vậy",
                "B": "as",
                "B_vi": "như, bởi vì",
                "C": "if",
                "C_vi": "nếu",
                "D": "so that",
                "D_vi": "để mà"
            },
            "correct": "D",
            "explanation": "So that indicates purpose.",
            "explanation_vi": "So that chỉ mục đích."
        }
    }
}

# ========== CHUẨN BỊ DỮ LIỆU ==========
all_questions = []
for part_name, part_qs in questions_data.items():
    for q_id, q_data in part_qs.items():
        all_questions.append({
            "id": f"{part_name}_{q_id}",
            "part": part_name,
            "number": q_id,
            "question": q_data["question"],
            "question_vi": q_data.get("question_vi", ""),
            "options": {k: v for k, v in q_data["options"].items() if not k.endswith("_vi")},
            "options_vi": {k.replace("_vi", ""): v for k, v in q_data["options"].items() if k.endswith("_vi")},
            "correct": q_data["correct"],
            "explanation": q_data["explanation"],
            "explanation_vi": q_data.get("explanation_vi", "")
        })

# ========== TẠO 4 BỘ ĐỀ ==========
random.seed(42)
shuffled = all_questions.copy()
random.shuffle(shuffled)

decks = {}
for i in range(4):
    start_idx = i * 30
    end_idx = start_idx + 30
    decks[f"Đề {i+1}"] = shuffled[start_idx:end_idx]

# ========== GIAO DIỆN STREAMLIT ==========
st.set_page_config(page_title="Ôn tập tiếng Anh Bắc 2", layout="wide")
st.title("📚 Ôn tập tiếng Anh Bắc 2 - Sở Y tế Gia Lai 2025")

# Cài đặt ngôn ngữ
st.sidebar.header("Cài đặt hiển thị")
language_mode = st.sidebar.radio("Chế độ ngôn ngữ:", ["Tiếng Việt", "Song ngữ", "English"])

if language_mode == "Tiếng Việt":
    show_english = False
    show_vietnamese = True
elif language_mode == "Song ngữ":
    show_english = True
    show_vietnamese = True
else:
    show_english = True
    show_vietnamese = False

# Bộ lọc
st.sidebar.header("Lọc câu hỏi")
selected_part = st.sidebar.selectbox("Chọn phần:", ["Tất cả", "Part 1", "Part 2", "Part 3", "Part 4"])
search_term = st.sidebar.text_input("Tìm kiếm câu hỏi:")

tab1, tab2, tab3 = st.tabs(["📖 Toàn bộ câu hỏi", "🎯 4 Bộ đề ôn tập", "📊 Thống kê"])

with tab1:
    st.header("Toàn bộ 120 câu hỏi (4 phần)")
    
    # Lọc câu hỏi
    filtered_questions = all_questions
    if selected_part != "Tất cả":
        filtered_questions = [q for q in filtered_questions if q["part"] == selected_part]
    
    if search_term:
        filtered_questions = [q for q in filtered_questions 
                             if search_term.lower() in q["question"].lower() 
                             or search_term.lower() in q["question_vi"].lower()]
    
    st.write(f"**Tìm thấy {len(filtered_questions)} câu hỏi**")
    
    for idx, q in enumerate(filtered_questions, 1):
        with st.expander(f"{q['part']} - Câu {q['number']}: {q['question'][:50]}..."):
            # Hiển thị câu hỏi
            if show_english:
                st.write(f"**Câu hỏi (English):** {q['question']}")
            if show_vietnamese and q["question_vi"]:
                st.write(f"**Câu hỏi (Tiếng Việt):** {q['question_vi']}")
            
            # Hiển thị đáp án
            st.write("**Đáp án:**")
            for opt in ["A", "B", "C", "D"]:
                if opt in q["options"]:
                    col1, col2, col3 = st.columns([1, 4, 1])
                    with col1:
                        st.write(f"**{opt}:**")
                    with col2:
                        if show_english:
                            st.write(q["options"][opt])
                        if show_vietnamese and opt in q["options_vi"]:
                            st.write(q["options_vi"][opt])
                    with col3:
                        if opt == q["correct"]:
                            st.success("✓ Đúng")
                        else:
                            st.error("✗ Sai")
            
            # Hiển thị đáp án đúng
            st.success(f"**Đáp án đúng: {q['correct']}**")
            
            # Hiển thị giải thích
            if show_english:
                st.info(f"**Giải thích (English):** {q['explanation']}")
            if show_vietnamese:
                if q.get("explanation_vi"):
                    st.info(f"**Giải thích (Tiếng Việt):** {q['explanation_vi']}")
                else:
                    st.info(f"**Giải thích:** {q['explanation']}")

with tab2:
    st.header("4 Bộ đề ôn tập (mỗi đề 30 câu)")
    selected_deck = st.selectbox("Chọn bộ đề:", list(decks.keys()))
    
    if selected_deck:
        st.subheader(f"{selected_deck}")
        deck_questions = decks[selected_deck]
        
        # Tính điểm nếu người dùng làm bài
        st.write("**Làm bài trực tiếp:**")
        user_answers = {}
        score = 0
        
        for idx, q in enumerate(deck_questions, 1):
            st.write(f"**Câu {idx}:**")
            if show_english:
                st.write(q["question"])
            if show_vietnamese and q["question_vi"]:
                st.write(q["question_vi"])
            
            # Hiển thị options
            options = []
            option_texts = []
            for opt in ["A", "B", "C", "D"]:
                if opt in q["options"]:
                    text = q["options"][opt]
                    if show_vietnamese and opt in q["options_vi"]:
                        text += f" | {q['options_vi'][opt]}"
                    options.append(opt)
                    option_texts.append(text)
            
            user_answer = st.radio(f"Chọn đáp án cho câu {idx}:", options, 
                                  format_func=lambda x: f"{x}: {option_texts[options.index(x)]}", 
                                  key=f"deck_{selected_deck}_q{idx}")
            
            user_answers[idx] = user_answer
            
            # Kiểm tra đáp án
            if user_answer == q["correct"]:
                score += 1
        
        if st.button("Nộp bài và chấm điểm"):
            st.success(f"**Điểm của bạn: {score}/30 ({score/30*100:.1f}%)**")
            
            # Hiển thị kết quả chi tiết
            st.subheader("Kết quả chi tiết:")
            for idx, q in enumerate(deck_questions, 1):
                user_answer = user_answers.get(idx)
                correct = q["correct"]
                
                if user_answer == correct:
                    st.write(f"✅ **Câu {idx}:** Đúng. Đáp án của bạn: {user_answer}")
                else:
                    st.write(f"❌ **Câu {idx}:** Sai. Đáp án của bạn: {user_answer}, Đáp án đúng: {correct}")
                
                # Hiển thị giải thích
                with st.expander(f"Xem giải thích câu {idx}"):
                    if show_english:
                        st.info(f"**Giải thích:** {q['explanation']}")
                    if show_vietnamese and q.get("explanation_vi"):
                        st.info(f"**Giải thích:** {q['explanation_vi']}")

with tab3:
    st.header("Thống kê phân bổ câu hỏi")
    
    # Thống kê theo phần trong từng đề
    stats_data = []
    for deck_name, deck_questions in decks.items():
        part_counts = {}
        for q in deck_questions:
            part_counts[q["part"]] = part_counts.get(q["part"], 0) + 1
        
        for part in ["Part 1", "Part 2", "Part 3", "Part 4"]:
            stats_data.append({
                "Đề": deck_name,
                "Phần": part,
                "Số câu": part_counts.get(part, 0)
            })
    
    df = pd.DataFrame(stats_data)
    pivot_df = df.pivot(index="Phần", columns="Đề", values="Số câu").fillna(0)
    
    st.subheader("Phân bổ câu hỏi trong 4 bộ đề")
    st.dataframe(pivot_df.astype(int), use_container_width=True)
    
    # Tổng số câu
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Tổng số câu hỏi", len(all_questions))
    with col2:
        st.metric("Số câu mỗi đề", 30)
    with col3:
        st.metric("Số đề", 4)
    with col4:
        st.metric("Tổng câu trong 4 đề", 120)
    
    # Biểu đồ
    st.subheader("Biểu đồ phân bổ")
    chart_data = pivot_df.T
    st.bar_chart(chart_data)
    
    # Thống kê theo phần
    st.subheader("Tổng số câu theo phần")
    part_counts = {}
    for q in all_questions:
        part_counts[q["part"]] = part_counts.get(q["part"], 0) + 1
    
    part_df = pd.DataFrame({
        "Phần": list(part_counts.keys()),
        "Số câu": list(part_counts.values())
    })
    st.dataframe(part_df, use_container_width=True)

st.markdown("---")
st.caption("© 2025 Sở Y tế tỉnh Gia Lai - Hội đồng tuyển dụng viên chức ngành Y tế")
st.caption("Phiên bản 1.0 - Đầy đủ 120 câu hỏi và 4 bộ đề")