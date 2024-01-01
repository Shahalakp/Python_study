#Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

def newlist(li,pos1,pos2):
    size=len(li)

    # new=li[pos1-1]
    # li[pos1-1]=li[pos2-1]
    # li[pos2-1]=new
    # return li

    li[pos1],li[pos2]=li[pos2],li[pos1]
    return li


li=[1,"animal",2,"hi",87,"nice","shit"]
print(li)
pos1=int(input("enter the position1 to swap:"))
pos2=int(input("enter the position2 to swap:"))

print(newlist(li,pos1,pos2))
