import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data.csv")

X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

model = LogisticRegression()
model.fit(X, y)

st.title("Customer Purchase Prediction")

age = st.number_input("Age")
salary = st.number_input("Salary")

if st.button("Predict"):
    result = model.predict([[age, salary]])
  
    if result[0]==1:
        st.success("Customer will Buy")
    else:
        st.error("Customer will Not Buy")
