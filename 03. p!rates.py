# first task from me



# Second task from the lecture
cities = {}
command = input().split("||")
while command[0] != "Sail":
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities.keys():
        cities[city] = {"population": 0, "gold": 0}
    cities[city]["population"] += population
    cities[city]["gold"] += gold
    
    
    
    
    command = input().split("||")
    
    
command = input().split("=>")
while command[0] != "End":
    action = command[0]    
    if action == "Plunder":
        town, people, gold = command[1], int(command[2]), int(command[3])
    elif action == "Prosper":
        pass
    
    command = input().split("=>")





print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
print(f"{town} has been wiped off the map!")
print(f"Gold added cannot be a negative number!" and ignore the command.)
print(f"{gold added} gold added to the city treasury. {town} now has {total gold} gold.")
print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
print("Ahoy, Captain! All targets have been plundered and destroyed!")