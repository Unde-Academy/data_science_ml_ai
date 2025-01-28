# Define a function called calculate_triangle_area so it can be reused
#Take Parameters  as the function accepts base and height as inputs, making it flexible for different values

def calculate_triangle_area(base,height) :
    """
    Calculate the area of a triangle given its base and height.
    :param base: The length of the base of the triangle
    :param height: The height of the triangle
    :return: The area of the triangle
    """
    
    # Calculate the area using the formula
    area = 0.5 * base * height
    return area

# How we will use it
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

#Lets test if our formular works
print("The area of the triangle is:", calculate_triangle_area(base, height))



