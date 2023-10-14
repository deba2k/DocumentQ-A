import streamlit as st

TITLE_TEXT = '''
    ## About:
    This is a LLM  powered chat bot.Now you can chat with your document.
    Connect your existing data sources to use this next gen. application.
    ## How to use :pushpin:
    - step 1: 
       #### :open_file_folder: Upload your document.
    - step 2:
        #### :key: Set your Open AI api key.
        [click here to create openAi api key](https://openai.com/product)
    - step 3:
        #### :thumbsup: Click on Submit :Now Now all set just ask questions.    
    '''

DEFAULT_API_KEY = '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'


def init(obj):
    # api_key variable for storing open ai api key
    if 'api_key' not in obj.session_state.keys():
        obj.session_state['api_key'] = "Default key"
    # pdf_pdf variable for storing pdf path
    if 'pdf_path' not in obj.session_state.keys():
        obj.session_state['pdf_path'] = ""


