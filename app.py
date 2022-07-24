import streamlit as st

st.title('Greatest among 3 numbers')
a = st.number_input('Enter the first number')
b = st.number_input('Enter the second number')
c = st.number_input('Enter the third number')
result = a
if b>result:
    result=b

if c>result:
    result=c
    
st.write('Greatest among the given numbers is', result)
