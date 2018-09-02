import datetime  #This Library will import computer Timer.
DOB=input("Enter your Date of Birth:")
#date of current system.
CurrentYear=datetime.datetime.now().year
Age=CurrentYear-int(DOB)
print("Your age is {}".format(Age))