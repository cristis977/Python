import streamlit as st
import numpy as np
import myfunc as fc
import pandas as pd
import altair as alt

def desc():

	paths = 'C:/Users/JY/Documents/PythonScripts/project/data/'
	y_df1 = fc.get_y_data(paths + 'y_data.csv') # 1년 데이터 로드
	
	st.subheader('전체데이터')
	fc.make_chart(y_df1, '전체데이터') # 데이터 차트화

	st.subheader('일평균')
	y_df2 = fc.resample_day(y_df1)
	fc.make_chart(y_df2, '일평균')     # 데이터 차트화

	st.subheader('월평균')
	y_df3 = fc.resample_month(y_df1)  # 데이터 차트화
	fc.make_chart(y_df3, '월평균')