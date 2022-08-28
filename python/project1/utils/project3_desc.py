import myfunc as fc
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import st_folium

def desc():
	paths = 'C:/Users/JY/Documents/PythonScripts/project/data/'
	My_location = fc.get_mydata(paths + 'My_location.csv') # 여행지도 파일 로드
	
	st.title('여행 지도')
	st.header('이름 주소 URL')

	t_name = My_location.loc[:,'Business_Name']	 # 보여줄 부분만 꺼내오기
	t_adr = My_location.loc[:,'Address']
	t_url = My_location.loc[:,'Maps_URL']
	st.write(pd.DataFrame({	 					# 데이터 프레임으로 만들면서 web에 표현
		'이름': t_name,
		'주소': t_adr,
		'URL' : t_url
	}))
	name = pd.DataFrame(My_location.loc[:,'Business_Name'])
	adr = pd.DataFrame(My_location.loc[:,'Address'])
	longi = pd.DataFrame(My_location.loc[:,'coords_longitude'])
	lati = pd.DataFrame(My_location.loc[:,'coords_latitude'])

	m = fc.w_map(My_location, lati, longi, name, adr)  # 지도 데이터 작성
		
	st_data = st_folium(m, width = 725) 		# folium을 이용하여 web에 표현

