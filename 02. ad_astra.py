# First task from me



# Second task from the lecture
# 0.2

import re

information = input()
pattern = r"(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"
# index 1 - item name, index 3 - expiration date, index 5 - calories 
matches = re.findall(pattern, information)
total_calories = [sum([int(match[5]) for match in matches])]
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for element in matches:
    item_name = element[1]
    expiration_date = element[3]
    calories = element[5]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")

# Second option from the lecture
# 02.1

import re

information = input()
pattern = r"(?i)(?P<item_name>[#|])([a-z\s]+)(\1)(?P<expiration_date>\d{2}\/\d{2}\/\d{2})(\1)(?P<calories>\d+)(\1)"
# index 1 - item name, index 3 - expiration date, index 5 - calories 
matches = re.findall(pattern, information)
total_calories = [sum([int(match[5]) for match in matches])]
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for match in matches:
    match_dict = dict(zip["symbol", "item_name", "symbol", "expiration_date", "symbol", "calories"], match)
    print(f"Item: {match_dict['item_name']}, Best before: {match_dict['expiration_date']}, Nutrition: {match_dict['calories']}")