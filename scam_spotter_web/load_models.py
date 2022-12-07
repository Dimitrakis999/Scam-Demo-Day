import tensorflow as tf
import streamlit as st

import nltk
from nltk.corpus import stopwords
from gensim.models import Word2Vec
import gensim.downloader as api
from keras.preprocessing.sequence import pad_sequences
nltk.download('stopwords')

# Dual Feed Functions
@st.experimental_memo(show_spinner=False)
def load_model(path):
    model = tf.keras.models.load_model(path)
    return model

# def predict_dual(model, X_image, X_text):
#     prediction = model.predict([X_image, X_text])
#     return prediction

# def predict_nlp(model, X_text):
#     prediction = model.predict(X_text)
#     return prediction
