def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print(" Select Operation\n1.Add\n2.Substract\n3.Multiply\n4.Divide")

while True:
    choice = input(" Enter choice (1/2/3/4):")
    if choice in ('1','2','3','4'):
        num1 = float(input(" Enter a Number: "))
        num2 = float(input(" Enter another Number: "))
        
        if choice =='1':
            print(num1, "+", num2,"=",add(num1,num2))
        elif choice =='2':
            print(num1, "-", num2,"=",substract(num1,num2))
        elif choice =='3':
            print(num1, "*", num2,"=",multiply(num1,num2))     
        elif choice =='4':
            print(num1, "/", num2,"=",divide(num1,num2))
    else:
        print("Invalid input\nExiting!!!")
        break
          
        next_calculation = input(" Want to do Another Calculation(Yes/No): ")
        if calculation =="no":
            break
               