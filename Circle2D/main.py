from circle2d import Circle2D

x1_y1_radius1 = list(map(float, input("Enter x1, y1, radius1: ").split(", ")))
x2_y2_radius2 = list(map(float, input("Enter x2, y2, radius2: ").split(", ")))

x1 = x1_y1_radius1[0]
y1 = x1_y1_radius1[1]
radius1 = x1_y1_radius1[2]

x2 = x2_y2_radius2[0]
y2 = x2_y2_radius2[1]
radius2 = x2_y2_radius2[2]

c1 = Circle2D(x1, y1, radius1)
c2 = Circle2D(x2, y2, radius2)

print(f"Area for c1 is {c1.getArea()}.")
print(f"Perimeter for c1 is {c1.getPerimeter()}.")

print(f"Area for c2 is {c2.getArea()}.")
print(f"Perimeter for c2 is {c2.getPerimeter()}.")

print(f"c1 contains centre of c2? {c1.containsPoint(c2.getX(), c2.getY())}")
print(f"c1 contains c2? {c1.contains(c2)}")
print(f"c1 overlaps c2? {c1.overlaps(c2)}")

# 5, 5.5, 10
# 9, 1.3, 10