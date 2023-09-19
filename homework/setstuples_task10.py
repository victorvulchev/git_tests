x1 = int(input("coordinates for x1:"))
y1 = int(input("coordinates for y1:"))
x2 = int(input("coordinates for x2:"))
y2 = int(input("coordinates for y2:"))
import math

distance_1 = math.sqrt(x1**2 + y1**2)
distance_2 = math.sqrt(x1**2 + y1**2)

if distance_1 == distance_2:
    print("they are the same distance away from the start")
else:
    if distance_1 > distance_2:
        print("They are not the same distance from the start. Point 2 is closer")
    else:
        print("They are not the same distance from the start. Point 1 is closer")
