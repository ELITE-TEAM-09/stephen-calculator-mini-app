
#This is a simple mini calculator with basic functionality

num1 = float(input("Type first number: "))
# Operators include *, +, -, //, /, and ** 
operator = input("Type operator: ") 
num2 = float(input("Type second number: "))

def mini_calculator(operator, num1, num2):
        if operator == "+":
            results = num1 + num2
            print (results)
        
        elif operator == "-":
            results = num1 - num2
            print (results)

        elif operator == "*":
            results = num1 * num2
            print (results)
        
        elif operator == "//":
            results = num1 // num2
            print (results)
            
        elif operator == "/":
            results = num1 / num2
            print (results)

        elif operator == "**":
            results = num1 ** num2
            print (results)
            
        else:
            print(f"ERROR: {operator} is not a valid operator.")


mini_calculator(operator, num1, num2)