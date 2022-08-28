import streamlit as st
from utils import project2_desc as p2d


def app():
	st.write('''
		### Streamlit
		'''
		)
	p2d.desc()
