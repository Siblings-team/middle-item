string=input("Enter your data or sentence of which's middle items are to be given, remember to have 1 whitespace between every item:- ")
length=len(string)
mylist=[]
x=0
y=0
for y in range(0,length):
    mylist.append(string[y])
    y+=1
    mylistlength=len(mylist)
howmany=int(input("How many middle no. of items do you want?"))
if length%2==0:
    def evenstring():
        if howmany%2==0:
            for x in range(0,mylistlength):
                mylist.pop(0)
                mylist.pop(-1)
                relength=len(mylist)
                if relength<=howmany:
                    break
        elif howmany%2!=0:
            yesorno=input("Number of items is even and the asked number of middle items is odd, do you want to continue?(yes/no)")
            if yesorno=="yes":
                rightorleft=input("Do you want your middle items to be calculated from right or left?(right/left")
                if rightorleft=="right":
                    print("haven't included this functionality yet")
                elif rightorleft=="left":
                    print("haven't included this functionality yet")
                else:
                    pass
            elif yesorno=="no":
                pass
            else:
                pass
        else:
            pass
        print(mylist)
elif length%2!=0:
    def oddstring():
        if howmany%2==0:
            yesorno=input("Number of items is odd and the asked number of middle items is even, do you want to continue?(yes/no)")
            if yesorno=="yes":
                rightorleft=input("Do you want your middle items to be calculated from right or left?(right/left")
                if rightorleft=="right":
                    print("haven't included this functionality yet")
                elif rightorleft=="left":
                    print("haven't included this functionality yet")
                else:
                    pass
            elif yesorno=="no":
                pass
            else:
                pass
        elif howmany%2!=0:
            for x in range(0,mylistlength):
                mylist.pop(0)
                mylist.pop(-1)
                relength=len(mylist)
                if relength<=howmany:
                    break
        else:
            pass
        print(mylist)
else:
    pass
