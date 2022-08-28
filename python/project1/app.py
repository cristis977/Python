import streamlit as st
from multipage import MultiPage
from pages import project1 as p1
from pages import project2 as p2
from pages import project3 as p3
from pages import project4 as p4
from pages import project5 as p5

from pages import intro

app = MultiPage()

st.title('Project')


app.add_page("메인 페이지",intro.app)
app.add_page("가상 환경 구축", p1.app)
app.add_page("Streamlit", p2.app)
app.add_page("과제1", p3.app)
app.add_page("과제2",p4.app)
app.add_page('과제2-2', p5.app)


app.run()








