# 내 방 어디? v1(~2023.02.01)
[내 방 어디? 링크](https://tkfk418-project1-app-xgbcty.streamlit.app/)
![screensh](image/homepage.PNG)
***

## 목적
계약일 기준 2022년 1월 1일부터 현재까지의 **서울시 전/월세 실거래 데이터 기반 검색** 및 **전세 시세 예측** 부동산 웹 개발
***

## 팀 구성
- 사용언어 : <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white">
- 작업툴 : <img src="https://img.shields.io/badge/VS%20Code-007ACC?style=flat&logo=Visual%20Studio%20Code&logoColor=white">
- 인원 : 7명
- 주요 업무 : 데이터 분석, 데이터 시각화, 머신러닝 코드 구현, PPT 제작
- 기간 : 2023-01-30 - 2023-02-10
***

## 주요 기능
- 홈페이지
    - 서울시 전월세 실거래 현황(최근 한달순)
- 전월세 검색페이지
    - 원하는 지역구 및 동, 전/월세 구분 검색
    - 보증금, 월세, 임대면적 슬라이더 검색
- 전세 예측페이지
    - 지역 선택 후 날짜에 따른 보증금 막대그래프로 시각화
    - 날짜 선택 후 지역구별 평균 실거래가 지도 시각화
    - 전세 월평균, 월세 월평균 추이 꺾은선그래프 시각화
    - 월세, 전세 실거래 수 지역 순위 막대그래프 시각화
    - 선택한 지역구 전세 평균 예측 모델 시각화
- 건의사항페이지
    - 게시판 작성자, 이메일, 제목, 내용 저장을 위한 db 구축
    - 문의 내용 작성칸 구축
    - 게시판 목록 구현
    - 관리자모드
        - 처리상태 변경
***

## 설치 방법
### Windows
+ 버전 확인 
    - vscode : 1.74.1
    - python : 3.9.0
    - 라이브러리 :  pandas (1.5.3), numpy (1.24.1), plotly (5.13.0), matplotlib (3.6.3), streamlit (1.17.0), streamlit-option-menu (0.3.2), geopandas (0.12.2), google-cloud-bigquery(3.5.0), pandas-gbq(0.19.1), prophet(1.1.2), seaborn(0.12.2), openai(0.26.5), streamlit_chat(0.0.2.1)

+ 주요 라이브러리 설치
    - `pip install numpy, pandas, plotly, matplotlib, streamlit, streamlit-option-menu, geopandas, google-cloud-bigquery, pandas-gbq, prophet, seaborn, openai, streamlit_chat`

# 내방 어디? v2(2023.02.02~)

## 주요 기능 업데이트 내용
- 홈페이지
    - 실거래 현황(최근 한달순)
    - 전세 월평균, 월세 월평균 추이 꺾은선그래프 **시각화**
    - 월세, 전세 실거래 수에 따른 지역 순위 막대그래프 **시각화**
- 전월세 검색페이지
    - 전/월세 구분 검색 중 모두 검색할 수 있도록 **추가**
    - 보증금, 월세, 임대면적 최소/최대값 정해줄 수 있도록 **추가**
    - 보증금, 월세, 임대면적 최소/최대값과 슬라이더값 **동기화**

- 전세 예측페이지
    - 날짜 선택 후 지역구별 평균 실거래가 지도 **시각화**

- 건의사항페이지
    - 처리 상태 **추가**
    - 빈칸 입력시 에러메시지 **추가**
    - 관리자 기능
        - 처리 상태 변경 기능 **추가**
    - 검색 기능
        - 제목, 작성자명, 내용에 같은 내용 검색 기능 **추가**
        
# 내방 어디? v3(2023.02.07~)

## 주요 기능 업데이트 내용
- 홈페이지
    - 전세 월평균, 월세 월평균 추이 꺾은선그래프 **삭제**
    - 월세, 전세 실거래 수 지역 순위 막대그래프 **삭제**

- 전세 예측페이지
    - 전세 월평균, 월세 월평균 추이 꺾은선그래프 **시각화**
    - 월세, 전세 실거래 수에 따른 지역 순위 막대그래프 **시각화**
    - 날짜 및 자치구별 동 선택 후 동별 평균 실거래가 지도 **시각화**
    - 지역구 선택 후 최신 데이터를 기준으로 추후 30일간 전세 평균 예측 모델 **시각화**
      - (LSTM 모델, Prophet 모델)
- 챗봇 
    - 지역구 및 날짜 입력으로 실거래가 검색 기능 **추가**
    - 간단한 일상 대화 기능 **추가**
- 업데이트
    - 최신 부동산 데이터 **업로드**
    - 메일 오전 9시 5분 데이터 **갱신**
        - 배치 파일 사용
- 평균 함수화
    - 구별 전세 일 평균 **함수화**
    - 구별 전세 월 평균 **함수화**
    - 구별 월세 일 평균 **함수화**
    - 구별 월세 월 평균 **함수화**
    - 동별 전세 일 평균 **함수화**

### 한계점
- 날짜 및 자치구별 동 선택 후 동별 평균 실거래가 지도 시각화 실패
  - 실시간 데이터와 geojson 파일의 법정동 명의 다름으로 지도 시각화가 나오지 않음
  - 추후 업데이트 할 예정