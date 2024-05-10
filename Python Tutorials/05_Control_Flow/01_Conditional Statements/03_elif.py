# 1 example

# Define a variable
score = 75

# Check the score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print the grade
print("Your grade is:", grade)

# Output
# Your grade is: C


# 2 example

# Define variables
age = 25
income = 50000

# Check eligibility for loan
if age >= 18:
    if income >= 30000:
        loan_amount = 200000
        print("Congratulations! You are eligible for a loan of $", loan_amount)
    elif income >= 20000:
        loan_amount = 100000
        print("Congratulations! You are eligible for a loan of $", loan_amount)
    else:
        print("Sorry, your income is too low for a loan.")
else:
    print("Sorry, you must be at least 18 years old to apply for a loan.")


# Output
# Congratulations! You are eligible for a loan of $ 200000