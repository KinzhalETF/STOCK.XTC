import random

# Function to generate a random 7-digit phone number
def generate_phone_number():
    # The first digit should not be 0 or 1 to ensure it's a valid area code
    first_digit = random.randint(2, 9)
    rest_of_number = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return f"207-{first_digit}{rest_of_number}"

# Number of phone numbers to generate
num_numbers = 10  # Change this to the desired number of phone numbers

# Generate and print the list of phone numbers
phone_numbers = [generate_phone_number() for _ in range(num_numbers)]
for number in phone_numbers:
    print(number)
