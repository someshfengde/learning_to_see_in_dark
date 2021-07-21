from numpy.lib.shape_base import expand_dims
import streamlit as st
from functionality import *
from about_us import *
from introduction import *

st.title("Learning to See in Dark Implementation")
app_mode = st.sidebar.selectbox(
    "Choose the app mode", ["Show instructions", "Run the app", "Source code"]
)

if st.sidebar.button(label="show contributors"):
    func()
else:
    if app_mode == "Show instructions":
        show_introduction()
        st.sidebar.success('To continue select "Run the app".')
    elif app_mode == "Source code":
        t1 = st.title("Code:")
        m1 = st.markdown(
            "## [github link](https://github.com/someshfengde/learning_to_see_in_dark)"
        )
        code1 = st.code(get_file_content_as_string("app.py"))
        title_1 = st.title("Functionality")
        code2 = st.code(get_file_content_as_string("functionality.py"))
    elif app_mode =='Run the app':
        # st.balloons()
        run_the_app()
