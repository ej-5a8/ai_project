import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="Countries MBTI Analysis",
    layout="centered"
)

st.title("🌍 국가별 MBTI 비율 분석")

# CSV 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 국가 컬럼 찾기
country_col = df.columns[0]

# MBTI 컬럼
mbti_cols = df.columns[1:]

# 국가 선택
country = st.selectbox(
    "국가를 선택하세요",
    sorted(df[country_col].unique())
)

# 선택 국가 데이터
selected_row = df[df[country_col] == country].iloc[0]

# MBTI 비율
values = selected_row[mbti_cols].astype(float)

# 내림차순 정렬
values = values.sort_values(ascending=False)

# 색상 설정
colors = []

# 1등 색상
top_color = "#FFD700"  # 노란색

# 하늘색 그라데이션
base_color = np.array([135, 206, 235]) / 255  # skyblue
white = np.array([1, 1, 1])

for i in range(len(values)):
    if i == 0:
        colors.append(top_color)
    else:
        ratio = i / (len(values) - 1)
        blended = base_color * (1 - ratio) + white * ratio
        colors.append(blended)

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(values.index, values.values * 100, color=colors)

# 값 표시
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.2,
        f"{height:.1f}%",
        ha='center',
        fontsize=9
    )

# 그래프 스타일
ax.set_title(f"{country} MBTI Distribution", fontsize=18, pad=20)
ax.set_ylabel("Percentage (%)")
ax.set_ylim(0, max(values.values * 100) + 5)

plt.xticks(rotation=45)

# 상단/우측 테두리 제거
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

st.pyplot(fig)

# 최고 MBTI 출력
st.success(
    f"🏆 {country}에서 가장 높은 MBTI는 "
    f"'{values.index[0]}' ({values.iloc[0] * 100:.1f}%) 입니다."
)
