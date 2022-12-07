import tensorflow as tf

import nltk
from nltk.corpus import stopwords
import string
from gensim.models import Word2Vec
import gensim.downloader as api
from keras.preprocessing.sequence import pad_sequences
nltk.download('stopwords')


MODEL_PATH = '../models/model2'

def load_model(path):
    model = tf.keras.models.load_model(path)
    return model

def model_predict(model, X_image, X_text):
    model.predict([X_image, X_text])


