import streamlit as st

#Heading

st.write("""# Multiplication of two numbers
This app calculates the product of 2 given numbers""")

#Get Input

st.header('Enter the numbers')

number_1 = st.number_input("Number 1")
number_2 = st.number_input("Number 2")

#Processing

product = number_1 * number_2

#Output

st.header('Output')

st.write('The product of ',number_1,' and ',number_2,' is ',product)
