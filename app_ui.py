import streamlit as st 
import pickle
model=pickle.load(open("model.pkl","rb"))
st.title("salary perdiction")
exp=st.number_input("Enter Experience",min_value=0, max_value=50, value=1)
if st.button("Predict"):
    result=model.predict([[exp]])
    st.write(f"predict salary: {int(result.flatten()[0])}")