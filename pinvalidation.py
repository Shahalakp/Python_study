p=input("enter the pin:")
for i in p:
    if not(i.isdigit()):
        print("not valid")
        break
else:
        if len(p)==4 or len(p)==6:
            for i in p:
                if int(i)%2==0:
                    print("not valid")
                    break
            else:
                print("valid")
        else:
            print("not valid")
    




