import streamlit as st

st.title("Public Veri ÜZerinden Yayınlama")

st.write("DF leri tanımladık")


import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1yOdL6g16ibLUiRVa41I0QGuA6RdMKe-rcifNc-5Rh08/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

#data = conn.read(spreadsheet=url, usecols=[0,1,4])
data = conn.read(spreadsheet=url)
st.dataframe(data)
