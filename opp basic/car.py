class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print(f"you drive the {self.model}")
        
    def stop(self):
        print(f"you stop the {self.model}")
        
    def discribe(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"For Sale: {self.for_sale}")
        
        