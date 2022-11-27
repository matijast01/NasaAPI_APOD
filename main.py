import streamlit as st
import requests

api_key = st.secrets["APIKEY"]
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request1 = requests.get(url)
content = request1.json()

image_url = content["hdurl"]
explanation = content["explanation"]
title = content["title"]

if not explanation.find("Your Sky Surprise:") == -1:
    explanation = explanation[:explanation.find("Your Sky Surprise:")]

request2 = requests.get(image_url)
image = request2.content

st.title(title)
st.image(image)
st.write(explanation)
