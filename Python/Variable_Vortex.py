#Riddle
#You have three containers: 1 holding 12 liters of water, another holding 7 liters of water, and a 3rd one thats empty but can hold up to 15 liters. Transfer the water so that each container ends up with an equal amount

container_1 = 12
container_2 = 7
container_3 = 0

#Equal distribution formula
total_water = container_1 + container_2 + container_3
equal_amount = total_water / 3

#Adjusting the containers
container_1 = equal_amount
container_2 = equal_amount
container_3 = equal_amount

#output
print(f"Container 1: {container_1} liters")
print(f"Container 2: {container_2} liters")
print(f"Container 3: {container_3} liters")