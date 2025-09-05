#perimeter of a rectangle
def calculate_perimeter(length,width):
    perimeter= 2*(length+width)
    return perimeter
#input data
length=int(input("enter the length:"))
width=int(input("enter the width:"))
#calculate the perimeter
perimeter=calculate_perimeter(length,width)
print("perimeter=",perimeter)
