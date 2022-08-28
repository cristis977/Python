import json
import streamlit as st
import pandas as pd
import folium
import numpy as np
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import altair as alt
def desc():


	month_test = pd.read_csv('y_data.csv', encoding='cp949')
	month_test.columns = ['loc', 'loc_name', 'date', 'temperature']
	month_test['date'] = pd.to_datetime(month_test['date']) # 데이터타입 변환
	
	month_df1 = pd.DataFrame(month_test, columns=['date','temperature'])
	month_df1['date'] = pd.to_datetime(month_df1['date']) # 데이터타입 변환
	
	d_test1 = pd.date_range('2021/01/01', '2022/01/01', freq='60min')
	d_test1 = pd.DataFrame(d_test1)
	d_test1.columns  = ['date']

	y_df1 = pd.merge(d_test1, month_df1, how='outer') #합치기
	y_df1.drop(y_df1.tail(1).index,inplace=True)
	y_df1.drop(y_df1.head(1).index,inplace=True)
	#chart_data = y_df1.set_index('date')

	chart = alt.Chart(y_df1).mark_line().encode(
		x = "date:T",
		y = "temperature"
	)
	hover = alt.selection_single(
    fields=["date"],
    nearest=True,
    on="mouseover",
    empty="none",
	)
	chart_temp = (
		alt.Chart(y_df1)
		.encode(
			x="date:T",
			y="temperature",
		)
	)
	points = chart_temp.transform_filter(hover).mark_circle(size=50)

	tooltips = (
    alt.Chart(y_df1)
    .mark_rule()
    .encode(
        x="date:T",
        y="temperature",
        opacity=alt.condition(hover, alt.value(0.1), alt.value(0)),
        tooltip=[
            alt.Tooltip("date:T", title="date"),
            alt.Tooltip("temperature", title="temperature"),
			],
		)
		.add_selection(hover)
	)

	st.altair_chart((chart+ points + tooltips).interactive(), use_container_width=True)

	'''st.line_chart(chart_data)  #1년치 시간당 차트 그래프'''

	month_test.set_index('date', inplace=True) # 인덱스를 시간으로

	dayly_mean = month_test['temperature'].resample('D').mean() # 인덱스 기준 월 평균

	monthly_mean = month_test['temperature'].resample('M').mean() # 인덱스 기준 월 평균

	st.line_chart(monthly_mean) # 

	st.line_chart(dayly_mean)




