import datetime
DOB=input("Enter your DOB:")
CurrentYear=datetime.datetime.now().year
Age=CurrentYear-int(DOB)
if(Age>=18):
    print("Your age is {} and You are Ready To vote".format(Age))
if(Age<18):
    print("Your age is {} and you arent allowed Here.".format(Age))
#this code will run even if the condition Failed.
print("Vote for Your Future.")