"""
String Operations To Perform :
    While | Exception Handling | String Operations 

"""

class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass

a = "RST Forum = Networking + Linux + Python + Cyber_Security + Advance_Penetration_Testing"

print("All Possible String -78")
print("Menu:\n\t1.Print\n\t2.Datatpye\n\t3.Lenght\n\t4.Update_Print_Updated_String\n\t5.Repetation\n\t6.Return_Character_AtIndex_Number\n\t7.Range_Slice([start:end])\n\t8.Membership(in)\n\t9.Membership(not in)\n\t10.Exit\n")

while(True):
    
    try:
        n=int(input("\nEnter a number to perform operation : "))
        if(n>10):
            raise ValueTooLargeError
        elif(n<=0):
            raise ValueTooSmallError
        elif(n==10):
            print("Thank You....!!")
            break
        elif(n==1):
            print(a)
        elif(n==2):
            print("Datatype of String a = ",type(a))
        elif(n==3):
            print("Lenght of String a = ",len(a))
        elif(n==4):
            print("Update String a = ",(a))
            u_s = input("Enter the String : ")
            print("Updated String = ", u_s)
        elif(n==5):
            k="Hello World..!!\t"
            i = int(input("Enter The Number Of Time You Want To Repeat The Above String = "))   
            print("String Repeated "+ str(i) + " Times  = ",k*i)
        elif(n==6):
            print(a)
            i = int(input("Enter The Index Number (<=86) Of Above String To Get The Respective Element = "))   
            print("Element at Index Number {} = ".format(i) ,a[i] )
        elif(n==7):
            print(a)
            i = int(input("Enter The Starting Point (<=85) = "))
            j = int(input("Enter The Ending Point  (<=85) = "))
            print("Slicing from {} to {}   :--->    ".format(i,j) ,a[i:j] )
        elif(n==8):
            print(a)
            i = input("Enter A String To Check Weather It *Is A* Member Of Above String Or Not = ")
            if i in a:
                print("True")
            else:
                print("False")
        elif(n==9):
            print(a)
            i = input("Enter A String To Check Weather It Is *NOT* A Member Of Above String Or Not = ")
            if i not in a:
                print("True")
            else:
                print("False")
                    
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print("")
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print("")
    except ValueError as e:
        print("Enter Valid Number ")
    finally:
        print("Got It...!!!")

