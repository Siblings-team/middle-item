# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:51:34 2020

@author: rsh110520
"""

string=input("Enter your data or sentence of which's middle items are to be given, remember to have 1 whitespace between every item:- ")
length=len(string)
mylist=[]
x=0
y=0
counter=0
for y in range(0,length):
    mylist.append(string[y])
    y+=1

    mylistlength=len(mylist)
    

howmany=int(input("How many middle no. of items do you want?"))
if length%2==0:
    def evenstring():
        global counter
        if howmany%2==0:
            for x in range(0,mylistlength-howmany):
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
                    while counter <(((mylistlength-howmany)//2)+1):
                        mylist.pop(-1)
                        counter +=1
                    counter=0
                    while counter <(((mylistlength-howmany)//2)):
                        mylist.pop(0)
                        counter +=1

                    
                elif rightorleft=="left":
                     while counter <(((mylistlength-howmany)//2)+1):
                        mylist.pop(0)
                        counter +=1
                     counter=0
                     while counter <(((mylistlength-howmany)//2)):
                        mylist.pop(-1)
                        counter +=1

                else:
                    print("Wrong input! You have to choose between right our left!")
            elif yesorno=="no":
                print("Thank you so much for using this program !")
            else:
                print("wrong input!you have to choose between (yes or no )!")

    evenstring()
    print(mylist)
elif length%2!=0:
    def oddstring():
        global counter
        if howmany%2==0:
            yesorno=input("Number of items is odd and the asked number of middle items is even, do you want to continue?(yes/no)")
            if yesorno=="yes":
                rightorleft=input("Do you want your middle items to be calculated from right or left?(right/left")
                if rightorleft=="right":
                     while counter <(((mylistlength-howmany)//2)+1):
                        mylist.pop(-1)
                        counter +=1
                     counter=0
                     while counter <(((mylistlength-howmany)//2)):
                        mylist.pop(0)
                        counter +=1
                elif rightorleft=="left":
                     while counter <(((mylistlength-howmany)//2)+1):
                        mylist.pop(0)
                        counter +=1
                     counter=0
                     while counter <(((mylistlength-howmany)//2)):
                        mylist.pop(-1)
                        counter +=1
                else:
                    print("Wrong input! You have to choose between right our left!")
            elif yesorno=="no":
                print("Thank you so much for using this program !")            
                pass
        elif howmany%2!=0:
            for x in range(0,mylistlength):
                mylist.pop(0)
                mylist.pop(-1)
                relength=len(mylist)
                if relength<=howmany:
                    break
        
    oddstring()    
    print(mylist)
