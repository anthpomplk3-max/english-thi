import streamlit as st
import random
import pandas as pd
import numpy as np
from itertools import chain

# ========== DỮ LIỆU BÀI ĐỌC CHO PART 2 ==========
reading_passages = {
    "Passage 1": {
        "content": """In the 1960s, The Beatles were probably the most famous pop group in the whole world. Since then, there have been a great many groups that have achieved enormous fame, so it is perhaps difficult now to imagine how sensational The Beatles were at that time. They were four boys from the north of England and none of them had any training in music. They started by performing and recording songs by black Americans and they had some success with these songs. Then they started writing their own songs and that was when they became really popular. The Beatles changed pop music. They were the first pop group to achieve great success from songs they had written themselves. After that it became common for groups and singers to write their own songs. The Beatles did not have a long career. Their first hit record was in 1963 and they split up in 1970. They stopped doing live performances in 1966 because it had become too dangerous for them – their fans were so excited that they surrounded them and tried to take their clothes as souvenirs! However, today some of their songs remain as famous as they were when they first came out. Throughout the world many people can sing part of a Beatles song if you ask them.""",
        "content_vi": """Vào những năm 1960, The Beatles có lẽ là nhóm nhạc pop nổi tiếng nhất trên toàn thế giới. Kể từ đó, đã có rất nhiều nhóm nhạc đạt được danh tiếng khổng lồ, vì vậy có lẽ bây giờ khó có thể tưởng tượng được The Beatles đã gây chấn động đến mức nào vào thời điểm đó. Họ là bốn chàng trai đến từ miền bắc nước Anh và không ai trong số họ được đào tạo về âm nhạc. Họ bắt đầu bằng việc biểu diễn và thu âm các bài hát của người Mỹ gốc Phi và đã có một số thành công với những bài hát này. Sau đó họ bắt đầu viết các bài hát của riêng mình và đó là khi họ trở nên thực sự nổi tiếng. The Beatles đã thay đổi nhạc pop. Họ là nhóm nhạc pop đầu tiên đạt được thành công lớn từ những bài hát do chính họ viết. Sau đó, việc các nhóm nhạc và ca sĩ tự viết bài hát của mình trở nên phổ biến. The Beatles không có sự nghiệp dài. Đĩa đơn hit đầu tiên của họ là vào năm 1963 và họ tan rã vào năm 1970. Họ ngừng biểu diễn trực tiếp vào năm 1966 vì nó đã trở nên quá nguy hiểm đối với họ - người hâm mộ của họ quá phấn khích đến mức bao vây họ và cố gắng lấy quần áo của họ làm đồ lưu niệm! Tuy nhiên, ngày nay một số bài hát của họ vẫn nổi tiếng như khi chúng mới ra mắt. Trên khắp thế giới, nhiều người có thể hát một phần bài hát của The Beatles nếu bạn yêu cầu họ.""",
        "questions": [1, 2, 3, 4, 5]
    },
    "Passage 2": {
        "content": """Orbis is an organization which helps blind people everywhere. It has built an eye hospital inside an aeroplane and flown it all over the world with an international medical team. Samantha Graham, a fourteen-year-old schoolgirl from England, went with the plane to Mongolia. Samantha tells a story of Eukhtuul, a young Mongolian girl.

"Last year, when Eukhtuul was walking from home, she was attacked by boys with sticks and her eyes were badly damaged. Dr. Duffrey, an Orbis doctor, said that without an operation she would never see again. I thought about all the everyday things I do that she couldn't, things like reading school books, watching television, seeing friends, and I realized how lucky I am."

"The Orbis team agreed to operate on Eukhtuul and I was allowed to watch, together with some Mongolian medical students. I prayed the operation would be successful. The next day, I sat nervously with Eukhtuul while Dr. Duffrey removed her bandages. In six months, your sight will back to normal," he said. Eukhtuul smiled, her mother cried, and I had to wipe away some tears, too!"

"Now Eukhtuul wants to study hard to become a doctor. Her whole future has changed, thanks to simple operation. We should all think more about how much our sight means to us." """,
        "content_vi": """Orbis là một tổ chức giúp đỡ người mù ở khắp mọi nơi. Họ đã xây dựng một bệnh viện mắt bên trong một chiếc máy bay và bay nó đi khắp thế giới với một đội ngũ y tế quốc tế. Samantha Graham, một nữ sinh 14 tuổi từ Anh, đã đi cùng chiếc máy bay đến Mông Cổ. Samantha kể câu chuyện về Eukhtuul, một cô gái trẻ Mông Cổ.

"Năm ngoái, khi Eukhtuul đang đi bộ từ nhà về, cô bị các cậu bé tấn công bằng gậy và đôi mắt của cô bị tổn thương nặng. Bác sĩ Duffrey, một bác sĩ của Orbis, nói rằng nếu không có phẫu thuật, cô sẽ không bao giờ nhìn thấy nữa. Tôi nghĩ về tất cả những việc hàng ngày tôi làm mà cô ấy không thể, những việc như đọc sách giáo khoa, xem tivi, gặp gỡ bạn bè, và tôi nhận ra mình may mắn thế nào."

"Đội Orbis đồng ý phẫu thuật cho Eukhtuul và tôi được phép xem, cùng với một số sinh viên y khoa Mông Cổ. Tôi cầu nguyện ca phẫu thuật sẽ thành công. Ngày hôm sau, tôi ngồi lo lắng bên Eukhtuul trong khi bác sĩ Duffrey tháo băng của cô. Sau sáu tháng, thị lực của em sẽ trở lại bình thường," ông nói. Eukhtuul mỉm cười, mẹ cô khóc, và tôi cũng phải lau đi một vài giọt nước mắt!"

"Bây giờ Eukhtuul muốn học tập chăm chỉ để trở thành bác sĩ. Toàn bộ tương lai của cô đã thay đổi, nhờ vào ca phẫu thuật đơn giản. Tất cả chúng ta nên suy nghĩ nhiều hơn về việc thị lực của chúng ta có ý nghĩa như thế nào đối với chúng ta." """,
        "questions": [6, 7, 8, 9, 10]
    },
    "Passage 3": {
        "content": """Did you know that on average we forget about 80% of the medical information a doctor might give us? This fascinating information came to light as a result of a study carried out by Utrecht University. What is even more interesting is that almost half of what we think we remember is wrong.

Why do you think this is? Well, it's not as complicated as you may think. You see, going to the doctor fills most people with anxiety and when we are really nervous and stressed we are more likely to focus on the diagnosis rather than the treatment. Therefore, we know what is wrong with us but have no idea what to do about it.

Here are some good tips to keep in mind when seeing a doctor. Always write down any important information. What would be even better is, if your doctor agreed, to record your consultation. This way, you can replay the advice at home, where you are more likely to absorb it. If you believe the situation is serious or you're really worried, seek the help of a family member. Just ask them to accompany you to listen in. This way you can be absolutely sure about what the doctor has told you and avoid falling into the same trap that most people do.""",
        "content_vi": """Bạn có biết rằng trung bình chúng ta quên khoảng 80% thông tin y tế mà bác sĩ có thể cung cấp cho chúng ta không? Thông tin thú vị này được tiết lộ nhờ một nghiên cứu được thực hiện bởi Đại học Utrecht. Điều thậm chí còn thú vị hơn là gần một nửa những gì chúng ta nghĩ rằng mình nhớ là sai.

Tại sao bạn nghĩ điều này xảy ra? Chà, nó không phức tạp như bạn nghĩ. Bạn thấy đấy, việc đi khám bác sĩ khiến hầu hết mọi người lo lắng và khi chúng ta thực sự lo lắng và căng thẳng, chúng ta có xu hướng tập trung vào chẩn đoán hơn là điều trị. Vì vậy, chúng ta biết điều gì sai với mình nhưng không biết phải làm gì với nó.

Dưới đây là một số mẹo hay cần ghi nhớ khi gặp bác sĩ. Luôn ghi chép bất kỳ thông tin quan trọng nào. Điều thậm chí còn tốt hơn là, nếu bác sĩ của bạn đồng ý, hãy ghi âm buổi tư vấn. Bằng cách này, bạn có thể phát lại lời khuyên ở nhà, nơi bạn có nhiều khả năng tiếp thu hơn. Nếu bạn tin rằng tình hình nghiêm trọng hoặc bạn thực sự lo lắng, hãy tìm kiếm sự giúp đỡ của một thành viên gia đình. Chỉ cần yêu cầu họ đi cùng bạn để lắng nghe. Bằng cách này, bạn có thể hoàn toàn chắc chắn về những gì bác sĩ đã nói với bạn và tránh rơi vào cái bẫy tương tự mà hầu hết mọi người mắc phải.""",
        "questions": [11, 12, 13, 14, 15]
    },
    "Passage 4": {
        "content": """Saving energy means saving money. Home owners and renters know this basic fact, but they often don't know what kinds of adjustments they can make in their homes and apartments that will result in savings.

For those willing to spend some time and money to reap long-term energy savings, an energy audit is the way to go. An energy auditor will come into your home and assess its energy efficiency. The auditor will pinpoint areas of your home that use the most energy and offer solutions to lower your energy use and costs. Trained energy auditors know what to look for and can locate a variety of flaws that may be resulting in energy inefficiency, including inadequate insulation, construction flaws, and uneven heat distribution.

There are quicker and less costly measures that can be taken as well. One way to save money is to replace incandescent lights with fluorescents. This can result in a savings of more than 50% on your monthly lighting costs.

When it's time to replace old appliances, it's wise to spend a bit more for an energy-efficient model, and be sure that you are taking advantage of energy-saving settings already on your current refrigerator, dishwasher, washing machine, or dryer.

Windows provide another opportunity to cut your energy costs. Caulk old Windows that might be leaky to prevent drafts, and choose double-paned windows if you're building an addition or replacing old windows.

Most areas of your home or apartment offer opportunities to save energy and money. The results are significant and are well worth the effort.""",
        "content_vi": """Tiết kiệm năng lượng có nghĩa là tiết kiệm tiền. Chủ nhà và người thuê nhà biết sự thật cơ bản này, nhưng họ thường không biết những loại điều chỉnh nào họ có thể thực hiện trong nhà và căn hộ của mình sẽ dẫn đến tiết kiệm.

Đối với những người sẵn sàng dành thời gian và tiền bạc để thu được khoản tiết kiệm năng lượng dài hạn, kiểm toán năng lượng là cách để thực hiện. Một kiểm toán viên năng lượng sẽ đến nhà bạn và đánh giá hiệu quả năng lượng của nó. Kiểm toán viên sẽ xác định các khu vực trong nhà bạn sử dụng nhiều năng lượng nhất và đề xuất giải pháp để giảm mức sử dụng và chi phí năng lượng của bạn. Các kiểm toán viên năng lượng được đào tạo biết phải tìm kiếm gì và có thể xác định vị trí nhiều lỗi có thể dẫn đến kém hiệu quả năng lượng, bao gồm cách nhiệt không đầy đủ, lỗi xây dựng và phân phối nhiệt không đều.

Cũng có những biện pháp nhanh hơn và ít tốn kém hơn có thể được thực hiện. Một cách để tiết kiệm tiền là thay thế đèn sợi đốt bằng đèn huỳnh quang. Điều này có thể giúp tiết kiệm hơn 50% chi phí chiếu sáng hàng tháng của bạn.

Khi đến lúc thay thế các thiết bị cũ, thật khôn ngoan khi chi thêm một chút cho một mẫu tiết kiệm năng lượng và đảm bảo rằng bạn đang tận dụng các cài đặt tiết kiệm năng lượng đã có trên tủ lạnh, máy rửa chén, máy giặt hoặc máy sấy hiện tại của bạn.

Cửa sổ cung cấp một cơ hội khác để cắt giảm chi phí năng lượng của bạn. Bít kín các cửa sổ cũ có thể bị rò rỉ để ngăn gió lùa và chọn cửa sổ hai lớp nếu bạn đang xây dựng phần mở rộng hoặc thay thế cửa sổ cũ.

Hầu hết các khu vực trong nhà hoặc căn hộ của bạn đều có cơ hội tiết kiệm năng lượng và tiền bạc. Kết quả là đáng kể và rất đáng để nỗ lực.""",
        "questions": [16, 17, 18, 19, 20]
    }
}

