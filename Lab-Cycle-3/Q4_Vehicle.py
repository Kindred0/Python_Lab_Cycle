class vehicle :
    def __init__(self) :
        self.engine_number = int(input("Engine Number\t\t: "))
        self.model = input("Model\t\t\t: ")
        self.type = input("Type\t\t\t: ")
        self.mileage = float(input("Mileage\t\t\t: "))
        self.vendor = input("Vendor\t\t\t: ")
        self.registration_number = int(input("Registration Number\t: "))
        self.owner = input("Owner\t\t\t: ")
    def display(self) :
        print("\nEngine Number\t\t: ",self.engine_number)
        print("Model\t\t\t: ",self.model)
        print("Type\t\t\t: ",self.type)
        print("Mileage\t\t\t: ",self.mileage)
        print("Vendor\t\t\t: ",self.vendor)
        print("Registration Number\t: ",self.registration_number)
        print("Owner\t\t\t: ",self.owner)

A = vehicle()
A.display()
