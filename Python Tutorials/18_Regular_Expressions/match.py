# Regular expressions (regex) are a powerful tool for matching patterns in text. In Python, the re module provides support for working with regular expressions.

import re

pattern = r'\d+'  # Matches one or more digits
string = "123abc"

match = re.match(pattern, string)
if match:
    print(f"Matched: {match.group()}")
else:
    print("No match")

#output
# Matched: 123