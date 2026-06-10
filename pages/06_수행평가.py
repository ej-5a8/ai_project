import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="식품 영양성분 분석",
    page_icon="🍔",
    layout="wide"
)

st.title("🍔 전국 통합 식품 영양성분 분석")

uploaded_file = st.file_uploader(
    "CSV 파일을 업로드하세요",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file, encoding="cp949")
    except:
        df = pd.read_csv(uploaded_file, encoding="utf-8")

    st.success("데이터 로드 완료!")

    st.subheader("데이터 미리보기")
    st.dataframe(df.head())

    # 컬럼 자동 탐색
    food_group_col = None
    food_name_col = None
    calorie_col = None

    for col in df.columns:
        if "식품대분류" in col:
            food_group_col = col

        if "식품명" in col:
            food_name_col = col

        if "에너지" in col or "열량" in col or "칼로리" in col:
            calorie_col = col

    if food_group_col and food_name_col and calorie_col:

        groups = sorted(df[food_group_col].dropna().unique())

        selected_group = st.selectbox(
            "식품군 선택",
            groups
        )

        filtered = df[df[food_group_col] == selected_group].copy()

        filtered[calorie_col] = pd.to_numeric(
            filtered[calorie_col],
            errors="coerce"
        )

        filtered = filtered.dropna(subset=[calorie_col])

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

        st.markdown("## 🔥 칼로리 TOP 10")

        top10 = (
            filtered
            .sort_values(calorie_col, ascending=False)
            [[food_name_col, calorie_col]]
            .head(10)
        )

        st.dataframe(top10, use_container_width=True)

        fig_top = px.bar(
            top10,
            x=food_name_col,
            y=calorie_col,
            title="칼로리 TOP10"
        )

        st.plotly_chart(fig_top, use_container_width=True)

        st.markdown("## 🥗 칼로리 LOW 10")

        low10 = (
            filtered
            .sort_values(calorie_col, ascending=True)
            [[food_name_col, calorie_col]]
            .head(10)
        )

        st.dataframe(low10, use_container_width=True)

        fig_low = px.bar(
            low10,
            x=food_name_col,
            y=calorie_col,
            title="칼로리 LOW10"
        )

        st.plotly_chart(fig_low, use_container_width=True)

    else:
        st.error(
            "식품군, 식품명, 칼로리 컬럼을 찾을 수 없습니다."
        )

else:
    st.info("CSV 파일을 업로드해주세요.")
