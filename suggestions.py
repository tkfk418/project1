# 건의사항 탭
import streamlit as st
import sqlite3
import time
import pandas as pd

conn = sqlite3.connect('suggestion.db', check_same_thread=False)
cur = conn.cursor()

# 테이블 생성
def create_tb():
    cur.execute('CREATE TABLE IF NOT EXISTS suggestion(author CHAR, email VARCHAR, title TEXT, comment MEDIUMTEXT, date TEXT, status TEXT)' )
    conn.commit()

# db 입력
def add_data(author, pword, title, date, comment, status):
    params = (author, pword, title, str(date), comment, status)
    cur.execute("INSERT INTO suggestion(author, email, title, date, comment, status) VALUES (?,?,?,?,?,?)",params)
    conn.commit()

# 목록 불러오기
def sugg_list():
    cur.execute('SELECT author, title, date, comment, status FROM suggestion')
    sugg = cur.fetchall()
    return sugg

# # 수정 (update)
# def data_update(username):
#     pass
# # 삭제 (delete)
# def data_delete(username):
#     cur.execute('DELETE FROM suggestion WHERE AUTHOR =:AUTHOR' ,{'AUTHOR':author})
#     conn.commit()
#     # conn.close()

# 검색 (작성자명)
def get_by_author(author):
	cur.execute("SELECT author, title, date, comment, status FROM suggestion WHERE author like '%{}%'".format(author))
	data = cur.fetchall()
	return data
# 검색(제목)
def get_by_title(title):
	cur.execute("SELECT author, title, date, comment, status FROM suggestion WHERE title like '%{}%'".format(title))
	data = cur.fetchall()
	return data
# 검색(내용)
def get_by_comment(comment):
	cur.execute("SELECT author, title, date, comment, status FROM suggestion WHERE comment like '%{}%'".format(comment))
	data = cur.fetchall()
	return data

# 처리상태 수정
def update_status(email):
    cur.execute('UPDATE suggestion SET status = "처리완료" WHERE email="{}"'.format(email))
    conn.commit()
def recover_status(email):
    cur.execute('UPDATE suggestion SET status = "접수" WHERE email="{}"'.format(email))
    conn.commit()


# ▲ DB 관련
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

def run_suggestions():
    st.subheader('건의사항')

    # 문의사항 입력
    with st.expander("문의하기"):
        form = st.form(key="annotation")
        with form:
            create_tb()
            cols = st.columns((1,1))
            author = cols[0].text_input("작성자명 ", max_chars = 12)
            email = cols[1].text_input("이메일 ")
            title = st.text_input("제목", max_chars = 50)
            comment = st.text_area("내용 ")
            submit = st.form_submit_button(label="작성")
            date = time.strftime('%Y.%m.%d %H:%M')
            status = "접수"
            if submit:
                
                # 내용란에 아래 글 입력, 이메일에 처리된 이메일 입력시 "처리완료" 혹은 "접수"로 변경함
                if comment == "ok_myroomadmin":
                    update_status(email)

                elif comment == "no_myroomadmin":
                    recover_status(email)

                else :
                    add_data(author, email, title, comment, date, status)
                    st.success("문의하신 내용이 접수되었습니다! 답변은 작성해주신 이메일로 발송됩니다. 감사합니다.")
                    st.balloons()

     # 검색
    with st.expander("검색"):
        cols = st.columns((1,1,1))
        search_term = cols[0].text_input('검색')
        search_option = cols[1].selectbox("검색옵션",("내용","작성자명","제목"))
        if cols[2].button("검색"):
                if search_option == "내용":
                    result=get_by_comment(search_term)
                elif search_option =="작성자명":
                    result=get_by_author(search_term)
                elif search_option =="제목":
                    result=get_by_title(search_term)
                s_result = pd.DataFrame(result, columns=['작성자명', '제목', '내용', '작성시각', '상태'])
                st.dataframe(s_result, use_container_width=True)


    # 목록
    container = st.container()
    with container:
        list = sugg_list()
        # st.write(list)
        df = pd.DataFrame(list, columns=['작성자명', '제목', '내용', '작성시각', '상태'])
        # st.dataframe(df.style.set_properties(subset=['내용'], **{'width': '1000px'}))
        st.dataframe(df, use_container_width=True)
        # st.table(df)