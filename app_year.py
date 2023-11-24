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

    df = pd.read_csv('./data/statisticsDivision_20231123151658.csv', encoding='cp949', sep='\t')
    st.dataframe(df)

    st.text('기초통계데이터 확인하기')

    if st.checkbox('통계데이터 보기') :
        st.dataframe(df.describe())
    else :
        st.text('')

    st.text('최고/최저 데이터 확인하기')

    column_list = df.columns [:]

    # selected_column = st.multiselectbox('컬럼을 선택하세요',column_list)
    selected_column = ('컬럼을 선택하세요',column_list)

    language = ['2013', '2014', '2015', '2016', '2017']

    st.dataframe (df.loc[ df[selected_column] == df[selected_column].min(), ])

    st.text(selected_column + '컬럼의 최대값')
    st.dataframe (df.loc[ df[selected_column] == df[selected_column].max(), ])

    # st.text(selected_column + '컬럼의 히스토그램')
    
    # fig1 = plt.figure()
    # df[selected_column].hist(bins= 20)
    # st.pyplot(fig1)


