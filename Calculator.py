def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

num1=float(input("Enter first number"))
num2=float(input("Enter second number"))

print("Choose Operation")
print("1.Additon")
print("2.ubtraction")
print("3.Multiplication")
print("4.Division")

choice=input("Enter choice(1/2/3/4):")
if choice=='1':
    result=add(num1,num2)
elif choice=='2':
    result=subtract(num1,num2)
elif choice=='3':
    result=multiply(num1,num2)
elif choice=='4':
    result=divide(num1,num2)
else:
    result='Invalid input' 
print("Result:",result)
   