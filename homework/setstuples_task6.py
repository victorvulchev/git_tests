x1 = int(input("coordinates for x1:"))
y1 = int(input("coordinates for y1:"))
x2 = int(input("coordinates for x2:"))
y2 = int(input("coordinates for y2:"))
import math

distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(distance)