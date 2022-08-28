import streamlit as st
from utils import project1_desc as p1d


def app():
	st.write('''
		### 가상 환경 구축
		'''
		)
	
	p1d.desc()