# ========== DỮ LIỆU CÂU HỎI & ĐÁP ÁN (120 câu) ==========
questions_data = {
    "Part 1": {
        1: {
            "question": "You should turn off the lights before going out, Mrs. Hoa said.",
            "options": {
                "A": "Mrs. Hoa told to turn off the lights before going out.",
                "B": "Mrs. Hoa suggested to turn off the lights before going out.",
                "C": "Mrs. Hoa suggested turning off the lights before going out.",
                "D": "Mrs. Hoa asked to us that we should turn off the lights before going out."
            },
            "correct": "C",
            "explanation": "Suggest + V-ing is the correct structure for giving advice."
        },
        2: {
            "question": "You won't have a seat unless you book in advance.",
            "options": {
                "A": "You won't have a seat if you don't book in advance.",
                "B": "You will have a seat if you don't book in advance.",
                "C": "You didn't have a seat because you didn't book in advance.",
                "D": "You can't have a seat although you book in advance."
            },
            "correct": "A",
            "explanation": "Unless = if not, so the meaning is the same."
        },
        3: {
            "question": "This is the first time I've made such a stupid mistake.",
            "options": {
                "A": "I had never made a stupid mistake.",
                "B": "I first made a stupid mistake.",
                "C": "Never before have I made such a stupid mistake.",
                "D": "The first mistake I made was a stupid one."
            },
            "correct": "C",
            "explanation": "Never before have I + past participle expresses the same meaning."
        },
        4: {
            "question": "He said: 'I bought these books last week'.",
            "options": {
                "A": "He said he had bought those books the week before.",
                "B": "He said he bought these books last week.",
                "C": "He said he had bought these books last week.",
                "D": "He said he bought these books the week before."
            },
            "correct": "A",
            "explanation": "In reported speech, tense changes (bought → had bought) and time expression changes (last week → the week before)."
        },
        5: {
            "question": "Mark can't wait to use his new computer-games console.",
            "options": {
                "A": "Mark is looking forward to using his new computer-games console.",
                "B": "Mark is not used to waiting for his new computer-games console.",
                "C": "Mark is patiently waiting to use his new computer-games console.",
                "D": "Mark is eagerly waiting to use his new computer-games console."
            },
            "correct": "A",
            "explanation": "Look forward to doing something expresses eagerness similar to can't wait to do something."
        },
        6: {
            "question": "Is it possible for me to come to your house at about 7p.m?",
            "options": {
                "A": "Must I come over to your house at about 7p.m?",
                "B": "Can I come to your house at about 7p.m?",
                "C": "Could I be come to your house at about 7p.m?",
                "D": "Will I come to your house at about 7p.m?"
            },
            "correct": "B",
            "explanation": "Can I is a polite way to ask for permission."
        },
        7: {
            "question": "The library stays open until seven o'clock.",
            "options": {
                "A": "The library doesn't close until seven o'clock.",
                "B": "Not until seven o'clock does the library open.",
                "C": "Not until seven o'clock the library doesn't close.",
                "D": "Not until seven o'clock does the library stay close."
            },
            "correct": "A",
            "explanation": "Stays open until means the same as doesn't close until."
        },
        8: {
            "question": "Although my father's always busy, he often helps me with my homework.",
            "options": {
                "A": "My father's always busy because he often helps me with my homework.",
                "B": "My father's always busy, and he often helps me with my homework.",
                "C": "My father's always busy, so he often helps me with my homework.",
                "D": "My father's always busy, but he often helps me with my homework."
            },
            "correct": "D",
            "explanation": "Although shows contrast, which can be replaced by but."
        },
        9: {
            "question": "We started cooking for the party four hours ago.",
            "options": {
                "A": "We began to cook for the party for four hours.",
                "B": "We have been cooked for the party for four hours.",
                "C": "We have been cooking for the party for four hours.",
                "D": "We cooked for the party four hours ago."
            },
            "correct": "C",
            "explanation": "The present perfect continuous tense indicates an action that started in the past and is still continuing."
        },
        10: {
            "question": "No one in the team can play better than John.",
            "options": {
                "A": "John as well as other players of the team plays very well.",
                "B": "John plays well but the others play better.",
                "C": "John is the best player of the team.",
                "D": "Everyone in the team, but John, plays very well."
            },
            "correct": "C",
            "explanation": "No one can play better than John means John is the best player."
        },
        11: {
            "question": "Sorry, I took you someone else.",
            "options": {
                "A": "Sorry, I thought you were somebody else.",
                "B": "Sorry, I made a mistake in taking you to someone else.",
                "C": "Sorry, I took you instead of somebody else.",
                "D": "Sorry, I asked somebody to take you."
            },
            "correct": "A",
            "explanation": "Took you for someone else means mistook you for someone else."
        },
        12: {
            "question": "Many think that Steve stole the money.",
            "options": {
                "A": "Steve is thought to have stolen the money.",
                "B": "The money is thought to be stolen by Steve.",
                "C": "It was not Steve who stole the money.",
                "D": "Many people think the money is stolen by Steve."
            },
            "correct": "A",
            "explanation": "Passive voice with infinitive perfect (to have stolen) for past action."
        },
        13: {
            "question": "I spent a long time getting over the disappointment of losing the match.",
            "options": {
                "A": "It took me long to forget the disappointment of losing the match.",
                "B": "It took me long to stop disappointing you.",
                "C": "Getting over the disappointment took me a long time than the match.",
                "D": "Losing the match disappointed me too much."
            },
            "correct": "A",
            "explanation": "Spent a long time getting over means it took a long time to forget."
        },
        14: {
            "question": "His eel soup is better than any other soups I have ever eaten.",
            "options": {
                "A": "Of all the soups I have ever eaten, his eel soup is the best.",
                "B": "I have ever eaten many soups that are better than his eel soup.",
                "C": "His eel soup is good but I have ever eaten many others better.",
                "D": "His eel soup is the worst of all soups I have eaten."
            },
            "correct": "A",
            "explanation": "Better than any other means the best among all."
        },
        15: {
            "question": "I haven't visited my hometown for a few years.",
            "options": {
                "A": "I last visited my hometown a few years ago.",
                "B": "I was in my hometown for a few years.",
                "C": "I didn't visit my hometown a few years ago.",
                "D": "I have been in my hometown for a few years."
            },
            "correct": "A",
            "explanation": "Haven't visited for a few years means the last visit was a few years ago."
        },
        16: {
            "question": "He couldn't stand being eliminated from the contest.",
            "options": {
                "A": "He didn't believe that he was thrown out from the contest.",
                "B": "Because he stood, he was eliminated from the contest.",
                "C": "He was eliminated from the contest because he was unable to stand.",
                "D": "He was unable to accept the failure in the contest."
            },
            "correct": "D",
            "explanation": "Couldn't stand means couldn't accept or tolerate."
        },
        17: {
            "question": "He sang very badly. Everyone left the room.",
            "options": {
                "A": "He sang so badly but everyone left the room.",
                "B": "He sang badly as a result of everyone leaving the room.",
                "C": "He sang very badly, so everyone left the room.",
                "D": "Everyone left the room, so he sang badly."
            },
            "correct": "C",
            "explanation": "The first sentence is the cause, the second is the result."
        },
        18: {
            "question": "Your birthday party was the last time I really enjoyed myself.",
            "options": {
                "A": "Your last birthday party wasn't really enjoyed to me.",
                "B": "I didn't really enjoy myself at your birthday party.",
                "C": "I haven't really enjoyed myself since your birthday party.",
                "D": "I haven't been to your birthday party lastly as I really enjoyed myself."
            },
            "correct": "C",
            "explanation": "The last time I enjoyed myself means I haven't enjoyed myself since then."
        },
        19: {
            "question": "I came back to my town last Sunday, said Mr. Pitt.",
            "options": {
                "A": "Mr. Pitt said that I had come back to his town the Sunday before.",
                "B": "Mr. Pitt said that he came back to his town the Sunday before.",
                "C": "Mr. Pitt said that I had come back to his town last Sunday.",
                "D": "Mr. Pitt said that he had come back to his town the Sunday before."
            },
            "correct": "D",
            "explanation": "Reported speech: tense change (came → had come) and time change (last Sunday → the Sunday before)."
        },
        20: {
            "question": "Nick is lazy, so he is punished.",
            "options": {
                "A": "Nick would not be punished if he were not lazy.",
                "B": "If Nick is not lazy, he would not be punished.",
                "C": "If Nick were lazy, he would be punished.",
                "D": "If Nick were not lazy, he would be punished."
            },
            "correct": "A",
            "explanation": "Second conditional for unreal present situation."
        }
    },
    "Part 2": {
        1: {
            "question": "The passage is mainly about ______",
            "options": {
                "A": "the Beatles' fame and success",
                "B": "how the Beatles became more successful than other groups",
                "C": "why the Beatles split up after 7 years",
                "D": "many people's ability to sing a Beatles song"
            },
            "correct": "A",
            "explanation": "The passage focuses on the Beatles' rise to fame, their impact on pop music, and their enduring legacy."
        },
        2: {
            "question": "The word 'sensational' is closest in meaning to ______",
            "options": {
                "A": "shocking",
                "B": "bad",
                "C": "notorious",
                "D": "popular"
            },
            "correct": "D",
            "explanation": "In this context, 'sensational' means causing great public interest and excitement."
        },
        3: {
            "question": "What is NOT TRUE about the Beatles?",
            "options": {
                "A": "They had a long stable career.",
                "B": "The members had no training in music.",
                "C": "They became famous when they wrote their own songs.",
                "D": "They changed pop music."
            },
            "correct": "A",
            "explanation": "The passage states that the Beatles did not have a long career (1963-1970)."
        },
        4: {
            "question": "The Beatles stopped their live performances because ______",
            "options": {
                "A": "They were afraid of being hurt by fans.",
                "B": "They did not want to work with each other.",
                "C": "They spent more time writing their own songs.",
                "D": "They had earned enough money."
            },
            "correct": "A",
            "explanation": "The text says it became too dangerous due to overexcited fans."
        },
        5: {
            "question": "The tone of the passage is that of ______",
            "options": {
                "A": "neutral",
                "B": "criticism",
                "C": "admiration",
                "D": "pleasant"
            },
            "correct": "C",
            "explanation": "The author admires the Beatles' achievements and impact."
        },
        6: {
            "question": "What is the writer's main purpose in writing the passage?",
            "options": {
                "A": "To describe a dangerous trip.",
                "B": "To explain how sight can be lost.",
                "C": "To warn against playing with sticks.",
                "D": "To report a patient's cure."
            },
            "correct": "D",
            "explanation": "The passage tells the story of Eukhtuul's successful eye operation."
        },
        7: {
            "question": "After meeting Eukhtuul, Samantha felt ______.",
            "options": {
                "A": "surprised by Eukhtuul's courage",
                "B": "grateful for her own sight",
                "C": "proud of the doctor's skill",
                "D": "angry about Eukhtuul's experience"
            },
            "correct": "B",
            "explanation": "Samantha realized how lucky she was to have her sight."
        },
        8: {
            "question": "What is the result of Eukhtuul's operation?",
            "options": {
                "A": "She can see better but won't have normal eyes.",
                "B": "She will need another operation.",
                "C": "She can already see perfectly again.",
                "D": "After some time she will see as well as before."
            },
            "correct": "D",
            "explanation": "The doctor said 'In six months, your sight will back to normal'."
        },
        9: {
            "question": "Which of the postcard Samantha wrote to an English friend?",
            "options": {
                "A": "Make sure you take care of your eyes because they're more valuable than you realize.",
                "B": "I'm staying with my friend Eukhtuul while I'm sightseeing in Mongolia.",
                "C": "You may have to fly a long way to have an operation you need, but the journey will be worth it.",
                "D": "I have visited a Mongolia and watched local doctors do an operation."
            },
            "correct": "A",
            "explanation": "The passage emphasizes the value of sight."
        },
        10: {
            "question": "What can a reader learn about in this passage?",
            "options": {
                "A": "The best way of studying medicine.",
                "B": "The international work of some eye doctors.",
                "C": "The difficulties of blind travelers.",
                "D": "The life of schoolchildren in Mongolia."
            },
            "correct": "B",
            "explanation": "The passage describes Orbis, an organization that helps blind people worldwide."
        },
        11: {
            "question": "According to the passage, the information doctors give us ______.",
            "options": {
                "A": "is mostly forgotten",
                "B": "is only 80% correct",
                "C": "is about 50% wrong",
                "D": "is usually not enough"
            },
            "correct": "A",
            "explanation": "The passage says we forget about 80% of medical information."
        },
        12: {
            "question": "The word 'complicated' in the passage is opposite in meaning to ______.",
            "options": {
                "A": "good",
                "B": "quick",
                "C": "short",
                "D": "simple"
            },
            "correct": "D",
            "explanation": "Complicated means complex, so simple is the opposite."
        },
        13: {
            "question": "The author says that when people consult a doctor, ______.",
            "options": {
                "A": "they usually have a family member with them",
                "B": "they are interested in knowing what they should do",
                "C": "they always believe that their situation is serious",
                "D": "they only want to know what is wrong with them"
            },
            "correct": "D",
            "explanation": "People focus on diagnosis rather than treatment when anxious."
        },
        14: {
            "question": "The word 'absorb' in the passage is closest in meaning to ______.",
            "options": {
                "A": "take in",
                "B": "inhale",
                "C": "swallow",
                "D": "digest"
            },
            "correct": "A",
            "explanation": "Absorb in this context means to take in or understand information."
        },
        15: {
            "question": "The author suggests recording the consultant in order to ______.",
            "options": {
                "A": "refer to it later to better understand your condition",
                "B": "play it to your family members to get their opinions",
                "C": "replay it to write down any important information",
                "D": "use it as evidence against your doctor if necessary"
            },
            "correct": "A",
            "explanation": "Recording helps you understand the advice better at home."
        },
        16: {
            "question": "Which two main organizational schemes can be identified in this passage?",
            "options": {
                "A": "order by topic and cause and effect",
                "B": "hierarchical order and order by topic",
                "C": "hierarchical order and chronological order",
                "D": "chronological order and compare and contrast"
            },
            "correct": "A",
            "explanation": "The passage discusses different topics (energy audits, appliances, windows) and cause-effect relationships."
        },
        17: {
            "question": "Which of the following ideas is NOT included in this passage?",
            "options": {
                "A": "Your local energy company will send an energy auditor at your request.",
                "B": "Double-paned windows can cut energy costs.",
                "C": "You can reduce your $130 monthly lighting costs to $65 by using fluorescent bulbs instead of incandescent.",
                "D": "Some appliances have energy-saving settings."
            },
            "correct": "C",
            "explanation": "The passage mentions saving 50% on lighting costs but doesn't give specific dollar amounts."
        },
        18: {
            "question": "Which of the following best expresses the main idea of this passage?",
            "options": {
                "A": "There are many things a homeowner or renter can do to save energy and money.",
                "B": "Hiring an energy auditor will save energy and money.",
                "C": "Homeowners and renters don't know what they can do to save energy and money.",
                "D": "Replacing windows and light bulbs are well worth the effort and cost."
            },
            "correct": "A",
            "explanation": "The main idea is that there are various ways to save energy and money at home."
        },
        19: {
            "question": "According to the passage, which of the following would an energy auditor NOT do?",
            "options": {
                "A": "Locate a variety of flaws that may result in energy inefficiency and fix them.",
                "B": "Look for problems with heat distribution.",
                "C": "Offer solutions to lower your energy costs.",
                "D": "Check for construction flaws."
            },
            "correct": "A",
            "explanation": "Auditors identify problems but don't fix them; they offer solutions."
        },
        20: {
            "question": "According the passage, double-paned windows",
            "options": {
                "A": "are energy efficient.",
                "B": "should only be used as replacement windows.",
                "C": "should only be used in new additions to homes.",
                "D": "will lower your heating costs by 50%."
            },
            "correct": "A",
            "explanation": "Double-paned windows are mentioned as energy-efficient."
        }
    },
    "Part 3": {
        1: {
            "question": "Society has changed in many ways (1)____ the introduction of computers, and people's lives at home and at the office have been affected.",
            "options": {
                "A": "for",
                "B": "from",
                "C": "at",
                "D": "since"
            },
            "correct": "D",
            "explanation": "Since indicates a point in time when the change started."
        },
        2: {
            "question": "Most people are working for fewer hours per week than they (2)____ to",
            "options": {
                "A": "want",
                "B": "used",
                "C": "ought",
                "D": "have"
            },
            "correct": "B",
            "explanation": "Used to refers to past habits."
        },
        3: {
            "question": "One recent report stated that (3)____ the number of hobbies had not increased, each hobby had become more specialized.",
            "options": {
                "A": "as",
                "B": "although",
                "C": "but",
                "D": "because of"
            },
            "correct": "B",
            "explanation": "Although shows contrast between two ideas."
        },
        4: {
            "question": "Nowadays, many managers would rather (4)____ time with their families than stay late in the office every day.",
            "options": {
                "A": "spending",
                "B": "spend",
                "C": "spent",
                "D": "to spend"
            },
            "correct": "B",
            "explanation": "Would rather is followed by a bare infinitive."
        },
        5: {
            "question": "Some companies now (5)____ managers take their annual holidays even if they don't want to",
            "options": {
                "A": "force",
                "B": "have",
                "C": "make",
                "D": "cause"
            },
            "correct": "C",
            "explanation": "Make someone do something means to force or cause someone to do something."
        },
        6: {
            "question": "But Percy soon showed a talent (6)______ business and made a fortune in the fur trade and auction business.",
            "options": {
                "A": "with",
                "B": "for",
                "C": "of",
                "D": "on"
            },
            "correct": "B",
            "explanation": "Talent for something is the correct preposition."
        },
        7: {
            "question": "Then disaster struck and he (7)______ all his money.",
            "options": {
                "A": "threw",
                "B": "sent",
                "C": "lost",
                "D": "wasted"
            },
            "correct": "C",
            "explanation": "Lost means no longer having something, especially money."
        },
        8: {
            "question": "But he soon made a fortune again - this time by (8)______ plastic bags.",
            "options": {
                "A": "manufacturer",
                "B": "manufactured",
                "C": "manufacturing",
                "D": "manufacture"
            },
            "correct": "C",
            "explanation": "By + V-ing indicates the means or method."
        },
        9: {
            "question": "After these first experiences of giving money away, Ross decided to do it on a (9)______ basis.",
            "options": {
                "A": "regular",
                "B": "frequent",
                "C": "occasional",
                "D": "usual"
            },
            "correct": "A",
            "explanation": "On a regular basis means regularly or consistently."
        },
        10: {
            "question": "It took years, but Ross finally (10)______ in giving away his entire fortune.",
            "options": {
                "A": "interested",
                "B": "succeeded",
                "C": "invested",
                "D": "tried"
            },
            "correct": "B",
            "explanation": "Succeed in doing something means to achieve the desired aim."
        },
        11: {
            "question": "The issue is whether this technological innovation has (11)______ more harm than good.",
            "options": {
                "A": "brought",
                "B": "played",
                "C": "made",
                "D": "done"
            },
            "correct": "A",
            "explanation": "Bring harm is a common collocation."
        },
        12: {
            "question": "In order to (12)______ the question, we must first turn to the types of consumers.",
            "options": {
                "A": "answer",
                "B": "address",
                "C": "remedy",
                "D": "put right"
            },
            "correct": "B",
            "explanation": "Address a question means to deal with or discuss it."
        },
        13: {
            "question": "Presumably, most parents (13)______ are always worrying about their children's safety buy mobile phones for them to track their whereabouts.",
            "options": {
                "A": "what",
                "B": "whom",
                "C": "which",
                "D": "who"
            },
            "correct": "D",
            "explanation": "Who is used for people as the subject of the relative clause."
        },
        14: {
            "question": "(14)______, we cannot deny the fact that text messages have been used by bullies to intimidate fellow students.",
            "options": {
                "A": "Therefore",
                "B": "Moreover",
                "C": "However",
                "D": "So that"
            },
            "correct": "C",
            "explanation": "However introduces a contrasting idea."
        },
        15: {
            "question": "There is also (15)______ evidence that texting has affected literacy skills.",
            "options": {
                "A": "indisputable",
                "B": "arguable",
                "C": "doubtless",
                "D": "unhesitating"
            },
            "correct": "A",
            "explanation": "Indisputable evidence means evidence that cannot be doubted."
        },
        16: {
            "question": "(16)______ breakfast Americans will eat cereal with milk which are often mixed (17)______ in a bowl, a glass of orange juice, and toasted bread or muffin with jam, butter, or margarine.",
            "options": {
                "A": "With",
                "B": "In",
                "C": "At",
                "D": "For"
            },
            "correct": "D",
            "explanation": "For breakfast means as part of the morning meal."
        },
        17: {
            "question": "cereal with milk which are often mixed (17)______ in a bowl",
            "options": {
                "A": "others",
                "B": "each other",
                "C": "one another",
                "D": "together"
            },
            "correct": "D",
            "explanation": "Mixed together means combined into one mixture."
        },
        18: {
            "question": "People who are on (18)______ eat just a cup of yogurt.",
            "options": {
                "A": "diet",
                "B": "holiday",
                "C": "engagement",
                "D": "duty"
            },
            "correct": "A",
            "explanation": "On a diet means following a special eating plan."
        },
        19: {
            "question": "Lunch and dinner are more (19)______.",
            "options": {
                "A": "varied",
                "B": "vary",
                "C": "variety",
                "D": "variously"
            },
            "correct": "A",
            "explanation": "More varied means having greater diversity."
        },
        20: {
            "question": "Most Americans do not know the answer (20)______.",
            "options": {
                "A": "either",
                "B": "too",
                "C": "so",
                "D": "neither"
            },
            "correct": "A",
            "explanation": "Either is used in negative sentences to mean also."
        }
    },
    "Part 4": {
        1: {"question": "I ______ my sister in December as planned.", "options": {"A": "will see", "B": "have seen", "C": "am going to see", "D": "see"}, "correct": "C", "explanation": "Be going to is used for plans and intentions."},
        2: {"question": "He seems quite ______ with his new job.", "options": {"A": "satisfied", "B": "satisfy", "C": "satisfying", "D": "satisfies"}, "correct": "A", "explanation": "After 'seem', we use an adjective. 'Satisfied' describes how he feels."},
        3: {"question": "- 'How was the game show last night?' - '______'", "options": {"A": "Great. I gained more knowledge about biology.", "B": "Just talking about it.", "C": "It showed at 8 o'clock.", "D": "I think it wasn't a good game."}, "correct": "A", "explanation": "This is an appropriate response to a question about a game show's quality."},
        4: {"question": "Internet cafes allow you ______ your web-based email account.", "options": {"A": "be accessed", "B": "accessing", "C": "access", "D": "to access"}, "correct": "D", "explanation": "'Allow someone to do something' is the correct structure."},
        5: {"question": "- Where is Jimmy? - He is ______ work. He is busy ______ his monthly report.", "options": {"A": "in / about", "B": "at / with", "C": "to / through", "D": "on / for"}, "correct": "B", "explanation": "'At work' means at the workplace. 'Busy with something' is the correct preposition."},
        6: {"question": "Are you looking forward ______ on your vacation?", "options": {"A": "going", "B": "to going", "C": "to go", "D": "you go"}, "correct": "B", "explanation": "Look forward to + V-ing is the correct structure."},
        7: {"question": "______ is the controller of the body.", "options": {"A": "Nervous System", "B": "Digestive System", "C": "Skeletal System", "D": "Circulatory System"}, "correct": "A", "explanation": "The nervous system controls body functions."},
        8: {"question": "It is thought that Google ______ cars may transform the way we move around cities in the future.", "options": {"A": "motionless", "B": "driver", "C": "driverless", "D": "driving"}, "correct": "C", "explanation": "Driverless cars are autonomous vehicles."},
        9: {"question": "Do you get ______ if your parents ask you to help out in your free time?", "options": {"A": "boring", "B": "exciting", "C": "annoyed", "D": "annoying"}, "correct": "C", "explanation": "Get annoyed means become irritated or angry."},
        10: {"question": "I ______ buy a new car, so I'm saving as much money as possible.", "options": {"A": "am going to", "B": "will be", "C": "can", "D": "will"}, "correct": "A", "explanation": "Be going to indicates a planned future action."},
        11: {"question": "YouTube ______ to become the world most popular video-sharing website since 2005.", "options": {"A": "grows", "B": "grew", "C": "have grown", "D": "has grown"}, "correct": "D", "explanation": "Since 2005 requires present perfect tense. YouTube is singular."},
        12: {"question": "We are talking about the writer ______ latest book is one of the best-sellers this year.", "options": {"A": "whom", "B": "who", "C": "whose", "D": "which"}, "correct": "C", "explanation": "Whose shows possession (the writer's latest book)."},
        13: {"question": "Your job is likely to include welcoming guests and receiving ______ for our Charity Centre.", "options": {"A": "donated", "B": "donate", "C": "donors", "D": "donations"}, "correct": "D", "explanation": "Receiving donations means accepting gifts or contributions."},
        14: {"question": "______ is the member of a family who earns the money that the family needs.", "options": {"A": "Homemaker", "B": "Husband", "C": "Women", "D": "Breadwinner"}, "correct": "D", "explanation": "Breadwinner is the person who earns money to support the family."},
        15: {"question": "If you ______ the doctor's advice, you won't get well.", "options": {"A": "don't listen", "B": "take", "C": "ignore", "D": "follow"}, "correct": "C", "explanation": "Ignore means to pay no attention to something."},
        16: {"question": "The father typically works outside the home while the mother is ______ domestic duties such as homemaking and raising children.", "options": {"A": "aware of", "B": "capable of", "C": "suitable for", "D": "responsible for"}, "correct": "D", "explanation": "Responsible for means having the duty of doing something."},
        17: {"question": "The more polite you appear to be, ______ your partner will be.", "options": {"A": "the happiest", "B": "the more happily", "C": "the happier", "D": "the most happily"}, "correct": "C", "explanation": "The + comparative adjective... the + comparative adjective structure."},
        18: {"question": "John made me ______ a lot with his hilarious jokes.", "options": {"A": "laugh", "B": "laughed", "C": "laughing", "D": "to laugh"}, "correct": "A", "explanation": "Make + someone + bare infinitive (without to)."},
        19: {"question": "Only humans produce ______ tears.", "options": {"A": "false", "B": "emotional", "C": "crocodile", "D": "feel"}, "correct": "B", "explanation": "Emotional tears are tears caused by emotions."},
        20: {"question": "Treat others the way you want ______", "options": {"A": "to treat", "B": "to be treat", "C": "to be treated", "D": "treating"}, "correct": "C", "explanation": "Passive infinitive (to be treated) is needed because you want to receive the treatment."},
        21: {"question": "Her husband is very kind. He always cares about her and never puts all of the housework ______ her.", "options": {"A": "in", "B": "on", "C": "about", "D": "with"}, "correct": "B", "explanation": "Put something on someone means to make someone responsible for something."},
        22: {"question": "Don't phone me between 6.00 and 9.00 tonight. I ______ then.", "options": {"A": "will study", "B": "am studying", "C": "will be studying", "D": "study"}, "correct": "C", "explanation": "Future continuous tense for an action in progress at a specific future time."},
        23: {"question": "American Idol began in 2002, ______ quickly became the most popular entertainment series with viewers in the hundreds of millions.", "options": {"A": "so", "B": "but", "C": "or", "D": "and"}, "correct": "D", "explanation": "And connects two related ideas."},
        24: {"question": "After eating dinner, I have to do the ______ and then do my homework every day.", "options": {"A": "wash-up", "B": "washing-ups", "C": "washing-up", "D": "washings-up"}, "correct": "C", "explanation": "Washing-up means washing dishes after a meal."},
        25: {"question": "He asked me why ______ to the meeting.", "options": {"A": "you didn't come", "B": "I hadn't come", "C": "didn't I come", "D": "don't I come"}, "correct": "B", "explanation": "Reported question: why + subject + verb (past perfect for past action)."},
        26: {"question": "I'm responsible for cooking dinner as my mother usually works ______.", "options": {"A": "lately", "B": "later", "C": "early", "D": "late"}, "correct": "D", "explanation": "Work late means work until late in the day."},
        27: {"question": "He passed his exams ______.", "options": {"A": "successes", "B": "successful", "C": "successfully", "D": "success"}, "correct": "C", "explanation": "Adverb (successfully) modifies the verb (passed)."},
        28: {"question": "All forms of discrimination against all women and girls ______ immediately everywhere.", "options": {"A": "must be taken away", "B": "must be followed", "C": "must be allowed", "D": "must be ended"}, "correct": "D", "explanation": "End discrimination means stop discrimination."},
        29: {"question": "Paddle-wheel machine helps to clean the wastewater before ______ it for farming.", "options": {"A": "recycling", "B": "reducing", "C": "rearranging", "D": "reusing"}, "correct": "D", "explanation": "Reusing means using again."},
        30: {"question": "Today my mother can't help ______ the cooking because she is ill.", "options": {"A": "for", "B": "with", "C": "of", "D": "in"}, "correct": "B", "explanation": "Help with something means assist in doing something."},
        31: {"question": "My teacher assigned us a writing task about ______ of our favorite singers.", "options": {"A": "biography", "B": "biodiversity", "C": "biology", "D": "biochemist"}, "correct": "A", "explanation": "Biography is the story of a person's life."},
        32: {"question": "I'd like ______ all of you to enjoy my party on this Friday.", "options": {"A": "inviting", "B": "invite", "C": "not invite", "D": "to invite"}, "correct": "D", "explanation": "Would like + to + infinitive."},
        33: {"question": "Volunteers become well ______ of the problems facing the world.", "options": {"A": "concerned", "B": "interested", "C": "aware", "D": "helpful"}, "correct": "C", "explanation": "Become aware of means become conscious of."},
        34: {"question": "They had a global ______ hit with their album concept about 'The dark side of the Moon'.", "options": {"A": "top", "B": "popular", "C": "smash", "D": "song"}, "correct": "C", "explanation": "Smash hit means a very successful song or performance."},
        35: {"question": "My parents let my sister ______ camping with her friends in the mountain.", "options": {"A": "to go", "B": "going", "C": "not go", "D": "go"}, "correct": "D", "explanation": "Let + someone + bare infinitive (without to)."},
        36: {"question": "Maria: 'Thanks for the lovely evening.' Diana: '______.'", "options": {"A": "Oh, that's right", "B": "I'm glad you enjoyed it", "C": "Yes, it's really great John", "D": "No, it's not good"}, "correct": "B", "explanation": "Appropriate response to thanks for an event."},
        37: {"question": "- 'What are you arguing about?' - '______'", "options": {"A": "Well, I think she's right.", "B": "That doesn't matter.", "C": "Nothing.", "D": "Yes, we are"}, "correct": "C", "explanation": "Common response to avoid discussing the argument."},
        38: {"question": "Their massive salaries let them afford to give ______ huge amounts to charities.", "options": {"A": "hack", "B": "off", "C": "away", "D": "up"}, "correct": "C", "explanation": "Give away means donate or give for free."},
        39: {"question": "I was enjoying my book, but I stopped ______ a program on TV.", "options": {"A": "reading to watch", "B": "reading for to watch", "C": "to read to watch", "D": "to read for watching"}, "correct": "A", "explanation": "Stop + V-ing + to + V means cease one activity to start another."},
        40: {"question": "It is ______ to work in this city with so much noise and pollution.", "options": {"A": "health", "B": "healthy", "C": "healthful", "D": "unhealthy"}, "correct": "D", "explanation": "Unhealthy means not good for health."},
        41: {"question": "Hoang ______ his email four times a week in order not to miss anything important.", "options": {"A": "is checking", "B": "will check", "C": "checks", "D": "check"}, "correct": "C", "explanation": "Present simple for habitual actions."},
        42: {"question": "Van Cao is one of the most well-known ______ in Viet Nam.", "options": {"A": "singers", "B": "musicians", "C": "authors", "D": "actors"}, "correct": "B", "explanation": "Van Cao is a famous composer (musician)."},
        43: {"question": "These games are challenging, ______ it's not easy to spend little time playing them.", "options": {"A": "so", "B": "and", "C": "for", "D": "or"}, "correct": "A", "explanation": "So shows result or consequence."},
        44: {"question": "Mrs. Huyen is ______ with what her son did.", "options": {"A": "disappointed", "B": "disappoint", "C": "disappointment", "D": "disappointing"}, "correct": "A", "explanation": "Be disappointed with something means feel unhappy because something is not as good as expected."},
        45: {"question": "I am going to have a short rest as I ______ a headache.", "options": {"A": "feel", "B": "have", "C": "suffer", "D": "take"}, "correct": "B", "explanation": "Have a headache is the common expression."},
        46: {"question": "Only the best ______ is recruited.", "options": {"A": "employee", "B": "application", "C": "candidate", "D": "CV"}, "correct": "C", "explanation": "Candidate is a person who applies for a job."},
        47: {"question": "He was offered the job despite his poor ______.", "options": {"A": "qualifications", "B": "achievements", "C": "preparations", "D": "expressions"}, "correct": "A", "explanation": "Qualifications refer to skills, education, or experience."},
        48: {"question": "The cashiers were asked to watch out ______ forged banknotes.", "options": {"A": "for", "B": "on", "C": "to", "D": "with"}, "correct": "A", "explanation": "Watch out for means be alert to danger."},
        49: {"question": "A skilled ______ will help candidates feel relaxed.", "options": {"A": "interviewing", "B": "interviewee", "C": "interviewer", "D": "interview"}, "correct": "C", "explanation": "Interviewer is the person who asks questions in an interview."},
        50: {"question": "He behaved ______ nothing had happened.", "options": {"A": "if", "B": "as if", "C": "before", "D": "because"}, "correct": "B", "explanation": "As if introduces a manner clause suggesting something unreal."},
        51: {"question": "After working at the same company for thirty years, my grandfather was looking forward to his ______.", "options": {"A": "charity", "B": "pension", "C": "allowance", "D": "overtime"}, "correct": "B", "explanation": "Pension is money paid regularly to a retired person."},
        52: {"question": "After three years working hard, he was ______.", "options": {"A": "advanced", "B": "raised", "C": "promoted", "D": "elevated"}, "correct": "C", "explanation": "Promoted means given a higher position or rank."},
        53: {"question": "People usually use more ______ language when they're in serious situations like interviews.", "options": {"A": "serious", "B": "solemn", "C": "formal", "D": "informal"}, "correct": "C", "explanation": "Formal language is used in official or serious contexts."},
        54: {"question": "He has all the right ______ for the job.", "options": {"A": "degrees", "B": "certificates", "C": "qualifications", "D": "diplomas"}, "correct": "C", "explanation": "Qualifications include skills, knowledge, and experience."},
        55: {"question": "Mary: 'I've made a lot of new friends.' Mary's mother: '______'", "options": {"A": "You are doing so well, dear.", "B": "I can't agree more with yours.", "C": "I feel so sorry for you, my girl.", "D": "You can never understand, dear."}, "correct": "A", "explanation": "Positive and encouraging response."},
        56: {"question": "The chairman didn't make any ______ upon the matter.", "options": {"A": "evaluation", "B": "investment", "C": "opinion", "D": "comment"}, "correct": "D", "explanation": "Make a comment on something is a common phrase."},
        57: {"question": "Don't you think you should apply for the job ______ writing?", "options": {"A": "at", "B": "with", "C": "in", "D": "for"}, "correct": "C", "explanation": "In writing means in written form."},
        58: {"question": "Finding a job in this time of economic crisis is becoming ______", "options": {"A": "as more difficult than", "B": "more difficult than", "C": "more and more difficult", "D": "more than difficult"}, "correct": "C", "explanation": "More and more difficult indicates increasing difficulty."},
        59: {"question": "Being a flight attendant is a ______ job. You may have to work long hours on long flights and not get enough sleep.", "options": {"A": "tedious", "B": "rewarding", "C": "fascinating", "D": "demanding"}, "correct": "D", "explanation": "Demanding means requiring a lot of effort or time."},
        60: {"question": "I studied languages ______ I could work abroad.", "options": {"A": "so", "B": "as", "C": "if", "D": "so that"}, "correct": "D", "explanation": "So that indicates purpose."}
    }
}

