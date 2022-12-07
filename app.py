import streamlit as st
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from PIL import Image
import random

#website = st.text_input("Enter the URL here")

st.markdown("""# Can you spot a scam website?""")

# URL_scam = {image_1: 'https://infinity-savings.xyz/',
#         image_2: 'https://legacy-tradesfx.online/',
#         image_3: 'http://www.fxtradingstation.co.uk/',
#         image_4: 'https://moneyadvicehelp.co.uk/'
#         image_5: 'https://www.deermarket.online/',
#         image_6: 'https://completepromarkets.com/',
#         image_7: 'https://castle-invest.com/',
#         image_8: 'https://www.coastheritage-invest.com/',
#         image_9: 'https://coinexpressmarket.com/',
#         image_10: 'https://www.nowloan.co.uk/',
#         image_11: 'https://fxfortrade.com/',
#         image_12: 'https://awesomeaussieshepherd.com/'}


count = 0

answer1 = 'Website A'
image_A = Image.open('images/scam/image_1.png')
image_B = Image.open('images/scam/image_3.png')
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_A, caption = 'Website A')
    with col2:
        st.image(image_B, caption = 'Website B')

with st.form(key='first_q', clear_on_submit=True):
    result1 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result1 == answer1:
    st.markdown('YOU DID IT')
    count +=1
else:
    st.markdown('YOU BEEN SCAMMED!')



answer2 = 'Website B'
image_A = Image.open('images/scam/image_2.png')
image_B = Image.open('images/scam/image_5.png')

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_A, caption = 'Website A')
    with col2:
        st.image(image_B, caption = 'Website B')

with st.form(key='second_q', clear_on_submit=True):
    result2 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result2 == answer2:
    st.markdown('YOU DID IT')
    count+=1
else:
    st.markdown('YOU BEEN SCAMMED!')

answer3 = 'Website B'
image_A = Image.open('images/scam/image_5.png')
image_B = Image.open('images/scam/image_6.png')
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_A, caption = 'Website A')
    with col2:
        st.image(image_B, caption = 'Website B')

with st.form(key='third_q', clear_on_submit=True):
    result3 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result3 == answer3:
    st.markdown('YOU DID IT')
    count+=1
else:
    st.markdown('YOU BEEN SCAMMED!')

answer4 = 'Website A'
image_A = Image.open('images/scam/image_4.png')
image_B = Image.open('images/scam/image_7.png')
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_A, caption = 'Website A')
    with col2:
        st.image(image_B, caption = 'Website B')

with st.form(key='fourth_q', clear_on_submit=True):
    result4 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result4 == answer4:
    st.markdown('YOU DID IT')
    count+=1
else:
    st.markdown('YOU BEEN SCAMMED!')

answer5 = 'Website B'
image_A = Image.open('images/scam/image_8.png')
image_B = Image.open('images/scam/image_5.png')
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_A, caption = 'Website A')
    with col2:
        st.image(image_B, caption = 'Website B')

with st.form(key='fifth_q', clear_on_submit=True):
    result5 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result5 == answer5:
    st.markdown('YOU DID IT')
    count+=1
else:
    st.markdown('YOU BEEN SCAMMED!')

# baseline_score = 0.5
#animation flipping a coin

dumb_answer_1 = random.randint(0, 1)
dumb_answer_2 = random.randint(0, 1)
dumb_answer_3 = random.randint(0, 1)
dumb_answer_4 = random.randint(0, 1)
dumb_answer_5 = random.randint(0, 1)

dumb_score = dumb_answer_1 + dumb_answer_2 + dumb_answer_3 + dumb_answer_4 + dumb_answer_5

st.write(f"The dumbest model flipped a coin and got a score of {dumb_score}")


#Audience score
st.write(f"You got {count} out of 5 correct")

#Model score
