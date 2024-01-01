from databasecode import addcontact,viewcontact


flag=1
while flag>0:
    op=int(input("1.add contact\n2.view phonebook\n3.exit\n=>"))

    if op==1:
        cuname=input("enter the contact name:")
        ph=input("enter the phone number:")
        status=addcontact(cuname,ph)
        if status==1:
            print("added succesfully")
        else:
            print("failed")
    if op==2:
        ot=viewcontact()
        for i in ot:
            print(i)
        
    if op==3:
        flag=0