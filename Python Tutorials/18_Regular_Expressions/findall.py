import re

pattern = r'\d+'  # Matches one or more digits
string = "abc123xyz456"

matches = re.findall(pattern, string)
print(f"Matches: {matches}")

#output
# Matches: ['123', '456']