def menu():
    print("Menu:\n\t1)add\n\t2)sub\n\t3)mul\n\t4)div\n\t5)mod\n\t6)exit")
    global x
    x=int(input("Enter selection\t:\t"))
    
def in_put():
    global a,b
    a=int(input("num1\t:\t"))
    b=int(input("num2\t:\t"))
    
def add():
    in_put()
    print("Add =",a+b)
    print("\n")
    menu()
def sub():
    in_put()
    print("Sub =",a-b)
    print("\n")
    menu()
def mul():
    in_put()
    print("Mul =",a*b)
    print("\n")
    menu()
def div():
    in_put()
    print("Div =",a/b)
    print("\n")
    menu()
def mod():
    in_put()
    print("Mod =",a%b)
    print("\n")
    menu() 
def exit():
    print("Thank You...!!!")

menu()
i=0
while(i<1):
    if(x==1):
        add()
    elif(x==2):
        sub()
    elif(x==3):
        mul()
    elif(x==4):
        div()
    elif(x==5):
        mod()
    elif(x==6):
        exit()
        break      

    
