# here + = plus || - = minus || * = multiply || / = divide



age1 = 4
age2 = 8

age1 += age2
#or we could have written as age1 = age1 + age2 (but it is inefficient)

print(age1)
print()
print()


# + can be replaced by - / * too
#______________________________________________________________________________

# ** = power mei || % = gives remainder
age3 = 11
age4 = 2

age3 **= 2
age3 %= age4

print("ER")
print(age3)
print(age4)
print()
print()



#_____________________________________________________________________________
# round() = rounds number || abs = more like mode like absolute value
#pow = to the power of written as (x,y) type
#max = gives maximum value || min = gives min value

x = 4.45
y = 3
z = 5
zz = -18

rounder = round(x)  # this round funcn can be written as round(x,y) here
                      # x is the no and y is no of decimal places it has to be rounded to
absol = abs(zz)
powerii = pow(y ,z)
maxi = max(x,y,z,zz)
minii = min(x,y,z,zz)

print ("RAPMM")
print(rounder)
print(absol)
print(powerii)
print(maxi)
print(minii)
print()
print()



#________________________________________________________________________________
# importing math functions

import math      #it will add maths funcn if written before codes
print("importing math")
print(math.pi) #it imports value of pi
print(math.e)  #it gives value of e
print(math.sqrt(9)) #gives squareroot of no
print(math.ceil(7.2)) # GIF hai ye
print(math.floor(7.8)) #LIF hai ye
#aur bhi h kafi need to explore as we need them
print()
print()


#_________________________________________________________________________________
# calculating circumference and area of circle
import math
print("Circle Area and Circumference Calculator")
radius = float(input("Enter Radius Of Circle:"))

circum =  2*math.pi*radius
area = math.pi * radius**2 #or i can use pow(radius,2)

print(f"The Area Of Circle Is : {round(area,2)}")
print(f"And Circumference Is : {round(circum,2)}")
print()
print()

#________________________________________________________________________________
#finding Hypotnuese of triangle

import math
print("Pythagoras Calculator")
Perpen = float(input("Enter the Perpendicular of Triangle "))
basee = float(input("Enter the Base of Triangle "))

Hypo =  math.sqrt( Perpen**2 + basee**2)

print(f"The Hypotnuese of Triange is : {round(Hypo,2)}")


