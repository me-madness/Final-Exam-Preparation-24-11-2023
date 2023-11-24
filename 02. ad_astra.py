# First task from me



# Second task from yhe lecture

import re

text = input()
pattern = r"(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})"
match = re.findall(pattern, text)

