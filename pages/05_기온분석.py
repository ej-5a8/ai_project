import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

st.title("🌡️ 서울 특정 날짜 기온 분석 및 미래 예측")

@st.cache_data
def load_data():

    try:
        df = pd.read_csv("seoul.csv", encoding="utf-8")
    except:
        df = pd.read_csv("seoul.csv", encoding="cp949")

    df.columns = (
        df.columns
        .str.replace('\ufeff', '', regex=False)
        .str.strip()
    )

    df["날짜"] = pd.to_datetime(
        df["날짜"],
        errors="coerce"
    )

    df = df.dropna(subset=["날짜"])

    df["최고기온(℃)"] = pd.to_numeric(
        df["최고기온(℃)"],
        errors="coerce"
    )

    df["최저기온(℃)"] = pd.to_numeric(
        df["최저기온(℃)"],
        errors="coerce"
    )

    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df


def predict_temperature(years, temps, target_year):

    years = np.array(years)
    temps = np.array(temps)

    mask = ~np.isnan(temps)

    years = years[mask]
    temps = temps[mask]

    if len(years) < 2:
        return None

    slope, intercept = np.polyfit(
        years,
        temps,
        1
    )

    prediction = slope * target_year + intercept

    return round(prediction, 1)


try:

    df = load_data()

    col1, col2 = st.columns(2)

    with col1:
        month = st.selectbox(
            "월 선택",
            range(1, 13)
        )

    days = sorted(
        df[df["월"] == month]["일"].unique()
    )

    with col2:
        day = st.selectbox(
            "일 선택",
            days
        )

    result = df[
        (df["월"] == month) &
        (df["일"] == day)
    ].copy()

    result = result.sort_values("연도")

    st.subheader(
        f"{month}월 {day}일 연도별 최고·최저기온"
    )

    if result.empty:

        st.warning("해당 날짜 데이터가 없습니다.")

    else:

        max_year = int(result["연도"].max())

        future_year = st.number_input(
            "예측할 미래 연도",
            min_value=max_year + 1,
            max_value=2100,
            value=max_year + 10
        )

        predicted_max = predict_temperature(
            result["연도"],
            result["최고기온(℃)"],
            future_year
        )

        predicted_min = predict_temperature(
            result["연도"],
            result["최저기온(℃)"],
            future_year
        )

        st.success(
            f"{future_year}년 {month}월 {day}일 예상 최고기온 : {predicted_max}℃"
        )

        st.info(
            f"{future_year}년 {month}월 {day}일 예상 최저기온 : {predicted_min}℃"
        )

        plt.rcParams["font.family"] = "Malgun Gothic"
        plt.rcParams["axes.unicode_minus"] = False

        fig, ax = plt.subplots(figsize=(14, 6))

        ax.plot(
            result["연도"],
            result["최고기온(℃)"],
            color="red",
            marker="o",
            label="최고기온"
        )

        ax.plot(
            result["연도"],
            result["최저기온(℃)"],
            color="blue",
            marker="o",
            label="최저기온"
        )

        # 예측값 표시
        ax.plot(
            [result["연도"].max(), future_year],
            [
                result["최고기온(℃)"].iloc[-1],
                predicted_max
            ],
            "r--"
        )

        ax.plot(
            [result["연도"].max(), future_year],
            [
                result["최저기온(℃)"].iloc[-1],
                predicted_min
            ],
            "b--"
        )

        ax.scatter(
            future_year,
            predicted_max,
            s=100,
            color="red",
            label=f"{future_year} 최고기온 예측"
        )

        ax.scatter(
            future_year,
            predicted_min,
            s=100,
            color="blue",
            label=f"{future_year} 최저기온 예측"
        )

        ax.set_title(
            f"{month}월 {day}일 연도별 기온 변화 및 미래 예측"
        )

        ax.set_xlabel("연도")
        ax.set_ylabel("기온(℃)")
        ax.grid(alpha=0.3)
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

        st.caption(
            "※ 예측값은 과거 데이터를 이용한 선형회귀 결과이며 실제 기온과 다를 수 있습니다."
        )

except Exception as e:

    st.error("오류가 발생했습니다.")
    st.exception(e)
