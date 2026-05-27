import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

# -----------------------------
# 한글 폰트
# -----------------------------
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
else:
    plt.rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# CSV 불러오기
# -----------------------------
df = pd.read_csv("popuiation.csv", encoding='cp949')

# 첫 번째 컬럼 = 행정구역
region_col = df.columns[0]

# 지역 목록
regions = df[region_col].tolist()

# -----------------------------
# UI
# -----------------------------
st.title("📊 서울 연령별 인구 분석")

selected_region = st.selectbox(
    "행정구역 선택",
    regions
)

# 선택된 지역
region_data = df[df[region_col] == selected_region].iloc[0]

# -----------------------------
# 연령 데이터 추출
# -----------------------------
ages = []
population = []

for col in df.columns:

    # "세"가 들어간 컬럼만 사용
    if "세" in col:

        try:
            # 나이 추출
            age_text = col.split("세")[0]
            age = int(age_text.replace(" ", "").replace("이상", ""))

            # 인구수
            value = str(region_data[col]).replace(",", "")
            value = int(value)

            ages.append(age)
            population.append(value)

        except:
            pass

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

# 축
ax.set_xlabel("나이")
ax.set_ylabel("인구수")

# 10살 단위 구분선
ax.set_xticks(range(0, 101, 10))
ax.grid(axis='x', linestyle='--', alpha=0.5)

# 범위
ax.set_xlim(0, 100)

# 출력
st.pyplot(fig)
