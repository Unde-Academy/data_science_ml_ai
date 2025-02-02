def reverse(password): 
    reversed = password[::-1]
    print(f"the reversed string of {password} is {reversed}")
password = input("enter password: ")
reverse(password)