# ========== CHUẨN BỊ DỮ LIỆU CƠ BẢN ==========
all_questions = []
for part_name, part_qs in questions_data.items():
    for q_id, q_data in part_qs.items():
        all_questions.append({
            "id": f"{part_name}_{q_id}",
            "part": part_name,
            "number": q_id,
            "question": q_data["question"],
            "options": q_data["options"],
            "correct": q_data["correct"],
            "explanation": q_data["explanation"]
        })

# ========== TẠO 10 BỘ ĐỀ VỚI HOÁN ĐỔI ==========
def shuffle_question_options(question):
    """Trảo đổi thứ tự đáp án và cập nhật đáp án đúng"""
    options = question["options"]
    option_keys = list(options.keys())
    option_values = list(options.values())
    
    # Tạo hoán vị ngẫu nhiên
    permutation = list(range(len(option_keys)))
    random.shuffle(permutation)
    
    # Tạo ánh xạ từ cũ sang mới
    new_keys = ["A", "B", "C", "D"][:len(option_keys)]
    old_to_new = {option_keys[i]: new_keys[permutation[i]] for i in range(len(option_keys))}
    new_to_old = {new_keys[permutation[i]]: option_keys[i] for i in range(len(option_keys))}
    
    # Tạo options mới
    new_options = {}
    for i, idx in enumerate(permutation):
        new_options[new_keys[i]] = option_values[idx]
    
    # Cập nhật đáp án đúng
    new_correct = old_to_new[question["correct"]]
    
    return {
        **question,
        "options": new_options,
        "correct": new_correct,
        "original_correct": question["correct"],  # Lưu đáp án gốc để hiển thị giải thích
        "mapping": new_to_old  # Ánh xạ để hiển thị giải thích đúng
    }

