import streamlit as st

st.title("Welcome to Ojha ji's  website with using streamlit 😎")

st.header("📝Fill out your info below")

name = st.text_input("What is your name? ")
age = st.number_input("How old are you? ",min_value=0,max_value=100)
city = st.text_input("Entr your city: ")
contact = st.number_input("Enter Your cell number? ")

if st.button("Submit"):
    st.success("Thanks for submitting your info")
    st.write(f"👋Hey, **{name}**! age:  **{age}** belongs to **{city}** your contact: **{contact}** is selected for prize🎉")
st.markdown("---")
st.caption("Built with using Stremlit ❤️")
