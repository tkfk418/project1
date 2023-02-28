# 필요한 라이브러리 
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu


# 다른 파일의 함수를 불러온다
from menu_00_home.title import run_title
from menu_01_roomSearch.search import run_search
from menu_02_prediction.predict import run_predict
from menu_04_suggest.suggestions import run_suggestions
from update import update_data
from menu_03_chatbot.chatbot import chatrun


def main():

    st.title('🏘️내 방, 어디👀?')


    selected3 = option_menu(None, ["🏠Home", "🔎전월세 검색", "📊전세 예측",
    '🤖챗봇', '💬건의사항'], 
            # icons=['house', 'cloud-upload', "list-task", 'gear'], 
            menu_icon="cast", default_index=0, orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "gray", "font-size": "15px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#47C83E"},
        }
    )

    data = update_data()

    if selected3 == "🏠Home":
        run_title(data)

    elif selected3 == "🔎전월세 검색":
        run_search(data)

    elif selected3 == "📊전세 예측":
        run_predict(data)

    elif selected3 == "🤖챗봇":
        chatrun()

    elif selected3 == "💬건의사항":
        run_suggestions()

    else:
        selected3 == "🏠Home"

if __name__ == "__main__":
    main()