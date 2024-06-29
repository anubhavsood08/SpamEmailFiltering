import streamlit as st
import pickle 
import string 
import nltk 
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
# string.punctuation
from nltk.corpus import stopwords
# stopwords.words('english')
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
# ps.stem('loving')
def transform_text(text):
    text=text.lower()
    text = nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]  #u cant copy lis like this text=y list is a mutable data type  
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()
    for i in text :
        z=ps.stem(i)
        y.append(z) #or y.append(stem(i))

    return "  ".join(y) #or y

tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms=st.text_area("Enter the message")
if st.button('Predict'):
# 1. preprocess
 transform_sms=transform_text(input_sms)
# 2. vectorize
 vector_input =tfidf.transform([transform_sms])
# 3. predict
 result=model.predict(vector_input)[0]
# 4. display
 if result==1:
    st.header("Spam")
 else :
    st.header("Not spam")