def create_exam(exam_num):
    """Tạo một đề thi với hoán đổi câu hỏi và đáp án"""
    random.seed(exam_num)  # Mỗi đề có seed khác nhau
    
    # 1. Tách Part 2 (câu đọc hiểu)
    part2_questions = [q for q in all_questions if q["part"] == "Part 2"]
    other_questions = [q for q in all_questions if q["part"] != "Part 2"]
    
    # 2. Xáo trộn câu hỏi Part 1, 3, 4
    random.shuffle(other_questions)
    
    # 3. Xử lý Part 2: Giữ nguyên thứ tự câu trong bài đọc, nhưng tráo đáp án
    # Nhóm câu hỏi theo bài đọc
    passage_groups = {}
    for passage_name, passage_data in reading_passages.items():
        question_ids = passage_data["questions"]
        passage_questions = [q for q in part2_questions if q["number"] in question_ids]
        # Sắp xếp theo thứ tự câu hỏi trong bài đọc
        passage_questions.sort(key=lambda x: question_ids.index(x["number"]))
        passage_groups[passage_name] = passage_questions
    
    # Xáo trộn thứ tự các bài đọc
    passage_names = list(passage_groups.keys())
    random.shuffle(passage_names)
    
    # 4. Tráo đáp án cho tất cả câu hỏi
    shuffled_other = [shuffle_question_options(q) for q in other_questions]
    
    shuffled_part2 = []
    for passage_name in passage_names:
        passage_questions = passage_groups[passage_name]
        shuffled_passage = [shuffle_question_options(q) for q in passage_questions]
        shuffled_part2.extend(shuffled_passage)
    
    # 5. Kết hợp tất cả câu hỏi
    exam_questions = shuffled_other + shuffled_part2
    
    # Đánh số lại câu hỏi từ 1 đến 120
    for i, q in enumerate(exam_questions, 1):
        q["exam_number"] = i
    
    return exam_questions, passage_names

