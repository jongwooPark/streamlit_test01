import streamlit as st
from streamlit_option_menu import option_menu

import Aum_prompt_create, Aum_prompt_ana, Aum_Server, Aum_reg, Aum_link, Aum_library

# 사용자 정의 CSS 추가
st.markdown("""
    <style>
    .st-emotion-cache-13ln4jf {
        max-width: 130rem;
          padding: 2rem 1rem 10rem;
    }
    .viewerBadge_container__1QSob { 
        display: none; 
    }

[data-testid="stIFrame"]{
        height: 1200px;
}
[data-testid="stHeadingWithActionElements"]{
    text-align: center;
}
[data-testid="stHeader"] {
    display: none;
}
.header-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}
.header-container img {
    margin-right: 10px;
}
.header-container h1 {
    display: inline;
    margin: 0;
}
 </style>
    """,
    unsafe_allow_html=True
)



class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title" : title,
            "function" : function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title="엄이디퓨전",
                menu_icon="buildings-fill",
                options=["프롬프트 생성기", "프롬프트 분석기", "엄이디퓨전 서버","서버 링크", "서버 예약","라이브러리","실내인테리어", "투시도", "조감도","스케치","모형사진","이미지"],
                icons=["chat-left-text","chat-left-quote","pc-display-horizontal","link","stopwatch", "archive-fill","chevron-right","chevron-right", "chevron-right", "chevron-right","chevron-right","chevron-right"],
                default_index=5
            )


        if app == "프롬프트 생성기" :
            Aum_prompt_create.app()
        if app == "프롬프트 분석기" :
            Aum_prompt_ana.app()
        if app == "엄이디퓨전 서버" :
            Aum_Server.app()
        if app == "서버 예약" :
            Aum_reg.app()
        if app == "서버 링크" :
            js_code = """
            <script type="text/javascript">
                window.open('http://192.9.201.151:7860/?__theme=dark', '_blank', 'width=1600,height=1000,top=100,left=100');
            </script>
            """
            st.components.v1.html(js_code, height=0, width=0)
            Aum_link.app()

        if app == "실내인테리어" :
            Aum_library.app()
           


    # run()
app = MultiApp()
app.run()

