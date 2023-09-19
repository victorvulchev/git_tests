x1 = int(input("coordinates for x1:"))
y1 = int(input("coordinates for y1:"))
x2 = int(input("coordinates for x2:"))
y2 = int(input("coordinates for y2:"))
x3 = int(input("coordinates for x3:"))
y3 = int(input("coordinates for y3:"))
x4 = int(input("coordinates for x4:"))
y4 = int(input("coordinates for y4:"))
import math
distance_1 = math.sqrt(x1**2 + y1**2)
distance_2 = math.sqrt(x2**2 + y2**2)
distance_3 = math.sqrt(x3**2 + y3**2)
distance_4 = math.sqrt(x4**2 + y4**2)
points = [(-1, 4), (5, 6), (-2, 2), (2, 2)]

# points = [(-1, 4), (5, 6), (-2, 2), (2, 2)]
# def distance_to_origin(point):
#     x, y = point
#     return math.sqrt(x**2 + y**2)
# sorted_points = sorted(points, key=distance_to_origin)
# for point in sorted_points:
#     print(point)
