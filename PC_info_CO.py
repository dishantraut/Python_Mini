"""
Class | Object | Try..Catch...Finally.. | raise | custom(user made) Exceptions | pass | inheritance 

"""

# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error ):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass


class comp():
    def __init__(self,brnd,config,ram,price):
        global s,b,c,r,p,m_n
        b=brnd 
        c=config
        r=ram
        p=price
    def info_dishant(this,m_n):
        print("Brand Name = {} " .format(b))
        print("Model Name = {} " .format(m_n))
        print("Configuration = {} " .format(c))
        print("RAM = {} " .format(r))
        print("MRP = Rs. {} " .format(p))



print("Hi... Class Computer here")
while(True):
    try:
        print("Menu:\n\t1.Lenovo\n\t2.Asus\n\t3.Dell\n\t4.Acer\n\t5.AlienWare")
        n=int(input("Enter the number to get the Model Details  :  "))
        print("\n\n")
        if(n<0):
            raise ValueTooSmallError
        elif(n>5):
            raise ValueTooLargeError
        elif(n==1):
            x=comp("Lenovo","i5 8thGen","8 GB",690000)
            x.info_dishant("LEGION..")
            break
        elif(n==2):
            x=comp("Asus","RYZEN","8 GB",50000)
            x.info_dishant("Turf..")
            break
        elif(n==3):
            x=comp("Dell"," i5 8th gen","8 GB | 2 TB HDD",53549.00)
            x.info_dishant("Inspiron 5570 ..")
            break
        elif(n==4):
            x=comp("Acer","Intel Core i5-8265U processor","8GB/1TB ",37490)
            x.info_dishant("Acer Aspire 3..")
            break
        elif(n==5):
            x=comp("AlienWare","8th Generation Intel Core i7-8750H 6-Core","1TB HDD, + 8 GB SSD",169563.00 )
            x.info_dishant(" AW17R5-7405SLV-PUS..")
            break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()
    except ValueError as e:
        print("Enter Valid Number ")
    """finally:
        print("\nThank You....Visit Again..!!!")"""
