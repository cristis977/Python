import streamlit as st
from PIL import Image

def desc():
	st.title('st.image / 이미지 표현')
	image1 = Image.open('C:\\Users\\JY\\Documents\\PythonScripts\\project\\pages\\images\\st-image.jpg')
	st.image(image1, caption='Explain st.image')
	st.write('''
	#### Example
		from PIL import Image
		image1 = Image.open('st-image.jpg')
		st.image(image1, caption='Explain st.image')
	''')









	
	st.caption('출처 : https://docs.streamlit.io/')
	
