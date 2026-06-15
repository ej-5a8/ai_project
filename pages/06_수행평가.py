import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="식품군별 100g당 칼로리 분석",
    page_icon="🍔",
    layout="wide"
)

st.title("🍔 식품군별 100g당 칼로리 분석")

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

# 컬럼 찾기
food_group_col = None
food_name_col = None
calorie_col = None

for col in df.columns:

    if "식품대분류" in col:
        food_group_col = col

    if "식품명" in col:
        food_name_col = col

    if "에너지" in col or "열량" in col:
        calorie_col = col

if not all([food_group_col, food_name_col, calorie_col]):
    st.error("필수 컬럼을 찾을 수 없습니다.")
    st.write(df.columns.tolist())
    st.stop()

# 숫자 변환
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

st.subheader(f"선택한 식품군 : {selected_group}")

col1, col2, col3 = st.columns(3)

col1.metric(
    "음식 수",
    len(filtered)
)

col2.metric(
    "평균 kcal(100g당)",
    round(filtered[calorie_col].mean(), 1)
)

col3.metric(
    "최고 kcal(100g당)",
    round(filtered[calorie_col].max(), 1)
)

# TOP10
st.subheader("🔥 100g당 칼로리가 높은 음식 TOP 10")

top10 = (
    filtered
    .sort_values(calorie_col, ascending=False)
    [[food_name_col, calorie_col]]
    .head(10)
)

top10.columns = [
    "음식명",
    "100g당 칼로리(kcal)"
]

st.table(top10)

# LOW10
st.subheader("🥗 100g당 칼로리가 낮은 음식 TOP 10")

low10 = (
    filtered
    .sort_values(calorie_col, ascending=True)
    [[food_name_col, calorie_col]]
    .head(10)
)

low10.columns = [
    "음식명",
    "100g당 칼로리(kcal)"
]

st.table(low10)

# 다운로드용 데이터
st.subheader("📋 전체 데이터")

show_df = filtered[
    [food_name_col, calorie_col]
].copy()

show_df.columns = [
    "음식명",
    "100g당 칼로리(kcal)"
]

st.dataframe(
    show_df,
    use_container_width=True
)
