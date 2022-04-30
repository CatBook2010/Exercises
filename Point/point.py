class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distance(self, point):
        x1, y1 = self.__x, self.__y
        x2, y2 = point.getX(), point.getY()
        return ((x2-x1)**2+(y2-y1)**2)**(1/2)

    def isNearBy(self, p1):
        distance = self.distance(p1)
        return distance < 5

    def __str__(self):
        return f"({self.__x}, {self.__y})"