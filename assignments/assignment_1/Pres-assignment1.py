def calculate_cylinder_volume(radius, height):
    """
    Calculate the volume of a cylinder.

    Parameters:
        radius (float): The radius of the cylinder's base.
        height (float): The height of the cylinder.

    Returns:
        float: The volume of the cylinder.
    """
    pi = 3.142
    volume = pi * (radius ** 2) * height
    return volume

radius = 5
height = 10
volume = calculate_cylinder_volume(radius, height)
print(f"The volume of the cylinder is: {volume}")