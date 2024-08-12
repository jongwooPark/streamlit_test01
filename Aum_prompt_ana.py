import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
import os
import time
from openai import OpenAI

def app():
    st.title("엄이디퓨전 프롬프트 분석기")
    load_dotenv()
    API_KEY = os.environ['OPENAI_API_KEY']
    client = OpenAI(api_key=API_KEY)

    assistant_id = "asst_nM9e2EROxNoXyo6dZTSv5IXD"
    # 어시스트 이름 : 엄이디퓨전30_분석기

    if 'thread_id2' not in st.session_state:
        thread = client.beta.threads.create()
        st.session_state.thread_id2 = thread.id
    
    thread_id2 = st.session_state.thread_id2   

    thread_messages = client.beta.threads.messages.list(thread_id2)

    for msg in reversed(thread_messages.data):
        with st.chat_message(msg.role ):
            st.write(msg.content[0].text.value)

    prompt = st.chat_input("엄이프롬프 생성기에 생성할 프롬프트를 입력하세요")

    if prompt:
        thread_message = client.beta.threads.messages.create(
            thread_id2,
            role="user",
            content=prompt,
        )
        with st.chat_message(thread_message.role):
            st.write(thread_message.content[0].text.value)
        
        run = client.beta.threads.runs.create(
            thread_id=thread_id2,
            assistant_id="asst_WsA5nQ2kaYUXwPZbVygHVxCl"
        )

   
        with st.spinner('응답 기다리는중...'):

            while run.status != "completed":
                time.sleep(0.1)
                run = client.beta.threads.runs.retrieve(
                    thread_id=thread_id2,
                    run_id=run.id
                )


        thread_messages = client.beta.threads.messages.list(thread_id2)
            
        with st.chat_message(thread_messages.data[0].role):
            st.write(thread_messages.data[0].content[0].text.value)

