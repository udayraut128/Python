import re

pattern = r'\d+'  # Matches one or more digits
string = "abc123xyz456"

matches = re.finditer(pattern, string)
for match in matches:
    print(f"Matched: {match.group()}")


#output
# Matched: 123
# Matched: 456