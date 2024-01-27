# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:56:26 2023

@author: jaide
"""


import streamlit as st
st.title("Project Smart Farming")
st.header("Soil Suitability Analysis")
typ = st.radio("How would you like to use this?", ["Soil Suitability Map Generator", "Individual Sample Testing"])

if typ == "Soil Suitability Map Generator":
    st.file_uploader("Input the .csv file of the Field")
else:
    st.number_input("Enter the Value of N")
    st.number_input("Enter the Value of P")
    st.number_input("Enter the Value of K")
    st.number_input("Enter the Value of pH")
    st.number_input("Enter the Value of Salinity")
    st.number_input("Enter the Value of Moisture Content")
    st.number_input("Enter the Value of Temperature")
    s = st.button("Submit")
    if s:
        st.write("The suitability index is 0.8")
        st.write("The range is 0-1. 1 is good; 0 is bad.")




st.sidebar.link_button("Go to Data Uploading Page", "https://project-smart-farming-vd6eonndrahxbzdq7sybvv.streamlit.app/")
st.sidebar.link_button("Go to Datalog", "https://project-smart-farming-ynd8tuet7bvfplkmbdmt8t.streamlit.app/")
st.sidebar.link_button("Go to Image Viewer", "https://project-smart-farming-zdgdgxvdjwjhzdjayfsoyj.streamlit.app/")
st.sidebar.link_button("Go to Weed Density Visualiser", "https://project-smart-farming-ztxhdu7jtbbvnpgpujlfdg.streamlit.app/")
st.sidebar.link_button("Go to Yield Prediction Page", "https://project-smart-farming-bbtrh6txamftuhp2svgrf4.streamlit.app/")
st.sidebar.link_button("Go to Soil Suitability Analysis Page", "https://project-smart-farming-rl8ttyplxcidujmvjqzdtt.streamlit.app/")
st.sidebar.link_button("Go to Type-Wise Weed Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/")
st.sidebar.link_button("Go to Crop Density Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/")
st.sidebar.link_button("Go to Cotton Bud Lifecycle Stage Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/")
st.sidebar.link_button("Go to Disease, Pest and Deficiency distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/")
st.sidebar.link_button("Go to  Cotton Bud Counter and Visualiser Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/")
st.sidebar.link_button("Go to Weather, Prices and other Information Page", "https://mausam.imd.gov.in/imd_latest/contents/satellite.php")
st.sidebar.link_button("Go to Main Page", "https://project-smart-farming-vefkkxyjh72zcdmf4pgzbs.streamlit.app/")
