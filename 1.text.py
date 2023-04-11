# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

# header, subheader, text, caption 연습하기
st.title('Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')
st.header('Header 연습')
st.subheader('Subheader 연습')
st.text('text 연습')
st.caption('caption 연습')

# markdown 연습하기
st.markdown('# MD title')
st.markdown('## MD header')
st.markdown('### MD subheader')
st.markdown('### MD')
st.markdown('_**MD 진하게 기울임**_')

# Latex & Code 연습하기
st.markdown('## Code & Latex')
st.code('a + ar + ar^2 + ar^3')
st.latex(r'''a + ar + ar^2 + ar^3''')

# write 연습하기
st.title('write')
st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')
st.text('아래 딕셔너리를 판다스 데이터프레임으로 변경')
st.caption("{'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']}")
df = pd.DataFrame


# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\1.text.py