# -----------------------List of Operations(func)-----------------------

# Function to add two numbers
def add(num_1: float, num_2: float):
    return num_1 + num_2

# Function to multiply two numbers
def multiply(num_1: float, num_2: float):
    return num_1 * num_2

# Function to divide two numbers
def divide(num_1: float, num_2: float):
    return num_1 / num_2

# Function to subtract two numbers
def sub(num_1: float, num_2: float):
    return num_1 - num_2

# List of arithmetic functions for easy access based on index
LIST_ARITH = [add, sub, multiply, divide]

# ----------------------Function to Get Operators-----------------------

# Function to get the correct arithmetic operation based on a string input
def get_operator(operation: str):
    # Check the operation string and return the corresponding function from LIST_ARITH
    if operation == "add":
        return LIST_ARITH[0]
    if operation == "sub":
        return LIST_ARITH[1]
    if operation == "multiply":
        return LIST_ARITH[2]
    if operation == "divide":
        return LIST_ARITH[3]

# ---------------------------END---------------------
