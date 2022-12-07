from scam_spotter_web.scrape import scrape_photo_text
from scam_spotter_web.text_processing import preprocess_pad
from scam_spotter_web.predict import model_predict, load_model

import tensorflow as tf

def predict_all(url, model):

    # Scrape image and text with selenium
    X_image, X_text = scrape_photo_text(url)

    # Process text from string to embedded array
    X_text = preprocess_pad(X_text)

    prediction = model_predict(model, X_image, X_text)

    return prediction

if __name__ == '__main__':
    url = 'https://www.barclays.co.uk/'
    model = load_model('../models/model2')
    print(predict_all(url, model))
