# Calculate Only two values using one operator 
num1 = float(input("Enter First Number : ")) # Call First value
op = input("Enter Operator : ") # Call operator
num2 = float(input("Enter Second Number : ")) # Call second Value

if op == '+': # For Add the two value
    print("Result : ",num1 + num2)
elif op == '-':# For Subtract the two value
    print("Result : ",num1 - num2)
elif op == '*': # For Multiple the two value
    print("Result : ",num1 * num2)
elif op == '/': # For Division the two value
    if num2 != 0:
        print("Result : ",num1 / num2) 
    else:
        print("Error : Division by Zero")
else: # User use to Invalid Operator
    print("Invalid Operator")


# print(float(eval(input("Enter the Value : ")))) # Shortcut method of calculate multiple value & operators in using python programming