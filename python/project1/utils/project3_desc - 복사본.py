import json
import streamlit as st
import pandas as pd
import folium
import numpy as np
from streamlit_folium import st_folium
def desc():
	My_location = pd.read_csv('My_location.csv')
	My_location.columns = ['coords_longitude', 'coords_latitude', 'type', 'Maps_URL','Address', 'Business_Name', 'CountryCode','Latitude', 'Longitude', 'Published', 'Title', 'Updated', 'type']


	st.title('This is title')
	st.header('this is header')

	test_name = My_location.loc[:,'Business_Name']
	test_adr = My_location.loc[:,'Address']
	test_url = My_location.loc[:,'Maps_URL']
	st.write(pd.DataFrame({
		'이름': test_name,
		'주소': test_adr,
		'URL' : test_url
	}))
	pd_name = pd.DataFrame(My_location.loc[:,'Business_Name'])
	pd_adr = pd.DataFrame(My_location.loc[:,'Address'])
	pd_long = pd.DataFrame(My_location.loc[:,'coords_longitude'])
	pd_lati = pd.DataFrame(My_location.loc[:,'coords_latitude'])

	m = folium.Map(location = [37.5602, 126.982], zoom_start= 12) # 기본시작위치
	for i in range(len(My_location)):   
		folium.Marker(
			[pd_lati['coords_latitude'][i], pd_long['coords_longitude'][i]],
			popup = pd_name['Business_Name'][i],
			adr = pd_adr['Address'][i]).add_to(m)
		folium.CircleMarker([pd_lati['coords_latitude'][i], pd_long['coords_longitude'][i]], radius = 3 , color = 'red', fill_color = 'red', popup = pd_name['Business_Name']).add_to(m)
		
	st_data = st_folium(m, width = 725)

