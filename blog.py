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
        /* 1. 제목 창 설정 */
        .st-key-title textarea {
            font-size: 32px !important;
            line-height: 1.6 !important;
            margin-left: 15px;
            margin-right: 15px;
            overflow: hidden;
        }
                
        /* 2. 본문 창 설정 */
        .st-key-body textarea {
            font-size: 24px !important;
            line-height: 1.6 !important;
            margin-left: 15px;
            margin-right: 15px;
            overflow: hidden;
        }
        
        /* 3. 가로선 위·아래 간격 설정 */
        hr {
            margin: 0px !important;
            width: 92% !important;
            margin-left: auto !important;
            margin-right: auto !important;
        }  
        
        /* 4. 제목·본문·가로선 전체 창 설정 */
        div[data-testid="stColumn"]:nth-child(2) {
            background-color: white;
            padding-top: 30px;
            padding-left: 50px;
            padding-right: 50px;
            border-radius: 10px !important
        }

        /* 5. 제목·본문 색깔 설정 */
        div[data-baseweb="base-input"] {
            background-color: white !important;
        }

        .stTextArea > div {
            border: none !important;
        }

        </style>
        """, unsafe_allow_html=True)

    # 3. 철자 오류 밑줄 삭제
    js = """
        <script>
            const txt_areas = window.parent.document.querySelectorAll('textarea');
            txt_areas.forEach(txt => {
                txt.spellcheck = false;
            });
        </script>
        """
    st.html(js)