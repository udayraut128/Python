# Creating a dictionary to store student names and their corresponding scores
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Emma": 88
}

# Accessing values
print("Bob's score:", student_scores["Bob"])

# Modifying values
student_scores["Charlie"] = 80
print("Charlie's updated score:", student_scores["Charlie"])

# Adding new key-value pairs
student_scores["Frank"] = 87
print("Frank's score:", student_scores["Frank"])

# Deleting key-value pairs
del student_scores["David"]
print("Dictionary after deleting David:", student_scores)

# Iterating over keys and values
print("Student names and scores:")
for name, score in student_scores.items():
    print(name, "->", score)

# Checking if a key exists
if "Alice" in student_scores:
    print("Yes, Alice's score is present in the dictionary.")
else:
    print("No, Alice's score is not present in the dictionary.")


#output
# Bob's score: 92
# Charlie's updated score: 80
# Frank's score: 87
# Dictionary after deleting David: {'Alice': 85, 'Bob': 92, 'Charlie': 80, 'Emma': 88, 'Frank': 87} 
# Student names and scores:
# Alice -> 85
# Bob -> 92
# Charlie -> 80
# Emma -> 88
# Frank -> 87