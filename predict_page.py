import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('logisticS.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

logistic = data["model"]


def show_predict_page():
    st.title("Covid Death Prediction")
    st.write("""### We need some information to predict""")
    sex = ('Female', 'Male')
    hospitalization = ('Out pataiant', 'In pataiant')
    intubated = ('Yes', 'No')
    penumonia = ('Yes', 'No')
    prganacy = ('Yes', 'No')
    diabetes = ('Yes', 'No')
    copd = ('Yes', 'No')
    asthma = ('Yes', 'No')
    inmsupr = ('Yes', 'No')
    hypertension = ('Yes', 'No')
    other_disease = ('Yes', 'No')
    cardiovascular = ('Yes', 'No')
    obesity = ('Yes', 'No')
    renal_chronic = ('Yes', 'No')
    tobacco = ('Yes', 'No')
    covid_res = ('Yes', 'No', 'Waiting')
    icu = ('Yes', 'No')

    sex = st.selectbox("Sex", sex)
    age = st.slider("Age", 0, 100, 35)
    hospitalization = st.selectbox("Hospitalization", hospitalization)
    intubated = st.selectbox("Oxygen Requirment ", intubated)
    penumonia = st.selectbox("Are you suffering from Penumonia? ", penumonia)
    prganacy = st.selectbox("Are you pregnent? ", prganacy)
    diabetes = st.selectbox("Do you have diabeties? ", diabetes)
    copd = st.selectbox("Chronic obstructive pulmonary disease? ", copd)
    asthma = st.selectbox("Do you have asthma? ", asthma)
    inmsupr = st.selectbox("Do you have Immune system suppressed? ", inmsupr)
    hypertension = st.selectbox("you have hypertension?", hypertension)
    other_disease = st.selectbox("you have any other disease?", other_disease)
    cardiovascular = st.selectbox("you have heart disease?", cardiovascular)
    obesity = st.selectbox("Are you obese ? ", obesity)
    renal_chronic = st.selectbox("renal chronic disease?", renal_chronic)
    tobacco = st.selectbox("Do you take tobaccu? ", tobacco)
    covid_res = st.selectbox("your covid test results? ", covid_res)
    icu = st.selectbox("Is pataints is in ICU ", icu)

    ok = st.button("Results")
    if ok:
        X = [sex, hospitalization, intubated, penumonia, age,
                       prganacy, diabetes, copd, asthma, inmsupr, hypertension,
                       other_disease, cardiovascular, obesity, renal_chronic,
                       tobacco, covid_res, icu]
        st.write(X)
        for i in range(len(X)):
            if X[i] == 'Female':
                X[i] = 1
            elif X[i] == 'Waiting':
                X[i] = 2
            elif X[i] == 'Yes':
                X[i] = 1
            elif X[i] == 'In pataiant':
                X[i] = 1
            elif X[i] in range(0, 100):
                pass
            else:
                X[i] = 0
        st.write(X)
        X = np.array([X])
        X = X.astype(int)

        death = logistic.predict(X)
        if death[0] == 0:
            result = 'you will Survive stay Home stay safe '
        else:
            result = 'You need immidiate health care attention'
        st.subheader(result)
