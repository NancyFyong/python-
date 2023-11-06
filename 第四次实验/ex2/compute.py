# main.py
from rectangle import calculate_rectangle_area, calculate_rectangle_perimeter
from circular import calculate_circle_area, calculate_circle_circumference

# 计算矩形的面积和周长
length = 5
width = 3
rectangle_area = calculate_rectangle_area(length, width)
rectangle_perimeter = calculate_rectangle_perimeter(length, width)
print(f"矩形面积: {rectangle_area}")
print(f"矩形周长: {rectangle_perimeter}")

# 计算圆形的面积和周长
radius = 4
circle_area = calculate_circle_area(radius)
circle_circumference = calculate_circle_circumference(radius)
print(f"圆形面积: {circle_area}")
print(f"圆形周长: {circle_circumference}")
