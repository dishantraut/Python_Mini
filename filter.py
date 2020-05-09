
age=[]
n=int(input("Enter the number of members in your family :\t"))
for i in range(n):
    p=int(input("Enter the ages:\t"))
    age.append(p)
print("The ages of your family members is  :")
print(age)

def chk(a):
    if(a<18):
        return False
    else:
        return True
a=filter(chk,age)
print()
print("The ages valid for voting are :")
print(list(a))


