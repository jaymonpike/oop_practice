from vehicle import Vehicle

if __name__ == "__main__":

    #Create an instance of the Vehicle class
    black_car = Vehicle("Tesla", "Model 3", 2018)
    red_car = Vehicle("Toyota", "Camry", 2023)

    all_vehicles = Vehicle.get_all_vehicles()
    for vehicle in all_vehicles:
        print(vehicle)