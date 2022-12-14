import streamlit as st
#import numpy as np
import pandas as pd
from wordcloud import WordCloud
#import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
#from PIL import Image
#import random

#website = st.text_input("Enter the URL here")

st.markdown("""# Is text more helpful?""")

st. write("--")


#Load text data from scam URLs
@st.experimental_singleton
def load_csv_text():
    df_scam_text = pd.read_csv('data/scam_text_prediction.csv', index_col=0)
    df_legit_text = pd.read_csv('data/legit_text_prediction.csv', index_col=0)
    return df_scam_text, df_legit_text

df_scam_text, df_legit_text = load_csv_text()

##Generating Wordcloud

# full_text_scam = df_scam_text['text'][0]#.astype('str')
# #one_big_string = ''.join(full_text.tolist())
# wordcloud_scam = WordCloud(width=1000, height=1000, max_words=50).generate(df_scam_text['text'][0])
# wordcloud_scam.to_file("scam_words.png")
# #Generating second Wordsmcacloud
# full_text_legit = df_legit_text['text'][1]#.astype('str')
# #one_big_string = ''.join(full_text.tolist())
# wordcloud_legit = WordCloud(width=1000, height=1000, max_words=50).generate(df_legit_text['text'][0])
# wordcloud_legit.to_file("legit_words.png")

# wordcloud_scam2 = WordCloud(width=1000, height=1000, max_words=50).generate(df_scam_text['text'][1])
# wordcloud_scam2.to_file("scam_words2.png")
# #Generating second Wordsmcacloud
# full_text = df_legit_text['text'][1]#.astype('str')
# #one_big_string = ''.join(full_text.tolist())
# wordcloud_legit2 = WordCloud(width=1000, height=1000, max_words=50).generate(df_legit_text['text'][1])
# wordcloud_legit2.to_file("legit_words2.png")

# wordcloud_scam3 = WordCloud(width=1000, height=1000, max_words=50).generate(df_scam_text['text'][2])
# wordcloud_scam3.to_file("scam_words3.png")
# #Generating second Wordsmcacloud
# full_text = df_legit_text['text'][1]#.astype('str')
# #one_big_string = ''.join(full_text.tolist())
# wordcloud_legit3 = WordCloud(width=1000, height=1000, max_words=50).generate(df_legit_text['text'][2])
# wordcloud_legit3.to_file("legit_words3.png")

# # Display Wordclouds side by side:

# wordcloud_scam4 = WordCloud(width=1000, height=1000, max_words=50).generate(df_scam_text['text'][3])
# wordcloud_scam4.to_file("scam_words4.png")
# #Generating second Wordsmcacloud
# full_text = df_legit_text['text'][1]#.astype('str')
# #one_big_string = ''.join(full_text.tolist())
# wordcloud_legit4 = WordCloud(width=1000, height=1000, max_words=50).generate(df_legit_text['text'][3])
# wordcloud_legit4.to_file("legit_words4.png")

# wordcloud_scam5 = WordCloud(width=1000, height=1000, max_words=50).generate(df_scam_text['text'][4])
# wordcloud_scam5.to_file("scam_words5.png")
# #Generating second Wordsmcacloud
# full_text = df_legit_text['text'][1]#.astype('str')
# #one_big_string = ''.join(full_text.tolist())
# wordcloud_legit5 = WordCloud(width=1000, height=1000, max_words=50).generate(df_legit_text['text'][4])
# wordcloud_legit5.to_file("legit_words5.png")

count = 0


if 'key2' not in st.session_state:
    st.session_state['key2'] = 0

answer11 = 'Website A'

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image('images/wordclouds/scam/scam_words1.png')

    with col2:
        st.image('images/wordclouds/safe/legit_words.png')

with st.form(key='first_q2', clear_on_submit=True):
    result11 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result11 == '':
    st.markdown('')

elif result11 == answer11:
    st.markdown('YOU DID IT')
    #st.session_state['key2'] += 1

else:
    st.markdown('YOU BEEN SCAMMED!')

