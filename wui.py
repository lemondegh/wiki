import pandas as pd
import streamlit as st
import multiprocessing
from io import StringIO

def get_core_cnt():
    # Get the number of CPU cores
    num_cores = multiprocessing.cpu_count()

    print(f"Number of CPU cores: {num_cores}")

    return num_cores

# st.subheader('Wikipedia 데이터 추출')
st.markdown('**Wikipedia 데이터 추출**')

tot_cores = get_core_cnt()
cores_half = int(tot_cores / 2)

st.write("Seed 수집 정보")
col1, col2 = st.columns(2)

with col1:
    n = st.number_input('차시(DB에 있는 최대 차수 이하로 설정)', value = 5)
with col2:
    core_msg = '코어 수(시스템 코어 수 : {})'.format(tot_cores)
    cores = st.number_input(core_msg, min_value = 1, max_value = tot_cores, value = cores_half)

st.write("Seed 수집 차시 : ", n, ", 코어 수 : ", cores)

options = ['Upload seed file', 'Insert seed']
captions = ['Seed file 지정', '사용자가 seed 입력']
opt = st.radio('Input seed ptions', index=0, horizontal=True, options = options, captions = ['Seed file 지정', '사용자가 seed 입력'])


if opt == options[0]:
    uploaded_file = st.file_uploader('**Seed file**', accept_multiple_files=False)

    if uploaded_file is not None:
        with st.expander('Seed...'):
            dataframe = pd.read_excel(uploaded_file, index_col=0)
            # st.dataframe(dataframe, use_container_width=True)
            st.table(dataframe) 

        if uploaded_file is not None and st.button('Start extraction'):
            st.toast('Extraction started...', icon='❗')            
else:
    seed = st.text_input('Insert seed', placeholder='Insert seed here...')

    if len(seed) > 0 and st.button('Start extraction'):
        st.toast('Extraction started...', icon='❗')            
    
      
# if uploaded_file is not None and st.button('Start extraction'):
#     st.toast('Extraction started...', icon='❗')
                
#     import subprocess
#     cmd = ['python', '1. check_seed.py']
#     process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = process.communicate()
#     print(stdout.decode())
#     print(stderr.decode())        



# import streamlit as st

# file_uploader = st.file_uploader(label="Upload a file")

# hide_label = """
# <style>
#     .css-9ycgxx {
#         display: none;
#     }
# </style>
# """

# st.markdown(hide_label, unsafe_allow_html=True)



    