# Tạo 10 đề thi
exams = {}
for i in range(1, 11):
    exam_questions, passage_order = create_exam(i)
    exams[f"Đề {i}"] = {
        "questions": exam_questions,
        "passage_order": passage_order
    }

# ========== GIAO DIỆN STREAMLIT ==========
st.set_page_config(page_title="Ôn tập tiếng Anh Bắc 2 - 10 Đề", layout="wide")
st.title("📚 10 Bộ Đề Thi Tiếng Anh Bắc 2 - Sở Y tế Gia Lai 2025")

# Cài đặt sidebar
st.sidebar.header("⚙️ Cài đặt hiển thị")
language = st.sidebar.radio("Ngôn ngữ:", ["Tiếng Việt", "Song ngữ", "English"])
show_explanation = st.sidebar.checkbox("Hiển thị giải thích đáp án", value=True)
show_passage = st.sidebar.checkbox("Hiển thị bài đọc Part 2", value=True)

if language == "Tiếng Việt":
    show_vi = True
    show_en = False
elif language == "Song ngữ":
    show_vi = True
    show_en = True
else:
    show_vi = False
    show_en = True

# Chọn đề
st.sidebar.header("📝 Chọn đề thi")
selected_exam = st.sidebar.selectbox("Chọn đề:", list(exams.keys()))

