def calc(x,y) :
   return x+y,x*y
while True :
    n=int(input("enter choice: \n1.Calculate\n2.Exit\n"))
    if(n==1) :
        x=int(input("enter x:"))
        y=int(input("enter y:"))
        x,y=calc(x,y)
        print(x)
        print(y)
    elif(n==2):
        exit(1)
    else:
        print("invalid input")
