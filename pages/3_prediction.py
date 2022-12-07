
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


DUAL_MODEL_PATH = 'models/dual_feed_model'
NLP_MODEL_PATH = 'models/nlp_model'
MODEL = load_model(NLP_MODEL_PATH)

st.markdown('## Is that website a scam?')

st.markdown("Enter a URL and we'll look at the landing page to see if it's a scam!")

website = st.text_input('Enter URL in http:// or https:// format:')

make_predict = st.button('Click to see if that website is a scam!')

## NLP Prediction
if make_predict:
    prediction = predict_nlp(MODEL, website)

    if prediction:
        out_text = prediction[0][0] * 100

        st.success(f'Probability of this site being a scam is {out_text: .2f} %!')


# ## Dual Prediction
# if make_predict:
#     prediction = predict_dual(MODEL, website)[0][0] * 100

#     if prediction:
#         out_text = prediction

#         st.success(f'Probability of this site being a scam is {out_text: .3f} %!')