# Chế độ xem
view_mode = st.sidebar.radio("Chế độ xem:", ["Xem toàn bộ đề", "Làm bài trực tiếp"])

# Hiển thị thông tin đề
st.header(f"{selected_exam}")
st.info(f"Đề thi gồm 120 câu: Part 1 (20 câu), Part 2 (20 câu), Part 3 (20 câu), Part 4 (60 câu)")

if selected_exam:
    exam_data = exams[selected_exam]
    exam_questions = exam_data["questions"]
    passage_order = exam_data["passage_order"]
    
    if view_mode == "Xem toàn bộ đề":
        # Hiển thị toàn bộ đề
        user_answers = {}
        
        # Tạo form cho toàn bộ đề
        with st.form("exam_form"):
            current_passage = None
            passage_index = 0
            
            for i, q in enumerate(exam_questions, 1):
                # Kiểm tra nếu là câu Part 2 và cần hiển thị bài đọc
                if q["part"] == "Part 2":
                    # Tìm bài đọc chứa câu hỏi này
                    for passage_name in passage_order:
                        passage_data = reading_passages[passage_name]
                        if q["number"] in passage_data["questions"]:
                            if current_passage != passage_name and show_passage:
                                st.subheader(f"📖 Bài đọc: {passage_name}")
                                if show_en:
                                    st.markdown(f"**Bài đọc (English):**")
                                    st.write(passage_data["content"])
                                if show_vi:
                                    st.markdown(f"**Bài đọc (Tiếng Việt):**")
                                    st.write(passage_data["content_vi"])
                                st.markdown("---")
                                current_passage = passage_name
                            break
                
                # Hiển thị câu hỏi
                st.markdown(f"**Câu {i} ({q['part']} - Câu {q['number']}):**")
                st.write(q["question"])
                
                # Hiển thị đáp án
                options = q["options"]
                user_answer = st.radio(
                    f"Chọn đáp án cho câu {i}:",
                    options=list(options.keys()),
                    format_func=lambda x: f"{x}. {options[x]}",
                    key=f"q_{i}"
                )
                user_answers[i] = user_answer
                
                st.markdown("---")
            
            submitted = st.form_submit_button("Nộp bài và xem kết quả")
        
        if submitted:
            # Tính điểm
            score = sum(1 for i, q in enumerate(exam_questions, 1) 
                       if user_answers.get(i) == q["correct"])
            
            st.success(f"**Điểm của bạn: {score}/120 ({score/120*100:.1f}%)**")
            
            # Hiển thị kết quả chi tiết
            st.subheader("📊 Kết quả chi tiết")
            for i, q in enumerate(exam_questions, 1):
                user_answer = user_answers.get(i)
                correct = q["correct"]
                
                col1, col2 = st.columns([3, 1])
                with col1:
                    if user_answer == correct:
                        st.write(f"✅ **Câu {i}:** Đúng")
                    else:
                        st.write(f"❌ **Câu {i}:** Sai")
                
                with col2:
                    if user_answer == correct:
                        st.success(f"Đáp án: {correct}")
                    else:
                        st.error(f"Đáp án của bạn: {user_answer}, Đáp án đúng: {correct}")
                
                # Hiển thị giải thích nếu được chọn
                if show_explanation:
                    with st.expander(f"Xem giải thích câu {i}"):
                        # Hiển thị đáp án gốc để giải thích
                        original_correct = q.get("original_correct", q["correct"])
                        mapping = q.get("mapping", {})
                        if mapping:
                            # Ánh xạ ngược để lấy đáp án gốc cho giải thích
                            original_for_explanation = mapping.get(original_correct, original_correct)
                            st.info(f"**Đáp án đúng (trong đề gốc): {original_for_explanation}**")
                        st.write(f"**Giải thích:** {q['explanation']}")
                
                st.markdown("---")
    
    else:  # Làm bài trực tiếp
        st.warning("Chế độ làm bài trực tiếp: Trả lời từng câu và xem kết quả ngay")
        
        # Chọn câu hỏi để làm
        question_num = st.slider("Chọn câu hỏi:", 1, 120, 1)
        
        q = exam_questions[question_num - 1]
        
        # Kiểm tra nếu là câu Part 2 và cần hiển thị bài đọc
        if q["part"] == "Part 2" and show_passage:
            # Tìm bài đọc chứa câu hỏi này
            for passage_name in passage_order:
                passage_data = reading_passages[passage_name]
                if q["number"] in passage_data["questions"]:
                    st.subheader(f"📖 Bài đọc: {passage_name}")
                    if show_en:
                        st.markdown(f"**Bài đọc (English):**")
                        st.write(passage_data["content"])
                    if show_vi:
                        st.markdown(f"**Bài đọc (Tiếng Việt):**")
                        st.write(passage_data["content_vi"])
                    st.markdown("---")
                    break
        
        # Hiển thị câu hỏi
        st.markdown(f"**Câu {question_num} ({q['part']} - Câu {q['number']}):**")
        st.write(q["question"])
        
        # Tạo options cho radio button
        options = q["options"]
        user_answer = st.radio(
            f"Chọn đáp án:",
            options=list(options.keys()),
            format_func=lambda x: f"{x}. {options[x]}",
            key=f"live_q_{question_num}"
        )
        
        # Kiểm tra đáp án
        if st.button("Kiểm tra đáp án"):
            if user_answer == q["correct"]:
                st.success(f"✅ **Chính xác!** Đáp án đúng là {q['correct']}")
            else:
                st.error(f"❌ **Sai rồi!** Đáp án của bạn: {user_answer}, Đáp án đúng: {q['correct']}")
            
            # Hiển thị giải thích
            if show_explanation:
                st.info(f"**Giải thích:** {q['explanation']}")

