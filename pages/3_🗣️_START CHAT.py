import streamlit as st
import template
import utils

template.init(st)
st.set_page_config(page_title="Document Q&A-Start chat", page_icon=":left_speech_bubble:")
with st.sidebar:
    st.title("Document Chat App :page_facing_up:")
    st.markdown(template.TITLE_TEXT)

try:
    if st.session_state['pdf_path'] != "":
        if "message" not in st.session_state:
            st.session_state["message"] = []

        # For showing the message in this page
        for message in st.session_state["message"]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        prompt = st.chat_input("Say something")

        if prompt:
            with st.chat_message("user"):
                st.markdown(prompt)

            st.session_state.message.append({"role": "user", "content": prompt})

            with st.chat_message("assistant"):
                with st.spinner("getting response"):
                    try:
                        response = utils.ask_question(prompt)  # actual method calling here
                        st.markdown(response.response)
                        st.session_state.message.append({"role": "assistant", "content": response})
                    except:
                        st.error("please upload your pdf again")


        def clear():
            if 'message' in st.session_state:
                st.session_state.message = []


        clear_chat = st.button("Clear chat", on_click=clear)
    else:
        st.warning("Please select pdf")
except TypeError:
    st.warning("Please set Api key first")
