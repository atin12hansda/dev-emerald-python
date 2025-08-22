#calculate circumferemce of a circle
import math
def circumference(radius):
    return 2 * math.pi * radius

#calculate area of a circle
def area(radius):
    return math.pi * radius ** 2

#calculate diameter of a circle
def diameter(radius):
    return 2 * radius

#calculate arc length of a circle
def arc_length(radius, angle):
    return (angle / 360) * circumference(radius)

# use the functions
if __name__ == "__main__":
    r = 5
    print(f"Circumference of circle with radius {r}: {circumference(r)}")
    print(f"Area of circle with radius {r}: {area(r)}")
    print(f"Diameter of circle with radius {r}: {diameter(r)}")
    angle = 90
    print(f"Arc length of circle with radius {r} and angle {angle}: {arc_length(r, angle)}")
    print("All calculations completed successfully.")
    print("You can now use these functions in your projects.")
    print("Thank you for using the circle calculations module!")
    print("Feel free to modify and expand the code as needed.")
    print("Have a great day!")
    print("Remember to import the math module for mathematical operations.")
    print("This module is designed to help with basic circle calculations.")
    print("You can also add more functions for other geometric shapes.")
    print("Consider contributing to the codebase if you find it useful.")