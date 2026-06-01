import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

st.title("🌡️ 서울 특정 날짜 기온 분석")

@st.cache_data
def load_data():

    # UTF-8 시도
    try:
        df = pd.read_csv("seoul.csv", encoding="utf-8")
    except:
        # 실패하면 CP949 시도
        df = pd.read_csv("seoul.csv", encoding="cp949")

    # 컬럼명 정리
    df.columns = (
        df.columns
        .str.replace('\ufeff', '', regex=False)
        .str.strip()
    )

    # 날짜 변환
    df["날짜"] = pd.to_datetime(
        df["날짜"],
        errors="coerce"
    )

    # 날짜 오류 제거
    df = df.dropna(subset=["날짜"])

    # 숫자형 변환
    df["최고기온(℃)"] = pd.to_numeric(
        df["최고기온(℃)"],
        errors="coerce"
    )

    df["최저기온(℃)"] = pd.to_numeric(
        df["최저기온(℃)"],
        errors="coerce"
    )

    # 연도/월/일 생성
    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df


try:

    df = load_data()

    col1, col2 = st.columns(2)

    with col1:
        month = st.selectbox(
            "월 선택",
            list(range(1, 13))
        )

    available_days = sorted(
        df[df["월"] == month]["일"].unique()
    )

    with col2:
        day = st.selectbox(
            "일 선택",
            available_days
        )

    result = df[
        (df["월"] == month) &
        (df["일"] == day)
    ].copy()

    result = result.sort_values("연도")

    st.subheader(
        f"{month}월 {day}일 연도별 최고·최저기온"
    )

    if len(result) == 0:

        st.warning("해당 날짜의 데이터가 없습니다.")

    else:

        plt.rcParams["font.family"] = "Malgun Gothic"
        plt.rcParams["axes.unicode_minus"] = False

        fig, ax = plt.subplots(figsize=(14, 6))

        ax.plot(
            result["연도"],
            result["최고기온(℃)"],
            color="red",
            marker="o",
            linewidth=2,
            label="최고기온"
        )

        ax.plot(
            result["연도"],
            result["최저기온(℃)"],
            color="blue",
            marker="o",
            linewidth=2,
            label="최저기온"
        )

        ax.set_title(
            f"{month}월 {day}일 연도별 기온 변화"
        )

        ax.set_xlabel("연도")
        ax.set_ylabel("기온(℃)")
        ax.grid(alpha=0.3)

        # 범례
        ax.legend()

        st.pyplot(fig)

        st.dataframe(
            result[
                [
                    "연도",
                    "최고기온(℃)",
                    "최저기온(℃)"
                ]
            ],
            use_container_width=True
        )

except Exception as e:

    st.error("데이터를 불러오는 중 오류가 발생했습니다.")
    st.exception(e)
