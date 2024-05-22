import re

pattern = r'\d+'  # Matches one or more digits
string = "abc123xyz456"

result = re.sub(pattern, '#', string)
print(f"Result: {result}")

#output
# Result: abc#xyz#
