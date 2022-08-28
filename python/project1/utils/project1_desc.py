import streamlit as st
from PIL import Image
def desc():
	image1 = Image.open('C:\\Users\\JY\\Documents\\PythonScripts\\project\\pages\\images\\install1.jpg')
	st.image(image1, caption='Anaconda PowerShell Prompt')
	st.write('''
		### 최초 가상 환경 구축을 위한 명령어 입력 모습
		 	conda create -n pub python=3.7.4 ipython numpy matplotlib pandas scipy scikit-learn tensorflow keras		
	''')
	image2 = Image.open('C:\\Users\\JY\\Documents\\PythonScripts\\project\\pages\\images\\install2.jpg')
	st.image(image2, caption='Anaconda PowerShell Prompt')
	st.write('''
		### 가상환경 설치 및 진입 후 추가적인 라이브러리 설치 모습
		 	pip install streamlit_folium
			pip install imageio-ffmpeg
			pip install pandas_datareader
			pip install seaborn
			pip install streamlit
		
	''')

















	