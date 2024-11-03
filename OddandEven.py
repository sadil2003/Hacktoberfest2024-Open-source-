# Function to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input from the user
num = int(input("Enter a number: "))

# Display result
result = check_odd_even(num)
print(f"The number {num} is {result}.")
