# Importing important libraries

import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Backend

# Declaring Stemmer Variable

ps = PorterStemmer()

# Creating Data Processing Function

def preprocess_text(text):
    # Converting into lower-case
    lower_converted = text.lower()

    # Getting a list of words
    list_of_words = nltk.word_tokenize(lower_converted)

    # Getting onlyn alphanumeric text
    only_alpha_numeric_words = []
    for i in list_of_words:
        if i.isalnum():
            only_alpha_numeric_words.append(i)

    # Removing Stopwords and puctuation marks
    cleaned_text = []
    for i in only_alpha_numeric_words:
        if i not in stopwords.words('english') and i not in string.punctuation:
            cleaned_text.append(i)

    # Applying stemming
    final_text = []
    for i in cleaned_text:
        final_text.append(ps.stem(i))

    # Returning final text
    return " ".join(final_text)


# Loading srtored TFIDF Vector and model using pickle library

tfidf = pickle.load(open('vectorizer1.pkl','rb'))
model = pickle.load(open('model1.pkl','rb'))

# Frontend

st.title('Email/SMS Spam Classifier')

# Taking Input

input_sms = st.text_area("Enter the message below: -")

# Creating a "Predict" button 

if st.button("Predict"):

    # Preprocessing Input
    preprocessed_text = preprocess_text(input_sms)

    # Vectorizing the text
    vector_input = tfidf.transform([preprocessed_text])

    # Predict
    result = model.predict(vector_input)[0]

    # Display the final result
    if result == 1:
        st.header('Spam')
    else:
        st.header("Not Spam")
