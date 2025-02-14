#Obtains Data from the user
def get_data():
    try:
        height = float(input("Enter Height: "))
        radius = float(input("Enter Radius: "))
        calculate_volume(radius, height)
    except ValueError:
        print("Ensure both values are numbers.")
        get_data()

# Calculates the volume of a cylinder
def calculate_volume(radius, height):
    volume = 3.142 * radius * radius * height
    print(f"The volume is: {volume}")

get_data()
