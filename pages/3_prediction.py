
import streamlit as st
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from PIL import Image
import random

#Live demo of model
#Takes URL and spits out image (and wordcloud)
#And gives us a probability that website is scam

st.text_input("Enter the URL here")
