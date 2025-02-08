import re

pattern = r'\d+'  # Matches one or more digits
string = "abc123xyz"

match = re.search(pattern, string)
if match:
    print(f"Matched: {match.group()}")
else:
    print("No match")

#output
# Matched: 123