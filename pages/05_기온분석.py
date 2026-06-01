import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

st.title("서울 특정 날짜 기온 변화 분석")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("seoul.csv", encoding="cp949")

    # 컬럼명 공백 제거
    df.columns = df.columns.str.strip()

    # 날짜 변환
    df["날짜"] = pd.to_datetime(df["날짜"])

    # 연도, 월, 일 추출
    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df

df = load_data()

# 월 선택
month = st.selectbox(
    "월 선택",
    sorted(df["월"].unique())
)

# 선택된 월의 일 목록
days = sorted(
    df[df["월"] == month]["일"].unique()
)

day = st.selectbox(
    "일 선택",
    days
)

# 데이터 필터링
filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

# 결측값 제거
filtered = filtered.dropna(
    subset=["최고기온(℃)", "최저기온(℃)"]
)

if filtered.empty:
    st.warning("해당 날짜의 데이터가 없습니다.")
else:

    st.subheader(f"{month}월 {day}일 연도별 기온 변화")

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        filtered["연도"],
        filtered["최고기온(℃)"],
        color="red",
        marker="o",
        label="최고기온"
    )

    ax.plot(
        filtered["연도"],
        filtered["최저기온(℃)"],
        color="blue",
        marker="o",
        label="최저기온"
    )

    ax.set_title(f"{month}월 {day}일 연도별 최고·최저기온")
    ax.set_xlabel("연도")
    ax.set_ylabel("기온(℃)")
    ax.grid(True, alpha=0.3)

    # 범례
    ax.legend()

    st.pyplot(fig)

    st.dataframe(
        filtered[
            ["연도", "최고기온(℃)", "최저기온(℃)"]
        ].sort_values("연도"),
        use_container_width=True
    )
