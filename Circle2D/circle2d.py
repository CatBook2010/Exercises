from math import pi

class Circle2D:
    def __init__(self, x=0, y=0, radius=0):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, newX):
        self.__x = newX

    def setY(self, newY):
        self.__y = newY

    def getRadius(self):
        return self.__radius

    def setRadius(self, newRadius):
        self.__radius = newRadius

    def getArea(self):
        return pi * self.__radius ** 2

    def getPerimeter(self):
        return 2 * pi * self.__radius

    def getDistance(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def containsPoint(self, x, y):
        return self.getDistance(self.__x, self.__y, x, y) <= self.__radius

    def contains(self, circle2D):
        return (self.getDistance(circle2D.getX(), circle2D.getY(), self.__x, self.__y) + circle2D.getRadius()) < self.__radius

    def overlaps(self, circle2D):
        return (self.getDistance(circle2D.getX(), circle2D.getY(), self.__x, self.__y) - circle2D.getRadius()) < self.__radius

    def __contains__(self, another):
        return (self.getDistance(circle2D.getX(), circle2D.getY(), self.__x, self.__y) + self.__radius) < circle2D.getRadius()

    def __eq__(self, circle2D):
        return self.__radius == circle2D.getRadius()