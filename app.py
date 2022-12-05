import streamlit as st
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from PIL import Image


st.markdown("""# Scam Spotter
## Not sure about a website?""")

# sidebar to make the point


# context / stats about scams



#Scam_URLs = pd.read_('')



# @st.experimental_singleton
# def load_csv():
#     df_scam = pd.read_csv('data/final_scam_df.csv', index_col=0)
#     df_legit = pd.read_csv('data/final_legit_df.csv', index_col=0)
#     return df_scam, df_legit

# df_scam, df_legit = load_csv()

#st.dataframe(df_scam)

#df_scam[0][2]

website = st.text_input("Enter the URL here")


# if website==df_scam[0]['website']:
#     st.write('This website is probably scam'
#              'Think twice before trusting this website'
#             )
# else:
#     st.write('This website is probably legit')


#Generating Worldcloud
#Load csv

#@st.experimental_singleton
def load_csv_text():
    df_scam_text = pd.read_csv('data/scam_text.csv', index_col=0)
    df_legit_text = pd.read_csv('data/legit_text.csv', index_col=0)
    return df_scam_text, df_legit_text

df_scam_text, df_legit_text = load_csv_text()

#get wordcloud for scam websites
# full_text = df_scam_text['text'].astype('str')
# one_big_string = ''.join(full_text.tolist())
# wordcloud = WordCloud().generate(one_big_string)

# wordcloud.to_file('scam_wordcloud.png')

#get wordcloud for legit websites
full_text = df_legit_text['text'].astype('str')
one_big_string = ''.join(full_text.tolist())

#add mask (shape) of the image

mask = np.array(Image.open('data/image_v4.jpg'))
wordcloud = WordCloud(stopwords=STOPWORDS,
               mask=mask, background_color="white",
               max_words=2000, max_font_size=256,
               random_state=42, width=mask.shape[1],
               height=mask.shape[0])
wc = wordcloud.generate(one_big_string)



#wordcloud.to_file('legit_wordcloud.png')

# Display the generated image:
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()
