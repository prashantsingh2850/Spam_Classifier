import streamlit as st
import pickle
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


def transform_text(text):
    text = text.lower()

    text = nltk.word_tokenize(text)

    ps = PorterStemmer()

    y = []

    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Email/sms Classifier')
input_sms = st.text_area('Enter the message')

if st.button('Predict'):
    #1. Preprocess
    transformed_sms = transform_text(input_sms)
    #2. Vectorize
    vector_input = tfidf.transform([transformed_sms])
    #3. Predict
    result = model.predict(vector_input)
    #4. Display
    if result == 1:
        st.header("spam")
    else:
        st.header("Not Spam")
