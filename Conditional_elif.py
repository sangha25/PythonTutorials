Grade=input("enter your Grade:")
if( int(Grade)>=90):
    print("your Score is A")
elif(int(Grade)>=80 and int(Grade)<90):
    print(" your score is B")
elif(int(Grade)>=70 and int(Grade)<80):
    print(" your score is C")
elif(int(Grade)>=60 and int(Grade)<70):
    print(" your score is D")
else:
    print("Sorry You Failed")
print("Finished")
