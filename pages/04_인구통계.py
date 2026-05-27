import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

# -----------------------------
# 한글 폰트 설정
# -----------------------------
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
else:
    plt.rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("popuiation.csv", encoding='utf-8')

# 행정구역 컬럼 이름 찾기
region_col = df.columns[0]

# 숫자형 컬럼만 추출
age_columns = df.columns[3:]

# 행정구역 목록
regions = df[region_col].tolist()

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="서울 인구 분석", layout="wide")

st.title("📊 서울 연령별 인구 분석")

selected_region = st.selectbox(
    "행정구역 선택",
    regions
)

# 선택된 지역 데이터
region_data = df[df[region_col] == selected_region].iloc[0]

# 나이 / 인구수 추출
ages = []
population = []

for col in age_columns:
    try:
        age = int(col.replace('세', '').replace(' 이상', '').strip())
        ages.append(age)

        value = str(region_data[col]).replace(',', '')
        population.append(int(value))

    except:
        continue

# -----------------------------
# 그래프
# -----------------------------
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(
    ages,
    population,
    color='hotpink',
    linewidth=3
)

# 제목
ax.set_title(f"{selected_region} 연령별 인구수", fontsize=18)

# 축 이름
ax.set_xlabel("나이", fontsize=13)
ax.set_ylabel("인구수", fontsize=13)

# x축 10살 단위 구분선
ax.set_xticks(range(0, 101, 10))
ax.grid(axis='x', linestyle='--', alpha=0.5)

# 보기 좋게
ax.set_xlim(0, 100)

st.pyplot(fig)
