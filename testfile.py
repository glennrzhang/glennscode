available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
for i in ["stamina grains","health potion","bread"]:
    health_points += available_items.pop(i,0)
print(health_points)
print(available_items)
