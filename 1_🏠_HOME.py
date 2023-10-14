import streamlit as st
import template
import utils

template.init(st)

st.set_page_config(page_title="Document Q&A", page_icon=":left_speech_bubble:")

with st.sidebar:
    st.title("Document Chat App :page_facing_up:")
    st.markdown(template.TITLE_TEXT)


def home_page():
    st.header("Chat with Document :speech_balloon:")
    document_path = st.file_uploader("Upload your PDF", type='pdf')

    if document_path is not None:
        with open("yourPdf/out.pdf", "wb") as f:
            f.write(document_path.getbuffer())
        btn = st.button("Process")
        st.session_state['pdf_path'] = "yourPdf/out.pdf"
        try:
            if btn:
                with st.spinner('please wait ...'):
                    utils.read_pdf()
                    utils.load_data()
                    st.success('Reading completed now open Start chat page to ask questions.')
        except Exception:
            st.error("App is running on Default or free openai api key for large document use your api key")


if __name__ == '__main__':
    home_page()
