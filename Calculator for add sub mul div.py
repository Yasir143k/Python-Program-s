num_1 = int(input("Enter the first number : "))
num_2 = int(input("Enter the second number : "))
def add(n1,n2):
    return n1+n2
result = add(num_1,num_2)
print(f"The addiotion of {num_1} and {num_2} is {result}")
def sub(n1,n2):
    return n1-n2
result_2 = sub(num_1,num_2)
print(f"The Subtraction of {num_1} and {num_2} is {result_2}")
def mul(n1,n2):
    return n1*n2
result_3 = mul(num_1,num_2)
print(f"The Multiplication of {num_1} and {num_2} is {result_3}")
def div(n1,n2):
    return n1/n2
result_4 = div(num_1,num_2)
print(f"The Division of {num_1} and {num_2} is {result_4}")
def remin(n1,n2):
    return n1%n2
result_5 = remin(num_1,num_2)
print(f"The Reminder of {num_1} and {num_2} is {result_5}")