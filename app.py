import streamlit as st
import pickle
import nltk
import string 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


stemmer = PorterStemmer()
nltk.download('punkt')
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('spam_model.pkl', 'rb'))
                    

def preprocess_text(message):
    message = message.lower()
    new_message = ''.join([char for char in message if char not in string.punctuation])
    tokens = word_tokenize(new_message)
    new_tokens = [word for word in tokens if word not in stopwords]
    stemmed_tokens = [stemmer.stem(word) for word in new_tokens]
    final_message = ' '.join(stemmed_tokens)
    return final_message



st.title('Spam or Ham classifier')
input = st.text_area("Enter a message :")

if st.button('Predict'):
    if input:
        processed_input = preprocess_text(input)
        transformed_input = vectorizer.transform([processed_input])
        prediction = model.predict(transformed_input)
        if prediction[0] == 0:
            st.write("The message is ham")
        else:
            st.write("The message is spam")

