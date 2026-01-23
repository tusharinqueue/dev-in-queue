print("Calculator")
print()
print("Limited to Only 2 Numbers And 4 Operations")
print("+,-,*(x),/")
print()
n1 = float(input("Enter 1st Number : "))
n2 = float(input("Enter 2nd Number : "))
oopr = input("Give Operation (+,-,*,/) ")

if oopr == "+":
    nf= (n1 + n2)
    print(round(nf, 2))
elif oopr == "-":
    nf= (n1 - n2)
    print(round(nf, 2))
elif oopr == "*":
    nf= (n1 * n2)
    print(round(nf, 2))
elif oopr == "/":
    nf= (n1 / n2)
    print(round(nf, 2))
else:
    print(f"The Operation '{oopr}' is Invalid ")


