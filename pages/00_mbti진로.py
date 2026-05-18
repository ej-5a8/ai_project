import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천 🌈",
    page_icon="✨",
    layout="centered"
)

st.title("✨ MBTI 진로 추천기")
st.write("나의 MBTI에 어울리는 진로를 알아보자! 😎")

mbti_data = {
    "INTJ": [
        {
            "job": "🧠 데이터 사이언티스트",
            "major": "컴퓨터공학과, 통계학과",
            "personality": "논리적이고 분석적인 성격",
            "salary": "평균 연봉 약 6,500만원"
        },
        {
            "job": "🚀 전략 기획가",
            "major": "경영학과",
            "personality": "계획 세우기를 좋아하고 목표 지향적",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],
    "INTP": [
        {
            "job": "💻 개발자",
            "major": "컴퓨터공학과",
            "personality": "호기심이 많고 문제 해결을 좋아함",
            "salary": "평균 연봉 약 5,800만원"
        },
        {
            "job": "🔬 연구원",
            "major": "물리학과, 화학과",
            "personality": "탐구심이 강하고 아이디어가 많음",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "ENTJ": [
        {
            "job": "📈 CEO",
            "major": "경영학과",
            "personality": "리더십이 강하고 추진력이 있음",
            "salary": "평균 연봉 약 8,000만원"
        },
        {
            "job": "⚖️ 변호사",
            "major": "법학과",
            "personality": "논리적이고 설득력이 뛰어남",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],
    "ENTP": [
        {
            "job": "🎤 마케터",
            "major": "광고홍보학과",
            "personality": "창의적이고 말하는 걸 좋아함",
            "salary": "평균 연봉 약 5,200만원"
        },
        {
            "job": "📱 스타트업 창업가",
            "major": "경영학과",
            "personality": "도전 정신이 강하고 아이디어가 많음",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "INFJ": [
        {
            "job": "💖 상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어나고 따뜻함",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "✍️ 작가",
            "major": "문예창작과",
            "personality": "상상력이 풍부하고 감수성이 깊음",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],
    "INFP": [
        {
            "job": "🎨 디자이너",
            "major": "시각디자인학과",
            "personality": "감성이 풍부하고 창의적",
            "salary": "평균 연봉 약 4,800만원"
        },
        {
            "job": "🎵 음악 프로듀서",
            "major": "실용음악과",
            "personality": "예술적 감각이 뛰어남",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "ENFJ": [
        {
            "job": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람들을 이끄는 걸 좋아함",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🎙️ 아나운서",
            "major": "언론정보학과",
            "personality": "소통 능력이 뛰어나고 밝음",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],
    "ENFP": [
        {
            "job": "📸 크리에이터",
            "major": "미디어학과",
            "personality": "에너지가 넘치고 창의적",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🌍 여행 기획자",
            "major": "관광학과",
            "personality": "새로운 경험을 좋아함",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],
    "ISTJ": [
        {
            "job": "🏦 회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 책임감이 강함",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "job": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각함",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "ISFJ": [
        {
            "job": "🏥 간호사",
            "major": "간호학과",
            "personality": "배려심이 깊고 성실함",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "👶 유치원 교사",
            "major": "유아교육과",
            "personality": "친절하고 따뜻함",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],
    "ESTJ": [
        {
            "job": "📊 공무원",
            "major": "행정학과",
            "personality": "체계적이고 리더십이 있음",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "🏢 프로젝트 매니저",
            "major": "경영학과",
            "personality": "조직 관리 능력이 뛰어남",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "ESFJ": [
        {
            "job": "🩺 병원 코디네이터",
            "major": "보건행정학과",
            "personality": "친화력이 좋고 배려심이 많음",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🎉 행사 기획자",
            "major": "이벤트학과",
            "personality": "사람들과 함께하는 걸 좋아함",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],
    "ISTP": [
        {
            "job": "🔧 기계 엔지니어",
            "major": "기계공학과",
            "personality": "손재주가 좋고 실용적",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "job": "🚗 자동차 디자이너",
            "major": "자동차공학과",
            "personality": "문제 해결 능력이 뛰어남",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],
    "ISFP": [
        {
            "job": "🖌️ 일러스트레이터",
            "major": "디자인학과",
            "personality": "감각적이고 자유로운 성향",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "🐶 동물 트레이너",
            "major": "동물자원학과",
            "personality": "다정하고 섬세함",
            "salary": "평균 연봉 약 3,800만원"
        }
    ],
    "ESTP": [
        {
            "job": "⚽ 스포츠 마케터",
            "major": "스포츠산업학과",
            "personality": "활동적이고 도전을 즐김",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🎬 방송 PD",
            "major": "방송영상학과",
            "personality": "순발력이 좋고 열정적",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],
    "ESFP": [
        {
            "job": "🎤 배우",
            "major": "연극영화과",
            "personality": "사람들 앞에 서는 걸 좋아함",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "💄 뷰티 크리에이터",
            "major": "뷰티미용학과",
            "personality": "트렌드에 민감하고 밝음",
            "salary": "평균 연봉 약 4,200만원"
        }
    ]
}

selected_mbti = st.selectbox(
    "👉 너의 MBTI를 선택해줘!",
    list(mbti_data.keys())
)

st.divider()

st.subheader(f"🌟 {selected_mbti}에게 추천하는 진로!")

for career in mbti_data[selected_mbti]:
    st.markdown(f"""
    ### {career['job']}
    - 📚 추천 학과: **{career['major']}**
    - 😊 잘 어울리는 성격: **{career['personality']}**
    - 💰 평균 연봉: **{career['salary']}**
    """)

st.success("🎉 미래의 멋진 모습을 응원할게!")
