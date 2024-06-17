class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

    def update_year(self, new_year):
        self.year = new_year
        print(f"The car's year has been updated to {self.year}")
car1 = Car("Toyota", "Camry", 2020)
car1.display_details()  
car1.update_year(2022)
car1.display_details()
car2 = Car("Honda", "Civic", 2018)
car2.display_details() 