answer22 = 'Website B'

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image('images/wordclouds/safe/legit_words2.png')

    with col2:
        st.image('images/wordclouds/scam/scam_words2.png')

with st.form(key='second_q2', clear_on_submit=True):
    result22 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result22 == '':
    st.markdown('')

elif result22 == answer22:
    st.markdown('YOU DID IT')
    #st.session_state['key2'] += 1

else:
    st.markdown('YOU BEEN SCAMMED!')


answer33 = 'Website A'

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image('images/wordclouds/scam/scam_words3.png')

    with col2:
        st.image('images/wordclouds/safe/legit_words3.png')

with st.form(key='third_q2', clear_on_submit=True):
    result33 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result33 == '':
    st.markdown('')

elif result33 == answer33:
    st.markdown('YOU DID IT')
    #st.session_state['key2'] += 1

else:
    st.markdown('YOU BEEN SCAMMED!')



answer44 = 'Website A'
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image('images/wordclouds/scam/scam_words4.png')

    with col2:
        st.image('images/wordclouds/safe/legit_words4.png')

with st.form(key='fourth_q2', clear_on_submit=True):
    result44 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result44 == '':
    st.markdown('')

elif result44 == answer44:
    st.markdown('YOU DID IT')
    #st.session_state['key2'] += 1

else:
    st.markdown('YOU BEEN SCAMMED!')

answer55 = 'Website B'
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image('images/wordclouds/safe/legit_words5.png')

    with col2:
        st.image('images/wordclouds/scam/scam_words5.png')

with st.form(key='fifth_q2', clear_on_submit=True):
    result55 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result55 == '':
    st.markdown('')

elif result55 == answer55:
    st.markdown('YOU DID IT')
    #st.session_state['key2'] += 1

else:
    st.markdown('YOU BEEN SCAMMED!')

counter = 0
if result11 == answer11:
    counter += 1
if result22 == answer22:
    counter += 1
if result33 == answer33:
    counter += 1
if result44 == answer44:
    counter += 1
if result55 == answer55:
    counter += 1

#Audience score
st.write(f"You got {counter} out of 5 correct")

#Model score
st.write('Our model got 4 out of 5')


#Display overall wordcloud for scam and safe websites


st.markdown('Wordclouds of scam and safe websites are quite similar')

full_text = df_scam_text['text'].astype('str')
one_big_string = ''.join(full_text.tolist())
wordcloud1 = WordCloud(width=1000, height=1000, max_words=50, background_color='white', min_word_length=3).generate(one_big_string)
wordcloud1.to_file("overall_scam_wordcloud.png")

full_text_2 = df_legit_text['text'].astype('str')
one_big_string_2 = ''.join(full_text_2.tolist())
wordcloud2 = WordCloud(width=1000, height=1000, max_words=50, background_color='white', min_word_length=3).generate(one_big_string_2)
wordcloud2.to_file("overall_safe_wordcloud.png")

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image('images/overall_scam_wordcloud.png')


    with col2:
        st.image('images/overall_safe_wordcloud.png')




        # plt.imshow(wordcloud2, interpolation='bilinear')
        # st.set_option('deprecation.showPyplotGlobalUse', False)
        # plt.axis("off")
        # plt.show()
        # st.pyplot()




# wordcloud.to_file('scam_wordcloud.png')

#get wordcloud for legit websites
# full_text = df_legit_text['text'].astype('str')
# one_big_string = ''.join(full_text.tolist())

#add mask (shape) of the image

# mask = np.array(Image.open('data/image_v4.jpg'))
# wordcloud = WordCloud(stopwords=STOPWORDS,
#                mask=mask, background_color="white",
#                max_words=2000, max_font_size=256,
#                random_state=42, width=mask.shape[1],
#                height=mask.shape[0])
# wc = wordcloud.generate(one_big_string)



#wordcloud.to_file('legit_wordcloud.png')

# Display Wordcloud on page:
# st.set_option('deprecation.showPyplotGlobalUse', False)
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.show()
# st.pyplot()
