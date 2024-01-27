# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 10:36:27 2023

@author: jaide
"""

import streamlit as st

st.title("Project Smart Farming")
st.header("Login Page")
u=st.text_input("Username")
p=st.text_input("Password")
if st.button("Submit"):
    if u=="username" and p=="password":
        st.write("Authentication Successful")
        st.link_button("Go to Main Page", "https://project-smart-farming-vefkkxyjh72zcdmf4pgzbs.streamlit.app/")
    else:
        st.write("Authentication Failed. Reload and Try Again...")
        
