print("Welcome to the Garden Watering Scheduler!")
total_liters = int(input("How many liters of water are needed for the garden? "))
extra_water = int(input("What percentage of water would you like to add for evaporation? (e.g., 5, 10, 15) "))
zones = int(input("How many zones will the water be distributed across? "))

# Calculate water needed per zone
total_with_extra = total_liters * (1 + extra_water / 100)
water_per_zone = round(total_with_extra / zones, 2)

print(f"Each zone will receive approximately {water_per_zone} liters of water.")
