import math
points = [(-1, 4), (5, 6), (-2, 2), (2, 2)]

def distance_to_origin(point):
    x, y = point
    return math.sqrt(x**2 + y**2)

sorted_points = sorted(points, key=distance_to_origin)

new_list = sorted(sorted_points, key=lambda x: x[0]) #incorrect

for point in new_list:
    print(point)