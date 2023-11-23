import math

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

radius = float(input())
area = calculate_circle_area(radius)
V = calculate_sphere_volume(radius)
print(f"The area of the circle with radius {radius} is: {area}")
print(f"The V of the sphere with radius {radius} is {V}")
