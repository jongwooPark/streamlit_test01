import streamlit as st
import streamlit.components.v1 as components

def app():

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

    iframe_code = '''
    <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
        <iframe src="http://aumlee.biz/intranet/aumlee_ai/terminal_schedule.php" 
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
                allowfullscreen></iframe>
    </div>
    '''

    components.html(iframe_code, height=1500)