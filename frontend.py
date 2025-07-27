import streamlit as st
import requests

st.set_page_config(
    page_title="Fun & Advice Generator",
    page_icon="🎭"
)   


st.title("🎉 Fun Generator App")
st.write("Click the buttons below to get a random joke or life advice.")

col1,col2=st.columns(2)

with col1:
    if st.button("Tell me a Joke"):
        res = requests.get("http://localhost:5000/joke")
        if res.status_code==200:
            data = res.json()
            st.success(data["setup"])
            st.info(data["punchline"])
        else:
            st.error("Failed to get Joke!!")

    
with col2:
    if st.button("Give Me Advice"):
        res = requests.get("http://localhost:5000/advice")
        if res.status_code==200:
            data = res.json()
            st.success(data["advice"])
        else:
            st.error("Falied to Get Advice")

