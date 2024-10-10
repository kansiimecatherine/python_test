#Question 1(a)
# Create a program that calculates the area of a triangle.
def area_of_the_triangle():
    base = float(input("\nEnter the base of the triangle:  "))
    height = float(input("Enter the height of the triangle:  "))
    area = (1/2)*base*height
    print(f"The area of a triangle with base {base} and height {height} is equal to {area:}",end='\n\n')
area_of_the_triangle()

