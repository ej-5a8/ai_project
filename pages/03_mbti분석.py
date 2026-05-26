```python
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="국가별 MBTI 분석",
    layout="centered"
)

st.title("🌍 국가별 MBTI 분석")

# CSV 읽기
df = pd.read_csv("countriesMBTI_16types.csv")

# 국가 컬럼
country_col = df.columns[0]

# MBTI 컬럼
mbti_cols = df.columns[1:]

# 국가 선택
country = st.selectbox(
    "국가를 선택하세요",
    sorted(df[country_col].unique())
)

# 선택 국가 데이터
row = df[df[country_col] == country].iloc[0]

# 데이터프레임 생성
mbti_df = pd.DataFrame({
    "MBTI": mbti_cols,
    "Value": row[mbti_cols].astype(float).values
})

# 정렬
mbti_df = mbti_df.sort_values(
    by="Value",
    ascending=False
).reset_index(drop=True)

# 퍼센트 변환
mbti_df["Percent"] = mbti_df["Value"] * 100

# 색상 설정
colors = []

for i in range(len(mbti_df)):
    if i == 0:
        colors.append("#FFD700")  # 1등 노란색
    else:
        opacity = 1 - (i / len(mbti_df)) * 0.7
        colors.append(f"rgba(135,206,235,{opacity})")

mbti_df["Color"] = colors

# 그래프 생성
chart = alt.Chart(mbti_df).mark_bar().encode(
    x=alt.X("MBTI:N", sort=None),
    y=alt.Y("Percent:Q", title="Percentage (%)"),
    color=alt.Color(
        "Color:N",
        scale=None,
        legend=None
    ),
    tooltip=[
        alt.Tooltip("MBTI:N"),
        alt.Tooltip("Percent:Q", format=".1f")
    ]
).properties(
    width=700,
    height=450,
    title=f"{country} MBTI Distribution"
)

st.altair_chart(chart, use_container_width=True)

# 최고 MBTI
top = mbti_df.iloc[0]

st.success(
    f"🏆 가장 높은 MBTI는 "
    f"{top['MBTI']} ({top['Percent']:.1f}%) 입니다."
)
```

