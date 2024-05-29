import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('classifier.pkl','rb'))

def predict_note_authentication(variance,skewness,curtosis,entropy):
   
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Banknote Authentication Classifier")
    variance = st.text_input("variance", placeholder="Type Here")
    skewness = st.text_input("skewness", placeholder="Type Here")
    curtosis = st.text_input("curtosis", placeholder="Type Here")
    entropy = st.text_input("entropy", placeholder="Type Here")

    if st.button("Get Prediction"):
        output = predict_note_authentication(variance, skewness, curtosis, entropy)
        st.success(f'Result: {output}.')
        st.write('1 = banknote is genuine, 0 = banknote is forged')

if __name__=='__main__':
    main()
