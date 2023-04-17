import streamlit as st

def find_largest(a, b, c):
    """
    Function to find the largest number among the 3 given numbers.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Streamlit app starts here
st.title("Find the largest among the 3 given numbers")

# Take user input for the 3 numbers
num1 = st.number_input("Enter the first number", value=0, step=1)
num2 = st.number_input("Enter the second number", value=0, step=1)
num3 = st.number_input("Enter the third number", value=0, step=1)

# Find the largest number
largest_num = find_largest(num1, num2, num3)

# Display the largest number
st.write(f"The largest number among {num1}, {num2}, and {num3} is {largest_num}.")
