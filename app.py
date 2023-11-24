import streamlit as st

from app_home import run_home_app
from app_year import run_year_app

def main() :
    st.title('연도별 기온정보와 강수량')

    menu = ['Home', 'YEAR', 'WEATHER']
    
    choice = st.sidebar.selectbox('메뉴 선택',menu)

    if choice == menu[0] :
        run_home_app()
    elif choice == menu[1] :
        run_year_app()
   

if __name__ == '__main__' :
    main()