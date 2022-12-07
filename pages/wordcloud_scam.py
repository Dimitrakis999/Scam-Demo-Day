####### Useless notebook just to create notebook
#######



import streamlit as st
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from PIL import Image
import random

df_scam_text = pd.read_csv('/home/zamanay/code/Dimitrakis999/Scam-Demo-Day/data/ayoob_text_prediction.csv', index_col=0)

wordcloud_scam = WordCloud(width=1000, height=1000, max_words=50).generate(df_scam_text['text'][0])
wordcloud_scam.to_file("scam_words.png")

wordcloud_scam2 = WordCloud(width=1000, height=1000, max_words=50).generate(df_scam_text['text'][1])
wordcloud_scam2.to_file("scam_words2.png")

wordcloud_scam3 = WordCloud(width=1000, height=1000, max_words=50).generate(df_scam_text['text'][2])
wordcloud_scam3.to_file("scam_words3.png")

wordcloud_scam4 = WordCloud(width=1000, height=1000, max_words=50).generate(df_scam_text['text'][3])
wordcloud_scam4.to_file("scam_words4.png")

wordcloud_scam5 = WordCloud(width=1000, height=1000, max_words=50).generate(df_scam_text['text'][4])
wordcloud_scam5.to_file("scam_words5.png")
