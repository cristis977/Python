import pandas as pd
import folium
import datetime
import numpy as np
import altair as alt
import streamlit as st

def get_mydata(paths):
    My_location = pd.read_csv(paths)     # 데이터 로드
    My_location.columns = ['coords_longitude', 'coords_latitude', 'type', 
    'Maps_URL','Address', 'Business_Name', 'CountryCode',
    'Latitude', 'Longitude', 'Published', 'Title', 'Updated',
    'type']    # 데이터 컬럼 재정의

    return My_location


def w_map(data, lati, long, name, adress):
    m = folium.Map(location = [37.5602, 126.982], zoom_start= 12)   # 지도 시작 위치
    for i in range(len(data)):
        folium.Marker(
            [lati['coords_latitude'][i], long['coords_longitude'][i]],  # 지도 위치
            popup = name['Business_Name'][i],                           # 팝업 내용
            adr = adress['Address'][i]).add_to(m)                       # 주소 내용
        folium.CircleMarker([lati['coords_latitude'][i], 
                             long['coords_longitude'][i]], 
                            radius = 3 , color = 'red', fill_color = 'red', # 지정위치에 빨간원 생성
                            popup = name['Business_Name']).add_to(m)    # 팝업 내용
    return m


def get_w_data(file_path):
    weather = pd.read_csv(file_path, encoding='cp949') # 데이터 로드
    weather.columns = ['loc_num','day', 'temperature', 'rain', 'wind_direction', 'wind_power', 
                             'r_hPa', 's_hPa', 'humidity', 'a', 'b'] #칼럼 재정의
    weather.drop(labels=['loc_num','rain', 'wind_direction', 'wind_power',  #불필요한 칼럼 제거
                        'r_hPa', 's_hPa', 'humidity', 'a', 'b'], axis=1, inplace=True)
    weather_day = pd.DataFrame(weather, columns=['day','temperature']) # 데이터 프레임화
    weather_day['day'] = pd.to_datetime(weather_day['day']) # 타입 변경
    weather_day.set_index('day', inplace=True) # 인덱스 재정의
    return weather_day


def missing_ck(df, freqs):
    start  = df.index[0]
    end = df.index[-1]
    timestamp = pd.date_range(start, end, freq=freqs)
    df = df.reindex(timestamp)
    
    return (df)

def physical_check(df):
    df[df < -33.0] = np.nan
    df[df>40] = np.nan
    return (df)

def step_check1(df):
    temp = df.iloc[0,0]
    df['step_check'] = df.diff().fillna(-999999.9)
    df[df.step_check < -3.0] = np.nan
    df[df.step_check > 3.0] = np.nan
    if temp:
        df.iloc[0,0] = temp
    return (df)

def persistence_ck(df):
    df['persis'] = df.step_check.abs()
    dummy_data = df.resample('H').sum()
    dummy_data.drop(dummy_data.index[-1], inplace=True)
    hour = dummy_data[dummy_data.persis<0.1].index.hour
    if len(hour):
        for i in hour:
            df[df.index.hour == i] = np.nan
    return (df)

def get_y_data(paths):
    y_weather = pd.read_csv(paths, encoding='cp949',skiprows=[0], names=['num','loc','date','temperature'])
    y_weather.drop(['num','loc'],axis = 1, inplace = True) # 데이터 재정의 후 필요없는 부분 삭제
    y_weather['date'] = pd.to_datetime(y_weather['date']) # 타입 재정의
#    y_weather = y_weather.set_index('date', inplace=True)
#    y_weather = missing_ck(y_weather, 'H')   
#    y_weather = physical_check(y_weather)
#    y_weather.drop(['step_check'],axis=1, inplace=True)
#    y_weather.reset_index(drop=False, inplace=True)
#    y_weather.columns =['date', 'temperature']
#    y_weather['date'] = pd.to_datetime(y_weather['date'])
#    y_weather = pd.DataFrame(y_weather)
    
    return y_weather


def resample_day(df):
  df.set_index(df['date'], inplace = True)
  df = df.dropna().resample('d').agg({'temperature':['size','mean']})
  df = df.droplevel(level=0, axis=1)
  df.loc[df['size']<18, 'mean'] = np.nan
  df.dropna(inplace = True)
  df = missing_ck(df, 'd')
  df.drop(['size'],axis=1, inplace=True)
  df.reset_index(drop=False, inplace = True) # 인덱스 재정의
  df.columns = ['date', 'temperature']
  return df

def resample_month(df):
  df = df.dropna().resample('m').agg({'temperature':['size','mean']})
  df = df.droplevel(level=0, axis=1)
  df.loc[df['size']<576, 'mean'] = np.nan
  df.dropna(inplace = True)
  df = missing_ck(df, 'm')
  df.drop(['size'],axis=1, inplace=True)
  df.reset_index(drop=False, inplace = True) # 인덱스 재정의 
  df.columns = ['date', 'temperature']
  return df

def make_chart(df, titlename):
	chart = alt.Chart(df, title=titlename).mark_line().encode(
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
		alt.Chart(df)
		.encode(
			x="date:T",
			y="temperature",
		)
	)
	points = chart_temp.transform_filter(hover).mark_circle(size=50)

	tooltips = (
    alt.Chart(df)
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