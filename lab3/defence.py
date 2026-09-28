class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def show_info(self):
        print(f"Brand is {self.brand}")
        if(self.year > 2020):
            print(f"Modern car")
        else : print(f"Old car")
p1 = Car("mercedes" , 2019)


p1.show_info()
