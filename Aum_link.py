import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
import os
import time
from openai import OpenAI

def app():
    st.title("엄이디퓨전 서버 링크")