import nltk
import joblib
from nltk.corpus import stopwords
import streamlit as st

cv = joblib.load('cv_joblib')
clf = joblib.load('clf_joblib')

def predict(raw_text):
	vectors = cv.transform(raw_text)
	return clf.predict(vectors)

def main():
	st.title("Spam Detector")
	raw_text = st.text_input("Enter the message","Type Here..")
	submit = st.button("Check spam")
	if submit:
		result = predict([raw_text])
		st.success(result)
	    

       
if __name__ == '__main__':
    main()