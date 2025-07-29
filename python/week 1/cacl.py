def  get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter  a  valid  number")

 

num1 =get_number("Enter the  first number:")
num2 =get_number("Enter the  second  number:")

sum_result = num1+num2
difference_result = num1-num2
product_result =num1-num2

print(f"the sum of {num1} and {num2} is:{sum_result}")
print(f"the difference of {num1} and {num2} is:{difference_result}")
print(f"the product of {num1} and {num2} is:{product_result}")
