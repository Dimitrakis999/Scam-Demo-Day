
import streamlit as st
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from PIL import Image
import random

from scam_spotter_web.main import predict_all
from scam_spotter_web.predict import load_model

#Live demo of model
#Takes URL and spits out image (and wordcloud)
#And gives us a probability that website is scam

MODEL_PATH = 'models/model2'
MODEL = load_model(MODEL_PATH)

st.markdown('## Is that website a scam?')

website = st.text_input('Enter URL here in https:// format')

predict = st.button('Click to see if that website is a scam!')

if predict:
    prediction = predict_all(MODEL, website)

    if prediction:
        out_text = prediction

        st.success(f'Probability of this site being a scam is {out_text}')
