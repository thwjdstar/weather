import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def main ():
    df = pd.read_csv('./data/statisticsDivision_20231123151658.csv', encoding='euc-kr')
    st.dataframe(df)
    
    st.text('연도별 최고/최저 평균기온 확인하기')

    column_list = df.columns [1:]
    
    selected_column = st.selectbox('컬럼을 선택하세요',column_list)

    st.text(selected_column + '컬럼의 히스토그램')
    fig1 = plt.figure()
    plt.hist(data = df, x= selected_column,rwidth= 0.8, bins =20 )
    st.pyplot(fig1)