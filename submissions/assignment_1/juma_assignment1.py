def circle_area(radius):
 
    pi = 3.142
    if radius < 0:
        return "Radius cannot be negative."
    diameter = 2 * radius
    area = pi * (radius ** 2)
    return diameter, area

radius = float(input("Enter the radius of the circle: "))
result = circle_area(radius)

if isinstance(result, str):
    print(result)
else:
    diameter, area = result
    print(f"The diameter of the circle is: {diameter}")
    print(f"The area of the circle is: {area}")
