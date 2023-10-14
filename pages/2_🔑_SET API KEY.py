import streamlit as st
import template
import os, openai
template.init(st)
st.set_page_config(page_title="Document Q&A-Set Api key", page_icon=":left_speech_bubble:")
with st.sidebar:
    st.title("Document Chat App :page_facing_up:")
    st.markdown(template.TITLE_TEXT)

__user_entered_api_key = st.text_input('Enter your OpenAI Api key')

__user_response = st.button("Submit")


if __user_response:
    if len(__user_entered_api_key) > 30:
        st.session_state['api_key'] = __user_entered_api_key
        openai.api_key = st.session_state['api_key']
        os.environ["OPENAI_API_KEY"] = st.session_state['api_key']
        st.success("Api key set successfully.")
    elif __user_entered_api_key == "":
        st.warning("Input text field is blank.")
    else:
        st.warning('Api key is seems invalid please enter valid one.')

st.json({"Api key": st.session_state['api_key']})