# 전월세 검색 탭

import streamlit as st
import pandas as pd

def run_search():
    st.title('전월세 검색')
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')

    with st.sidebar():
        st.selectbox()