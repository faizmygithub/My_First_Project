num1=int(raw_input("Enter the First Number "))
num2=int(raw_input("Enter the Second Number "))
choice = int(raw_input("Enter choice 1. ADD, Enter choice 2. Subtract, Enter choice 3. Multiply,Enter choice 4.Divide "))

if choice==1:
    print (num1, "+",  num2,  "= ", num1+num2)
elif choice==2:
    print (num1, "-" , num2,"= ", num1-num2)
elif choice==3:
    print (num1, "*" , num2, "= " ,num1*num2)
elif choice==4:
    print (num1,"/" , num2 , "= " ,num1/num2)
else:
    print("Invalid Input")




