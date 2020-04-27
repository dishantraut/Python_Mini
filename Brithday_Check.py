"""   BirthDay App    """

dic = {}
while(True):
    print("*******Birthday App*******")
    print("1.Show Birthday\n2.Add To Birthday List\n3.Exit")
    choice = int(input("Enter Choice\t:\t"))

    if(choice == 1):
        if(len(dic.keys())==0):
            print("Nothing To Show")
            print("--------------------------------")
        else:
            name=input("Enter The Name\t:\t")
            BD=dic.get(name,"No Data Found")
            print(BD)
            print("--------------------------------")
    elif(choice == 2):
        name=input("Enter The Name\t:\t")
        bdate=input("Enter BirthDate\t:\t")
        dic[name] = bdate
        print("Birthday Added")
        print("--------------------------------")
    elif(choice == 3):
        break
    else:
        print("Choose a valid option...!!!")
