import streamlit as st

st.set_page_config(
    page_title="MBTI 책 & 영화 추천 🎬📚",
    page_icon="✨",
    layout="centered"
)

st.title("✨ MBTI 책 & 영화 추천기")
st.write("너의 MBTI에 딱 어울리는 책이랑 영화 찾아보자! 😎")

mbti_data = {
    "INTJ": {
        "books": [
            "📘 사피엔스 - 유발 하라리",
            "📗 코스모스 - 칼 세이건"
        ],
        "movies": [
            "🎬 인터스텔라",
            "🎬 인셉션"
        ]
    },

    "INTP": {
        "books": [
            "📘 이기적 유전자 - 리처드 도킨스",
            "📗 데미안 - 헤르만 헤세"
        ],
        "movies": [
            "🎬 매트릭스",
            "🎬 컨택트"
        ]
    },

    "ENTJ": {
        "books": [
            "📘 성공하는 사람들의 7가지 습관",
            "📗 넛지"
        ],
        "movies": [
            "🎬 아이언맨",
            "🎬 소셜 네트워크"
        ]
    },

    "ENTP": {
        "books": [
            "📘 아웃라이어",
            "📗 트렌드 코리아"
        ],
        "movies": [
            "🎬 울프 오브 월스트리트",
            "🎬 레디 플레이어 원"
        ]
    },

    "INFJ": {
        "books": [
            "📘 어린 왕자",
            "📗 미드나잇 라이브러리"
        ],
        "movies": [
            "🎬 월플라워",
            "🎬 소울"
        ]
    },

    "INFP": {
        "books": [
            "📘 연금술사",
            "📗 나미야 잡화점의 기적"
        ],
        "movies": [
            "🎬 어바웃 타임",
            "🎬 라라랜드"
        ]
    },

    "ENFJ": {
        "books": [
            "📘 죽고 싶지만 떡볶이는 먹고 싶어",
            "📗 미움받을 용기"
        ],
        "movies": [
            "🎬 코코",
            "🎬 원더"
        ]
    },

    "ENFP": {
        "books": [
            "📘 해리포터",
            "📗 페인트"
        ],
        "movies": [
            "🎬 주토피아",
            "🎬 업"
        ]
    },

    "ISTJ": {
        "books": [
            "📘 총, 균, 쇠",
            "📗 공부의 본질"
        ],
        "movies": [
            "🎬 포레스트 검프",
            "🎬 셜록 홈즈"
        ]
    },

    "ISFJ": {
        "books": [
            "📘 아몬드",
            "📗 완벽하지 않은 것들에 대한 사랑"
        ],
        "movies": [
            "🎬 리틀 포레스트",
            "🎬 코다"
        ]
    },

    "ESTJ": {
        "books": [
            "📘 원씽",
            "📗 부자의 그릇"
        ],
        "movies": [
            "🎬 탑건: 매버릭",
            "🎬 머니볼"
        ]
    },

    "ESFJ": {
        "books": [
            "📘 기분이 태도가 되지 않게",
            "📗 나는 나로 살기로 했다"
        ],
        "movies": [
            "🎬 겨울왕국",
            "🎬 인턴"
        ]
    },

    "ISTP": {
        "books": [
            "📘 팩트풀니스",
            "📗 인간 실격"
        ],
        "movies": [
            "🎬 존 윅",
            "🎬 베이비 드라이버"
        ]
    },

    "ISFP": {
        "books": [
            "📘 모모",
            "📗 달러구트 꿈 백화점"
        ],
        "movies": [
            "🎬 이웃집 토토로",
            "🎬 비긴 어게인"
        ]
    },

    "ESTP": {
        "books": [
            "📘 돈의 심리학",
            "📗 자존감 수업"
        ],
        "movies": [
            "🎬 분노의 질주",
            "🎬 스파이더맨: 노 웨이 홈"
        ]
    },

    "ESFP": {
        "books": [
            "📘 오늘 밤, 세계에서 이 사랑이 사라진다 해도",
            "📗 불편한 편의점"
        ],
        "movies": [
            "🎬 위대한 쇼맨",
            "🎬 맘마미아!"
        ]
    }
}

selected_mbti = st.selectbox(
    "👉 너의 MBTI를 선택해줘!",
    list(mbti_data.keys())
)

st.divider()

st.subheader(f"🌟 {selected_mbti}에게 추천하는 책!")

for book in mbti_data[selected_mbti]["books"]:
    st.write(book)

st.divider()

st.subheader(f"🎬 {selected_mbti}에게 추천하는 영화!")

for movie in mbti_data[selected_mbti]["movies"]:
    st.write(movie)

st.success("🍀 재미있게 즐기고, 새로운 작품도 많이 만나봐!")
