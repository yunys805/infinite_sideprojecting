import streamlit as st

# 1. 웹 기본 설정
st.set_page_config(page_title='블로그', layout='wide')
col1, col2, col3 = st.columns([1, 2.5, 1])

with col2:
    # 2. 제목·본문 창 생성
    st.text_area(label='', height=100, placeholder='제목', key='title')
    st.markdown('---')
    st.text_area(label='', height=1000, placeholder='본문을 입력하세요', key='body')

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap');

        /* =============== 1. streamlit 사전 설정 변경 =============== */
        /* 1. 창 크기 조절기 삭제 */
        textarea {
            resize: none !important;
        }
                
        /* 2. 창 하단 영어 문구 삭제 */
        div[data-testid="InputInstructions"] > span:nth-child(1) {
            visibility: hidden;
        }
        
        /* 3. 바탕·상단 바 색깔 변경*/
        .stApp, .stAppHeader {
            background-color: #f2eee6 !important;
        }

        /* =============== 2. 제목·본문 창 설정 =============== */
        /* 1. 제목·본문 창 공통 설정 */
        .st-key-title textarea,
        .st-key-body textarea {
            margin-left: 40px;
            margin-right: 40px;
            overflow: hidden;
            
            font-family: 'Nanum Gothic', sans-serif !important;
            color: black !important;
            letter-spacing: -0.05em !important;
            word-spacing: 0.1em !important;
            line-height: 1.7 !important;
        }
        div[data-baseweb="textarea"] {
            border: none !important;
        }

        /* 2. 제목 창 단독 설정 */
        .st-key-title textarea {
            font-size: 35px !important;
        }
                
        /* 3. 본문 창 단독 설정 */
        .st-key-body textarea {
            font-size: 24px !important;
        }
        
        /* 4. 가로선 위·아래·좌우 간격 설정 */
        hr {
            margin: 0px !important;
            width: 87% !important;
            margin-left: auto !important;
            margin-right: auto !important;
        }  
        
        /* 5. 제목·본문·가로선 전체 박스 설정 */
        div[data-testid="stColumn"]:nth-child(2) {
            background-color: white;
            padding-top: 30px;
            padding-left: 50px;
            padding-right: 50px;
            border: 1px solid #ddd !important;
            border-radius: 10px !important
        }

        /* 6. 제목·본문 창 색깔 설정 */
        div[data-baseweb="base-input"] {
            background-color: white !important;
        }

        </style>
                
        """, unsafe_allow_html=True)
    
  