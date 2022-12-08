from scam_spotter_web.scrape import scrape_photo_text, scrape_text
from scam_spotter_web.text_processing import preprocess_pad


def predict_dual(model, url):

    # Scrape image and text with selenium
    X_image, X_text = scrape_photo_text(url)

    # Process text from string to embedded array
    X_text = preprocess_pad([X_text])

    prediction = model.predict([X_image, X_text])

    return prediction

def predict_nlp(model, url):

    # Scrape text with selenium
    X_text = scrape_text(url)

    # Process text for model ingestion
    X_text_padded = preprocess_pad([X_text])

    # Do prediction with model
    prediction = model.predict(X_text_padded)

    return prediction


# if __name__ == '__main__':
#     url = 'https://www.barclays.co.uk/'
#     model = load_model('../models/model2')
#     print(predict_dual(url, model))
