# streamlit 라이브러리와 datetime 모듈 불러오기
import streamlit as st
from datetime import datetime  

st.title('Unit 4. Input Widgets')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/widgets')

st.header('1. Button')
if st.button('say hello'):
    st.write('Hello')
else:
    st.write('Goodbye')


# st.header('2. Radio button')
radio_btn = st.radio('좋아하는 과일을 선택하세요',
                     ('사과', '딸기', '바나나'))
                     
if radio_btn == '사과':
    st.write('아삭아삭')
elif radio_btn == '딸기':
    st.write('상큼달콤')
else:
    st.write('한 입 베어물 때 부드럽고..~ 달콤하고..~ 참기름 처럼 꼬소-하고..~ 아카시아 꽃!향기가 나면서..')


st.header('3. Checkbox')
agree = st.checkbox('I Love U')
if agree:
    st.write('🥰'*10)

st.header('4. Select box')
option = st.selectbox('어떤 메뉴로 드릴까요?', ('마라탕', '초밥', '김치볶음밥'))
st.write('네', option, ' 으로 드리겠습니다.')

st.header('5. Multi select')
options = st.multiselect('좋아하는 색은?', ['Green', 'Yellow', 'Red', 'Blue'], ['Yellow', 'Red'])
st.write('선호 색상: ')
for i in options:
    st.write(i)


st.header('6. Input: Text/Number')

st.subheader('**_text_input_**')
title = st.text_input('가장 좋아하는 영화는?', 'Interstella')
st.write('당신의 최애 영화는 ', title)

st.subheader('**_number_input_**')
number = st.number_input('1-10 사이의 숫자를 입력하세요',
                        min_value=1, max_value=10, value=5, step=1)
st.write('입력한 숫자는 ', number)

st.header('7. Date input')
ymd = st.date_input('When is your birthday', datetime(1998,12,16))
st.write('Your Birthday ', ymd)

st.header('8. Slider')

st.subheader('**_Slider- 이전 구간_**')
age = st.slider('나이가 어떻게 되세요 ?', 0, 130 ,25)
st.write(age)

st.subheader('**_최소-최대값 내에서 숫자 사이 구간_**')
values = st.slider('값 구간 선택', 0.0, 100.0, (25.0, 75.0))
st.write('값 구간은', values)

st.subheader('**_년 월 일 사이 구간_**')

slider_date = st.slider(
    '날짜 구간을 선택하세요',
    datetime(2022, 1, 1), datetime(2022, 12, 31),
    value=(datetime(2022,6,1), datetime(2022,7,31)),
    format='YY/MM/DD')
st.write('slider_date : ', slider_date)
st.write('slider_date[0] : ', slider_date[0], 'slider_date[1] : ', slider_date[1])




# 년 월 일 시 사이 구간
slider_time = st.slider(
    'Select a range of datetime?',
    datetime(2022, 1, 1, 0, 30), datetime(2022, 12, 31, 0, 30),
    value=(datetime(2022, 7, 1, 0, 30), datetime(2022, 10, 31, 9, 30)),
    format='MM/DD/YY - hh:mm')
st.write('Slider time: ', slider_time)

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\4-1.input.py