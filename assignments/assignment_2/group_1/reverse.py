# Function to reverse a password using the slicing technique
def reverse(password):
    return password[::-1]

# Get input from the user
password = input("Enter your password: ")

# Reverse the password
reversed_password = reverse(password)

# Print the reversed password
print("Reversed password: ", reversed_password)