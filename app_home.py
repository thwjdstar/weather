import streamlit as st

def run_home_app():
    
    st.text('<평균기온의 정보와 강수량>')
    st.text('기간 : 2013.01~2023.11')

    st.text('아래 이미지는 날씨별 아이콘입니다.')

    img_url = 'https://naver-help-phinf.pstatic.net/MjAyMjA3MDZfMzYg/MDAxNjU3MTA4NjA0MDk5.-VxI4XshxkjJjXOh3nG3tm3-QPWbOXwi7u-MRGHIuEQg.ywF9YjzMkQyzW-TqKfVR113_hxM6RWCiRnz0WQ0QnjMg.PNG/icon_02.png?type=w1000'

    st.image(img_url)