cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven


print(f"There are {cars} cars available.")
print(f"There are only {drivers} drivers available.")
print(f"Ther will be {cars_not_driven} empty cars today")
print(f"We can transport {carpool_capacity} people today.")
print(f"we have {passengers} to carpool today.")
print(f"We heed to put about {average_passengers_per_car} in each car")
print("That will be all Glenn will do in this chapter today")
#this will be all for now
#delete the comments afterwards