# ========== THỐNG KÊ ==========
st.sidebar.header("📊 Thống kê")
if st.sidebar.button("Xem thống kê các đề"):
    st.subheader("📈 Thống kê phân bổ câu hỏi trong 10 đề")
    
    stats_data = []
    for exam_name, exam_data in exams.items():
        part_counts = {"Part 1": 0, "Part 2": 0, "Part 3": 0, "Part 4": 0}
        for q in exam_data["questions"]:
            part_counts[q["part"]] += 1
        
        stats_data.append({
            "Đề": exam_name,
            "Part 1": part_counts["Part 1"],
            "Part 2": part_counts["Part 2"],
            "Part 3": part_counts["Part 3"],
            "Part 4": part_counts["Part 4"],
            "Tổng": 120
        })
    
    df = pd.DataFrame(stats_data)
    st.dataframe(df, use_container_width=True)
    
    # Hiển thị thứ tự bài đọc trong mỗi đề
    st.subheader("📖 Thứ tự bài đọc Part 2 trong các đề")
    for exam_name, exam_data in exams.items():
        st.write(f"**{exam_name}:** {', '.join(exam_data['passage_order'])}")

# ========== HƯỚNG DẪN ==========
st.sidebar.header("📖 Hướng dẫn")
st.sidebar.info("""
**Cách sử dụng:**
1. Chọn đề thi từ danh sách
2. Chọn chế độ xem:
   - Xem toàn bộ đề: Xem và làm tất cả câu hỏi
   - Làm bài trực tiếp: Làm từng câu một
3. Bài đọc Part 2 sẽ được hiển thị khi cần
4. Xem giải thích đáp án sau khi làm bài
""")

st.markdown("---")
st.caption("© 2025 Sở Y tế tỉnh Gia Lai - 10 bộ đề thi tiếng Anh Bắc 2")
st.caption("Mỗi đề có 120 câu được hoán đổi vị trí và tráo đáp án")