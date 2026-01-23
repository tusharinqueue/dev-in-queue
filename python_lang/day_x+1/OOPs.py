#oops

class Car:
    #class variable -- defined outside constructor
    #share data across all objects || shared among all instances of a class
    current_year=2026
    no_of_cars=0
    def __init__(self, color , year , for_sale , condition , company):
        self.color=color
        self.year=year
        self.for_sale=for_sale
        self.condition=condition
        self.company=company
        Car.no_of_cars+=1 #class variable will update when a object if created

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
