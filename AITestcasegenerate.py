import streamlit as st
import pandas as pd
from io import StringIO

st.title('XC AI Assited Test Cases Generator')


df = pd.DataFrame({
    'firstoption': ['Select','L&A', 'P&C', 'Re-Insurance'],
    })

af = pd.DataFrame({
    'secondoption': ['Select','USA', 'Austrailia', 'UK','Asia'],
    })

tf = pd.DataFrame({
    'thrirdoption': ['Select','Motor', 'Home', 'Marine','Fire','Auto'],
    })


optionfr = st.sidebar.selectbox(
    'Which Insurance type you want to select?',
     df['firstoption'])

optionse = st.sidebar.selectbox(
    'Which Region you want to select?',
     af['secondoption'])


optiontr = st.sidebar.selectbox(
    'Which Line of Business you want to select?',
     tf['thrirdoption'])



uploaded_file = st.sidebar.file_uploader("Choose a file_(User Sories/BRD/Acceptance_Criteria Doc)")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)






st.sidebar.text_input("Acceptance Criteria", key="Acceptance Criteria")

st.sidebar.button("Generate Test Case", key="Generate Test Case")

if st.session_state.get("Generate Test Case"):




	









