class Car:
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year

    def display(self):
        print(f"Name: {self.name}\nModel: {self.model}\nYear: {self.year}")
        

    def change_model(self,new_model):
        self.model = new_model

    


if __name__ == "__main__":
    car = Car("Bmw","X5",2021)
    car.display()
    car.change_model("X6")
    car.display()