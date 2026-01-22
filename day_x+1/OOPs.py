#oops

class Car:
    def __init__(self, color , year , for_sale , condition , company):
        self.color=color
        self.year=year
        self.for_sale=for_sale
        self.condition=condition
        self.company=company

    def buy(self):
        print("Yes i want to buy that car")

    def sell(self):
        print("I wanna sell this car")


my_polo = Car("red" ,
              2009 ,
              False ,
              "fine" ,
              "VW")
my_polo.buy()
