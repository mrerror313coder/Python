def cale(a, b,c):
   if c=='+' :
    print(a+b)
   elif c=='-' :
    print(a-b)
   elif c=='*' :
    print(a*b)
   elif c=='/' :
       print(a/b)
   else :
       print("Invaild Input")


first=int(input("Enter first number: "))
second=int(input("Enter second number: "))
operation=input("Enter operation: ")
cale(first, second, operation)

