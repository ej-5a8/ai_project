import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="식품군별 칼로리 분석",
    page_icon="🍔",
    layout="wide"
)

st.title("🍔 식품군별 칼로리 분석 시스템")

# 데이터 읽기
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(
            "전국통합식품영양성분정보_음식_표준데이터.csv",
            encoding="utf-8"
        )
    except:
        df = pd.read_csv(
            "전국통합식품영양성분정보_음식_표준데이터.csv",
            encoding="cp949"
        )

    return df

df = load_data()

# 컬럼 자동 탐색
food_group_col = None
food_name_col = None
calorie_col = None

for col in df.columns:

    if "식품대분류" in col:
        food_group_col = col

    if "식품명" in col:
        food_name_col = col

    if (
        "에너지" in col
        or "열량" in col
        or "칼로리" in col
    ):
        calorie_col = col

if not all([food_group_col, food_name_col, calorie_col]):
    st.error("필수 컬럼을 찾을 수 없습니다.")
    st.stop()

df[calorie_col] = pd.to_numeric(
    df[calorie_col],
    errors="coerce"
)

df = df.dropna(subset=[calorie_col])

# 식품군 선택
food_groups = sorted(
    df[food_group_col].dropna().unique()
)

selected_group = st.selectbox(
    "식품군 선택",
    food_groups
)

filtered = df[
    df[food_group_col] == selected_group
]

st.markdown("---")

col1, col2, col3 = st.columns(3)

col1.metric(
    "음식 수",
    len(filtered)
)

col2.metric(
    "평균 칼로리",
    round(filtered[calorie_col].mean(), 1)
)

col3.metric(
    "최고 칼로리",
    round(filtered[calorie_col].max(), 1)
)

# TOP10
st.subheader("🔥 칼로리 TOP 10")

top10 = (
    filtered
    .sort_values(
        calorie_col,
        ascending=False
    )
    [[food_name_col, calorie_col]]
    .head(10)
)

st.dataframe(
    top10,
    use_container_width=True
)

# LOW10
st.subheader("🥗 칼로리 LOW 10")

low10 = (
    filtered
    .sort_values(
        calorie_col,
        ascending=True
    )
    [[food_name_col, calorie_col]]
    .head(10)
)

st.dataframe(
    low10,
    use_container_width=True
)

# 전체 데이터
with st.expander("전체 데이터 보기"):
    st.dataframe(
        filtered,
        use_container_width=True
    )
