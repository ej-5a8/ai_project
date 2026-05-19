import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 관광지 TOP 10",
    layout="wide"
)

st.title("🇰🇷 외국인 인기 서울 관광지 TOP 10")
st.markdown("폴리움을 사용한 서울 관광 명소 지도")

# 서울 중심 좌표
seoul_center = [37.5665, 126.9780]

# 지도 생성
m = folium.Map(
    location=seoul_center,
    zoom_start=11,
    tiles="OpenStreetMap"
)

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선 시대 대표 궁궐"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "desc": "쇼핑과 먹거리 중심지"
    },
    {
        "name": "남산서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울 야경 명소"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "desc": "전통 한옥 거리"
    },
    {
        "name": "인사동",
        "lat": 37.574187,
        "lon": 126.984952,
        "desc": "전통 문화 거리"
    },
    {
        "name": "홍대거리",
        "lat": 37.556336,
        "lon": 126.922652,
        "desc": "젊음과 예술의 거리"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009223,
        "desc": "현대적 랜드마크"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.512556,
        "lon": 127.102535,
        "desc": "서울 초고층 전망대"
    },
    {
        "name": "청계천",
        "lat": 37.569223,
        "lon": 126.978387,
        "desc": "도심 속 산책 명소"
    },
    {
        "name": "광장시장",
        "lat": 37.570435,
        "lon": 126.999596,
        "desc": "한국 전통 시장 음식"
    }
]

# 마커 추가
for idx, place in enumerate(places, start=1):
    popup_html = f"""
    <b>{idx}. {place['name']}</b><br>
    {place['desc']}
    """

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=folium.Popup(popup_html, max_width=250),
        tooltip=place["name"],
        icon=folium.Icon(
            color="red",
            icon="info-sign"
        )
    ).add_to(m)

# 지도 표시
st_folium(
    m,
    width=1200,
    height=700
)

st.markdown("---")
st.caption("데이터 예시: 외국인 관광객 선호 서울 명소")
