import streamlit as st 
from functionality import *

st.title('learning to see in dark implementation')
readme_text = st.markdown(get_file_content_as_string("Readme.md"))

st.sidebar.title("What to do")
app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Show instructions", "Run the app", "Show the source code"])
if app_mode == "Show instructions":
    st.sidebar.success('To continue select "Run the app".')
elif app_mode == "Show the source code":
    readme_text.empty()
    st.code(get_file_content_as_string("functionality.py"))
elif app_mode == "Run the app":
    readme_text.empty()
    run_the_app()


    

