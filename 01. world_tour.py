# First task from me



# Second task from the lecture

stops = input()
command = input().split(":")

while command[0] != "Travel":
    if command[0] == "Add Stop":
        index, some_string = int(command[2], command[2])
        if index in range(len(stops)):
            stops = stops[:index] + some_string + stops[index:]
    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[2], command[2])
        if start_index in range(len(stops)) and end_index in range(len(stops) -1):
            stops = stops[:start_index] + stops[end_index +1:]
    elif command[0] == "Switch":
         old_string, new_string= int(command[2], command[2])
         if old_string in stops:
             stops = stops.replace(old_string, new_string)
         
    print(stops)     
    command = input().split(":")     


print(f"Ready for world tour! Planned stops: {string}")