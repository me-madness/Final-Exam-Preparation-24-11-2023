# First task from me



# Second task from yhe lecture

import re

information = input()
pattern = r"(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"
matches = re.findall(pattern, information)
total_calories = [sum([int(match[5]) for match in matches])]
days = total_calories // 2000
print(f"You have food to last you for: {days} days")
