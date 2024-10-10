# Using a function create a program that calcuates calculates the volume of a cylinder.
import math
def volume_of_a_cylinder():
    radius = int(input("Enter the radius of a cylinder: "))
    height = int(input("Enter the height of a cylinder: "))
    volume = (math.pi * (radius**2)*height)
    print(f"The volume of the cylindre with radius {radius} and height {height} is {volume}")
volume_of_a_cylinder()
    