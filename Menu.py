import streamlit as st
import base64
st.set_page_config(
    page_title="Xử lý ảnh",

)

st.subheader(':gray[Nguyễn Ngọc Tuấn   21110936]')
st.subheader(':gray[Bùi Trọng Trí      21110933]')

import base64
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.imgur.com/CkF6i4v.jpeg");
background-size: 100%;
background-position: center;
background-repeat: no-repeat;
background-attachment: local;
}}

.subheader-text {{
    color: black;
}}

[data-testid="stSidebar"] > div:first-child {{
background-size: 180%;
background-position: center; 
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)