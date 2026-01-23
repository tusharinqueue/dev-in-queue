# if || else || or else+if + elif(can write as many of these)||
#example 1

age = int(input("Please Enter Your Age : "))
if age >= 100:
    print("You Are Gonna Die Enjoy Your Remaining Life")
elif age >= 18:
    print("You are now eligible to create bank account")
elif age <= 0:
    print("WOW! You Haven't Been Born Yet")
else:
    print("You are Under 18 Year Of Age So You Can't Create an Account ")

print()
#_____________________________________________________________________________
#example2 Binary Statement

rr = input("Would You Like to Eat Pizza (y/n) ")     #here if we user single = it will consider rr as we are giving it
                                                     # variable value y | so to have comparison we use ==
if rr == "y":
    print("1 Amazing Pizza Comming in a While")
else:
    print("Anything Else You Would Like To Eat")

print()

#-----------------------------------------------------------------------------
#example 3 Empty Statemant

Name = input("Please Enter Your Name: ")

if Name == "":
    print("You Did Not Write Your Name")
else:
    print(f"Hello {Name}")

print()
#_______________________________________________________________________________
#example 3 Boolean

online = True        #we can change it to change result
if online:
    print("you are online")
else:
    print("you are offline")

#___________________________________________________________________________
temp = 20
is_sunny = True
if temp >= 28 and is_sunny:
    print("It is HOT outside ")
    print("It is SUNNY *")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
# here (and) means both condition must be true
#we can use (or) if we want ,only one of the (atleast 1) condition to be true
#using (not) inverts the condn (notTrue,notFalse)


#________________________________________________________________________________________-
#conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of two values based on a condition
# X if condition else Y

num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"
#print("Positive" if num > 0 else "Negative")
#result = "EVEN" if num % 2 == 0 else "ODD"
#max_numa if a else b
#min_num = a if a < b else b
#status = "Adult" if age >= 18 else "Child"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
#weather = "HOT" if temperature > 20 else "COLD"