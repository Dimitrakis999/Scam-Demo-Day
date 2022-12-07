
import streamlit as st
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from PIL import Image

from scam_spotter_web.main import predict_dual, predict_nlp
from scam_spotter_web.load_models import load_model

# Live demo of model
# Takes URL and spits out image (and wordcloud)
# And gives us a probability that website is scam


DUAL_MODEL_PATH = 'models/model2'
NLP_MODEL_PATH = 'models/nlp_model.h5'
MODEL = load_model(DUAL_MODEL_PATH)

st.markdown('## Is that website a scam?')

website = st.text_input('Enter URL here in https:// format')

make_predict = st.button('Click to see if that website is a scam!')

if make_predict:
    prediction = predict_dual(MODEL, website)[0][0] * 100

    if prediction:
        out_text = prediction

        st.success(f'Probability of this site being a scam is {out_text: .3f} %!')
