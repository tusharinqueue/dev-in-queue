print("Compound Interest Calculator")
print()

money =0

while money <=0:
    money = float(input("Enter The Money: "))
    if money <=0:
        print ("Money Can't be Negative or Zero")
rate=0

while rate<=0:
    rate = float(input("Enter The Rate: "))
    if rate <=0:
        print ("Rate Can't be Negative or Zero")
time=0

while time<=0:
    time = float(input("Enter The Time in Years: "))
    if time <=0:
        print ("Time Can't be Negative or Zero")

cinterest = money * pow((1 + rate/100),time)

print(f"Interest is {round(cinterest,2)}")
