#print(help(str))
from os import access

name = input("Enter Your Username: ")

if len(name)>= 12:
    raise ValueError("Username Cannot Be of More Than 12 Digits")
elif not name.find(" ")==-1:
    raise ValueError("Username Cannot Contain Spaces")
elif not name.isalpha():
    raise ValueError("Username Can Only Contain Alphabets")
else:
    print(f"Hello {name}")
#______________________________________________________________________________
#QUIZ

confi = (input("Wanna Play Quiz!? (y/n) : "))
if confi != "y":
    raise Exception("Invalid Input")

score = 0

que1 = float(input("Que 1: 3!=  "))
if que1 == 6:
    score += 4
else:
    score -= 1

que2 = int(input("Que 2: 2x11=  "))
if que2 == 22:
    score += 4
else:
    score -= 1

que3 = float(input("Que 3: 18/10=  "))
if que1 == 1.8 :
    score += 4
else:
    score -= 1

print(f"Your Final Score is {score}")
#______________________________________________________________________________
# indexing
#indexing = accessing elements of a sequence using [] (indexing operator)
#                [start:end:step]
# if no start then assumed position =0  Same with all positions
# minus denote selection of position from end

credit_no = "9876-2356-6434"
access = input("do want to get credit card (y/n) ")

if access != "y" and "n" :
    print("enter valid response (y/n)")
elif access == "n" :
    print(f"Well , Thanks For Playing {name}")
elif access == "y" :
    pass

print(" looks like you want it")
print("""credit no is in xxxx-xxxx-xxxx format and 
each section will shown depending upon no of que answered correctly""")
print("")

if score < 0:
    print("No credit card for you")
elif score ==2:
    print(f"you only get xxxx-xxxx-{credit_no[-4::]}")
elif score ==7:
    print(f"you only get xxxx-{credit_no[-9::]}")
elif score ==12:
    print(f"here you enjoy {credit_no}")

#_____________________________________________________________________________
# format specifiers = {:flags) format a value based on what

# :(number) = allocate that many spaces
# .(number)f = round to that many decimal places (fixed point)
# :03 allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, comma separator

 