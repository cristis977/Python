import json
import streamlit as st
import pandas as pd
import folium
import numpy as np
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
def desc():
	test_weather = pd.read_csv('weather_data.csv', encoding='cp949')
	test_weather.columns = ['loc_num','day', 'temperature', 'rain', 'wind_direction', 'wind_power', 'r_hPa', 's_hPa', 'humidity', 'a', 'b']

	test_day = pd.DataFrame(test_weather, columns=['day','temperature'])   # csv를 df 로 변환
	test_day['day'] = pd.to_datetime(test_day['day'])

	all_day = pd.date_range('2022/06/01', '2022/06/08', freq='1min')
	all_day = pd.DataFrame(all_day, columns=['day'])

	df_day = pd.merge(all_day, test_day, how='outer')
	df_day.drop(df_day.tail(1).index,inplace=True)
	df_day.drop(df_day.head(1).index,inplace=True)
	df_day.set_index('day')
	chart_data = pd.DataFrame(df_day, columns=['temperature'])
	chart_data.fillna(method='ffill', inplace=True) # 채워주기
	chart_data.set_index(df_day['day'], inplace=True)
	
	
	
	st.line_chart(chart_data)










