from point import Point

x1 = float(input("Input x for point 1: "))
y1 = float(input("Input y for point 1: "))
x2 = float(input("Input x for point 2: "))
y2 = float(input("Input y for point 2: "))

point_1 = Point(x1, y1)
point_2 = Point(x2, y2)

print(f"Here is the distance beetween them: {point_1.distance(point_2)}.")

isNearBy = point_1.isNearBy(point_2)
if isNearBy:
    print("Your points are near each other.")
else:
    print("Your points are far from each other.")