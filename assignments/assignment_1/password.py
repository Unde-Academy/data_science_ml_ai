# input_password = input("Enter your password: ")
# print(input_password[ : : -1])


# def check_password(user_password):
#   return user_password[ : : -1]

# print(check_password("password1234"))

def reverse_password (user_password):
  user_password = input("Enter your password: ")
  reversed_password = user_password[ : : -1]
  print(reversed_password)
reverse_password("user_password")