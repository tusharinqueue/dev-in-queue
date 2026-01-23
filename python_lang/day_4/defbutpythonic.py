# def parity():
#     x = int(input("What is x: "))
#     if is_even(x):
#         print("x is even")
#     else:
#         print("x is odd")
#
# def is_even(x):
#     return x % 2 == 0
#
# parity()
#______________________________________________________________________________

def parity():
    x = int(input("what is x: "))
    print(f"x is {"even" if x%2 == 0 else "odd"}")

parity()