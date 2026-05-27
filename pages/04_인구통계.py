import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import re

# -----------------------------
# 한글 폰트 설정
# -----------------------------
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
else:
    plt.rc('font', family='DejaVu Sans')

plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# CSV 불러오기
# -----------------------------
df = pd.read_csv("popuiation.csv", encoding="cp949")

# 행정구역 컬럼
region_col = "행정구역"

# 지역 목록
regions = df[region_col].tolist()

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="서울 연령별 인구 분석",
    layout="wide"
)

st.title("📊 서울 연령별 인구 분석")

selected_region = st.selectbox(
    "행정구역 선택",
    regions
)

# 선택 지역 데이터
region_data = df[df[region_col] == selected_region].iloc[0]

# -----------------------------
# 연령 데이터 추출
# -----------------------------
ages = []
population = []

for col in df.columns:

    # 0세 ~ 99세
    match = re.search(r'_(\d+)세$', col)

    if match:
        age = int(match.group(1))

        value = str(region_data[col]).replace(",", "")
        value = int(value)

        ages.append(age)
        population.append(value)

    # 100세 이상
    elif "100세 이상" in col:
        value = str(region_data[col]).replace(",", "")
        value = int(value)

        ages.append(100)
        population.append(value)

# -----------------------------
# 그래프
# -----------------------------
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(
    ages,
    population,
    color="hotpink",
    linewidth=3
)

# 제목
ax.set_title(f"{selected_region} 연령별 인구수", fontsize=18)

# 축 이름
ax.set_xlabel("나이")
ax.set_ylabel("인구수")

# x축 10살 단위
ax.set_xticks(range(0, 101, 10))

# 세로 구분선
ax.grid(axis='x', linestyle='--', alpha=0.5)

# x축 범위
ax.set_xlim(0, 100)

# 출력
st.pyplot(fig)
