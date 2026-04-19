import streamlit as st
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Customer Purchase Prediction")
st.write("Predict whether a customer will purchase based on age and salary.")
age = st.number_input("Age")
salary = st.number_input("Salary")

if st.button("Predict"):
    if age<=0 or salary <=0:
        st.error("Please Enter valid positive values.")
    elif age>100:
        st.error("Age seems unrealistic")
    
    else:
        input_data = scaler.transform([[age, salary]])
        result = model.predict(input_data)
        prob=model.predict_proba(input_data)
        st.subheader("Result:")
    
        if result[0] == 1:
            st.success("Customer WILL purchase 🎉")
        else:
            st.warning("Customer will NOT purchase ❌")
        st.subheader("Probability:")
        st.write("No Purchase(0)",round(prob[0][0]*100,2),"%")
        st.write("Purchase(1)",round(prob[0][1]*100,2),"%")
