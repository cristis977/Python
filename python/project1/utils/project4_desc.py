import streamlit as st
import myfunc as fc
def desc():
	paths = 'C:/Users/JY/Documents/PythonScripts/project/data/'
	weather = fc.get_w_data(paths + 'weather_data.csv') # 날짜 datetime 변환까지 완료
	weather	= fc.missing_ck(weather, 'T') # 비어있는 시간 결측 해결
	weather = fc.physical_check(weather) # 물리적 한계 검사
	weather = fc.step_check1(weather) # 결측 검사
	weather = fc.persistence_ck(weather) # 결측 검사

	chart_data = weather.interpolate(method='time') # 결측 부분 채우기
	st.line_chart(chart_data['temperature'])










