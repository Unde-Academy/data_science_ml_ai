#radius = input("enter the radius:")
#pi = 3.142
#area = pi * radius**2
#print(area) 
import math
def calculate_area(radius):
    return math.pi * radius ** 2
radius = float(input("enter the radius:"))
area = calculate_area(radius)
print(area)