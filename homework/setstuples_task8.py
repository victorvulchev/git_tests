x1 = int(input("coordinates for x1:"))
y1 = int(input("coordinates for y1:"))
x2 = int(input("coordinates for x2:"))
y2 = int(input("coordinates for y2:"))
x3 = int(input("coordinates for x3:"))
y3 = int(input("coordinates for y3:"))
import math

a = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
b = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
c = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
print(a)
print(b)
print(c)

if c < a + b and b + c > a and a + c > b:
    # sin_a = a / c
    # sin_b = b / c
    # to_print = math.degrees(math.asin(sin_a))
    # to_print2 = math.degrees(math.asin(sin_b))
    # print(to_print)
    # print(to_print2)
    hyp = 0
    if c == math.sqrt(a**2 + b**2):
        hyp = c
        side_a = a
        side_b = b
    elif a == math.sqrt(c**2 + b**2):
        hyp = a
        side_a = c
        side_b = b
    else:
        hyp = b
        side_a = a
        side_b = c
    angle_A = math.degrees(math.acos((side_b**2 + hyp**2 - side_a**2) / (2 * side_b * hyp)))
    angle_B = math.degrees(math.asin((side_a / hyp)))
    angle_C = 180 - angle_A - angle_B
    #can't find angles
    print(angle_A)
    print(angle_B)
    print(angle_C)
    if angle_A == 90 or angle_B == 90 or angle_C == 90:
        print("The triangle has a 90 degree angle")
else:
    print("Not a triangle")