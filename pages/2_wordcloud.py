import streamlit as st
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from PIL import Image
import random

#website = st.text_input("Enter the URL here")

st.markdown("""# Is text more helpful?""")

#Function to scrape text from selected URL
#Should return a list of strings that can generate wordcloud

# def scrape_this_url():
#     url = ''
#     text = request.get( ... )
#     return text


#Run a pre-selected list of scam and safe URLs through the function
#and store text for each in a variable

# URLs_scam = ['url_1', 'url_2', 'url_3', 'url_4', 'url_5']
# URLs_safe = ['url_1', 'url_2', 'url_3', 'url_4', 'url_5']

# for url in range(len(URLs_scam)+1):
#     scam_text_1 = scrape_this_url(URLs_scam[url])
#     scam_text_2 = scrape_this_url(URLs_scam[url])
#     scam_text_3 = scrape_this_url(URLs_scam[url])
#     scam_text_4 = scrape_this_url(URLs_scam[url])
#     scam_text_5 = scrape_this_url(URLs_scam[url])

# for url in range(len(URLs_safe)+1):
#     safe_text_1 = scrape_this_url(URLs_safe[url])
#     safe_text_2 = scrape_this_url(URLs_safe[url])
#     safe_text_3 = scrape_this_url(URLs_safe[url])
#     safe_text_4 = scrape_this_url(URLs_safe[url])
#     safe_text_5 = scrape_this_url(URLs_safe[url])


#Load text data from scam URLs
@st.experimental_singleton
def load_csv_text():
    df_scam_text = pd.read_csv('data/scam_text.csv', index_col=0)
    df_legit_text = pd.read_csv('data/legit_text.csv', index_col=0)
    return df_scam_text, df_legit_text

df_scam_text, df_legit_text = load_csv_text()

##Generating Wordcloud
full_text = df_scam_text['text'][0]#.astype('str')
#one_big_string = ''.join(full_text.tolist())
wordcloud = WordCloud(width=1000, height=1000, max_words=50).generate(full_text)

#Generating second Wordcloud
full_text = df_scam_text['text'][1]#.astype('str')
#one_big_string = ''.join(full_text.tolist())
wordcloud_2 = WordCloud(width=1000, height=1000, max_words=50).generate(full_text)


# Display Wordclouds side by side:

count = 0

answer1 = 'Website A'

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

    with col2:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud_2, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()


with st.form(key='first_q', clear_on_submit=True):
    result1 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result1 == answer1:
    st.markdown('YOU DID IT')
    count +=1
else:
    st.markdown('YOU BEEN SCAMMED!')


answer2 = 'Website B'

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

    with col2:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud_2, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

with st.form(key='second_q', clear_on_submit=True):
    result2 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result2 == answer2:
    st.markdown('YOU DID IT')
    count+=1
else:
    st.markdown('YOU BEEN SCAMMED!')

answer3 = 'Website B'
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

    with col2:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud_2, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

with st.form(key='third_q', clear_on_submit=True):
    result3 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result3 == answer3:
    st.markdown('YOU DID IT')
    count+=1
else:
    st.markdown('YOU BEEN SCAMMED!')

answer4 = 'Website A'
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

    with col2:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud_2, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

with st.form(key='fourth_q', clear_on_submit=True):
    result4 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result4 == answer4:
    st.markdown('YOU DID IT')
    count+=1
else:
    st.markdown('YOU BEEN SCAMMED!')

answer5 = 'Website B'
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

    with col2:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud_2, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

with st.form(key='fifth_q', clear_on_submit=True):
    result5 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result5 == answer5:
    st.markdown('YOU DID IT')
    count+=1
else:
    st.markdown('YOU BEEN SCAMMED!')


#Audience score
st.write(f"You got {count} out of 5 correct")

#Model score


#Display overall wordcloud for all scam and safe websites


st.markdown('Wordclouds of scam and safe websites are quite similar')

full_text = df_scam_text['text'].astype('str')
one_big_string = ''.join(full_text.tolist())
wordcloud1 = WordCloud(width=1000, height=1000, max_words=50, background_color='white', min_word_length=3).generate(one_big_string)

full_text_2 = df_legit_text['text'].astype('str')
one_big_string_2 = ''.join(full_text_2.tolist())
wordcloud2 = WordCloud(width=1000, height=1000, max_words=50, background_color='white', min_word_length=3).generate(one_big_string_2)

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud1, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

    with col2:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud2, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()




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
