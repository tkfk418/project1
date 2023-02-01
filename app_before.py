import streamlit as st
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import numpy as np
from streamlit_option_menu import option_menu


def main():

    st.title('월세 볼래?')
    (" ")
    (" ")
    (" ")

    selected = option_menu(None, ["🏠Home", " 🔎전월세 검색",  "📊전세vs월세?", '💬건의사항'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#ebb0b0"},
    })   
    
    submenu = st.sidebar.title('간편 검색')
    submenu_lists1 = ["영등포구", '관악구', '구구구']
    submenu_lists2 = ["영등포 1동", '영등포 2동', '영등포 3동']
    submenu_lists3 = ["30미만", '30이상 40미만', '40이상 50미만']
    submenu_lists4 = ["500미만", '500이상 2000이하', '2000이상 5000미만']
    submenu_lists5 = ["아파트", '오피스텔', '빌라']

    submenu = st.sidebar.selectbox('지역', submenu_lists1)
    submenu = st.sidebar.selectbox('동/읍/면', submenu_lists2)
    submenu = st.sidebar.selectbox('월세', submenu_lists3)
    submenu = st.sidebar.selectbox('보증금', submenu_lists4)
    submenu = st.sidebar.selectbox('건물 타입', submenu_lists5)
    submenu = st.sidebar.button('검색', type = 'primary')

    if (selected=='🔎전월세 검색'):
        pass


    elif (selected=='🏠Home'):        
        data = pd.read_csv('bds_data.csv', encoding='cp949')
        st.write(data.head())


    elif (selected=='💬건의사항'):
        title_input = st.text_input('제목')
        st.title(title_input)
        msg_input = st.text_area('내용', height=100)
        st.write(msg_input)
        password_input = st.text_input('비밀번호')
        st.title(password_input)
        st.button('등록')


        


    else:
        pass

    
       
    
    


if __name__ == "__main__":
    main()