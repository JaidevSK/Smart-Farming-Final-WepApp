# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:01:07 2023

@author: jaide
"""

import PIL
import streamlit as st


st.set_page_config(
    page_title="Field Image Viewer",
    page_icon="📷",
    layout="wide",
    initial_sidebar_state="expanded"
)

f_5m=PIL.Image.open("img5m.jpg")
f_30m=PIL.Image.open("img30m.jpg")
f_50m=PIL.Image.open("img50m.jpg")
f_100m=PIL.Image.open("img100m.jpg")
f_120m=PIL.Image.open("img120m.jpg")
st.markdown("<h1 style='text-align: center;'>Field Map (Drone View)</h1>", unsafe_allow_html=True)

st.write("Provides the view of the field map from various heights in an interactive way.")

height = st.select_slider('Altitude', options=[10,30,50,75,100])
v_range = st.slider('Select the %range of the vertical part of the image to be seen', 0.0, 100.0, (25.0, 75.0))
h_range = st.slider('Select the %range of the horizontal part of the image to be seen', 0.0, 100.0, (25.0, 75.0))
date = st.date_input("Select the date of the data to be seen")

if height==10:
    width, height = f_5m.size
    left = (width/100)*h_range[0]
    top = (height/100)*v_range[0]
    right = (width/100)*h_range[1]
    bottom = (height/100)*v_range[1]
    f_5m1 = f_5m.crop((left, top, right, bottom))
    st.image(f_5m1)
    
elif height==30:
    width, height = f_30m.size
    left = (width/100)*h_range[0]
    top = (height/100)*v_range[0]
    right = (width/100)*h_range[1]
    bottom = (height/100)*v_range[1]
    f_20m1 = f_30m.crop((left, top, right, bottom))
    st.image(f_20m1)
elif height==50:
    width, height = f_50m.size
    left = (width/100)*h_range[0]
    top = (height/100)*v_range[0]
    right = (width/100)*h_range[1]
    bottom = (height/100)*v_range[1]
    f_50m1 = f_50m.crop((left, top, right, bottom))
    st.image(f_50m1)
elif height==75:
    width, height = f_100m.size
    left = (width/100)*h_range[0]
    top = (height/100)*v_range[0]
    right = (width/100)*h_range[1]
    bottom = (height/100)*v_range[1]
    f_80m1 = f_100m.crop((left, top, right, bottom))
    st.image(f_80m1)
elif height == 100:
    width, height = f_120m.size
    left = (width/100)*h_range[0]
    top = (height/100)*v_range[0]
    right = (width/100)*h_range[1]
    bottom = (height/100)*v_range[1]
    f_100m1 = f_120m.crop((left, top, right, bottom))
    st.image(f_100m1)

