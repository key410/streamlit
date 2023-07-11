# 1.Hello world
import streamlit as st

# タイトル、ヘッダー、テキストを出力
st.title("Hello world!!")
st.header("header")
st.write("text write")

# streamlitの各部品を出力
st.button("ボタン")
st.selectbox("select", ("sel1", "sel2"))
st.multiselect("multiselect", ("sel1", "sel2"))
st.radio("radio", ("あいうえお", "かきくけこ"))

st.text_input("テキストボックス")
st.text_area("テキストエリア")

st.slider("スライダー", 0, 10, 5)