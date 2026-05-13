import streamlit as st
st.title('나의 첫 웹서비스 만들기!')
a=st.text_input('이름을 입력하세요')
b=st.selectbox('좋아하는 음식을 선택하세요',['치킨','마라탕','김치볶음밥'])
if st.button('인사말 생성'):
  st.write(a+'님 안녕하세요!')
  st.info('반갑습니다')
  st.warning(b+'이라니! 뭘 좀 아시는군요!!!!!!!!!!')
  st.error('우리 사이좋게 지내요!!!')
  st.balloons()
  
