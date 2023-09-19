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
    if a == b and b == c:
        print("Равностраннен")
    elif a == b or a == c or b == c:
        print("Равнобедрен")
    else:
        print("разностранен")
