print("Calculate fuel consumtion.")
Feed = input("Enter travel distance(kilometers): ")
Kilometers = int(Feed)
Feed = input("Enter fuel usage(liters): ")
Liters = int(Feed)
Consumption = Liters / Kilometers * 100
print("Fuel consumption is",Consumption,"l per 100 km")
