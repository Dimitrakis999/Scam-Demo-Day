import streamlit as st
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from PIL import Image


#st.markdown("""# Scam Spotter
## Not sure about a website?""")

#website = st.text_input("Enter the URL here")

st.markdown("""# Can you spot a scam website?""")

images = ['data/image_v4.jpg', 'data/robber_image_v3.png']
captions = ['Website A','Website B']

st.image(images,width=350, caption=captions)

#Define function that takes two screenshot (one scam, one legit)
#from two random URLs (one scam, one legit)

# your_answer = st.multiselect(
#     'Which of the two websites is a scam?',
#     ['Website A', 'Website B']) #max_selections=1)

#st.write('You selected:', your_answer)



# URL = {image_1: 'https://infinity-savings.xyz/',
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







#scam_URLs = ['https://infinity-savings.xyz/',
        # 'https://legacy-tradesfx.online/',
        # 'http://www.fxtradingstation.co.uk/',
        # 'https://moneyadvicehelp.co.uk/'
        # 'https://www.deermarket.online/',
        # 'https://completepromarkets.com/',
        # 'https://castle-invest.com/',
        # 'https://www.coastheritage-invest.com/',
        # 'https://coinexpressmarket.com/',
        # 'https://www.nowloan.co.uk/',
        # 'https://fxfortrade.com/',
        # 'https://awesomeaussieshepherd.com/']

#safe_URLs = ['SOME SAFE WEBSITES']



# image1 = Image.open('images/image_1.png')
# st.image(image1, width=700)

#generate 2 sets of random int < 10 for scam & safe images
#load images using f string

# random_set_scam = [1,2,3,4,5]

# random_set_safe = [1,2,3,4,5]

#loading and displaying screenshot of scam website


answer1 = 'Website A'
image_A = Image.open('images/scam/image_1.png')
image_B = Image.open('images/safe/image_1.png')
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_A, caption = 'Website A')
    with col2:
        st.image(image_B, caption = 'Website B')


answer2 = 'Website B'
image_A = Image.open('images/safe/image_2.png')
image_B = Image.open('images/scam/image_2.png')
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_A, caption = 'Website A')
    with col2:
        st.image(image_B, caption = 'Website B')

answer3 = 'Website B'
image_A = Image.open('images/safe/image_3.png')
image_B = Image.open('images/scam/image_3.png')
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_A, caption = 'Website A')
    with col2:
        st.image(image_B, caption = 'Website B')


answer4 = 'Website A'
image_A = Image.open('images/scam/image_4.png')
image_B = Image.open('images/safe/image_4.png')
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_A, caption = 'Website A')
    with col2:
        st.image(image_B, caption = 'Website B')

answer5 = 'Website B'
image_A = Image.open('images/safe/image_5.png')
image_B = Image.open('images/scam/image_5.png')
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_A, caption = 'Website A')
    with col2:
        st.image(image_B, caption = 'Website B')




# images = ['data/image_v4.jpg', 'data/robber_image_v3.png']
# captions = ['Website A','Website B']

# st.image(images,width=350, caption=captions)


# safe = []
# for random_number in random_set_safe:
#     safe.append(f'images/scam/image_{random_number}.png')


# scam = []




with st.form(key='first_q', clear_on_submit=True):
    result1 = st.selectbox(label='Which website?', options=['','Website A', 'Website B'])
    st.form_submit_button(label='Submit')

if result1 == answer1:
    st.markdown('YOU DID IT')
else:
    st.markdown('YOU BEEN SCAMMED!')




#Define function to calculate final score
#Encode options to pick
#Scam is 1. Legit is 0
#Calculate perfect score
#Calculate final score/perfect score

# baseline_score = 0.5
#animation flipping a coin
# st.write("The dumbest model flipped a coin five times and got a score of f'{baseline_score}'")


# your_score = 0.75

# st.write("You got a score of f'{your_score}'")

# #Define function to get accuracy based on those five random pairings
# #

# model_score = 0.85

# st.write("Our model got a score of f'{model_score}'")







# @st.experimental_singleton
# def load_csv():
#     df_scam = pd.read_csv('data/final_scam_df.csv', index_col=0)
#     df_legit = pd.read_csv('data/final_legit_df.csv', index_col=0)
#     return df_scam, df_legit

# df_scam, df_legit = load_csv()

#st.dataframe(df_scam)

#df_scam[0][2]



# if website==df_scam[0]['website']:
#     st.write('This website is probably scam'
#              'Think twice before trusting this website'
#             )
# else:
#     st.write('This website is probably legit')


#Generating Worldcloud
#Load csv

#@st.experimental_singleton
# def load_csv_text():
#     df_scam_text = pd.read_csv('data/scam_text.csv', index_col=0)
#     df_legit_text = pd.read_csv('data/legit_text.csv', index_col=0)
#     return df_scam_text, df_legit_text

# df_scam_text, df_legit_text = load_csv_text()

#get wordcloud for scam websites
# full_text = df_scam_text['text'].astype('str')
# one_big_string = ''.join(full_text.tolist())
# wordcloud = WordCloud().generate(one_big_string)

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
