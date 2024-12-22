class Car:
    def __init__(self, year, mileage, brand, model):
        self.year = year
        self.mileage = mileage
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - {self.mileage}km"