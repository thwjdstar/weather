import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')


def run_year_app():
    st.subheader('데이터 분석')

    st.text('전체 데이터 프레임 확인하기')


    df = pd.read_csv('./data/statisticsDivision_20231123151658.csv', encoding='euc-kr')
    st.dataframe(df)

    if st.checkbox('통계데이터 보기') :
        st.dataframe(df.describe())
    else :
        st.text('')
    
    st.text('기초통계데이터 확인하기') 

    data = df[df['일시'].str.contains('2013')]
    st.dataframe(data)

    selected_list = st.multiselect('연도와 원하는 내용 선택', df.columns[1:] ) 

    print(selected_list[1:])

    if len(selected_list) != 0:  #선택된 리스트가 0개인경우 출력 x 
        st.dataframe(df[selected_list])
    else:
        st.text('')


    # selected_column = st.multiselectbox('컬럼을 선택하세요',column_list)
    # selected_column = '컬럼을 선택하세요',str(column_list)

    # st.text(selected_column + '컬럼의 최소값')
    # st.dataframe (df.loc[ df[selected_column] == df[selected_column].min(), ])

    # st.text(selected_column + '컬럼의 최대값')
    # st.dataframe (df.loc[ df[selected_column] == df[selected_column].max(), ])

    # st.text(selected_column + '컬럼의 히스토그램')
    
    # fig1 = plt.figure()
    # df[selected_column].hist(bins= 20)
    # st.pyplot(fig1)


