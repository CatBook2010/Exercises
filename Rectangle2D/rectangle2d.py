class Rectangle2d:
    def __init__(self, x, y, width, height):
        self.__x
        self.__y
        self.__width = width
        self.__height = height
    
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def getPerimeter(self):
        return 2 * (self.getHeight() + self.getWidth())
    
    def getArea(self):
        return self.getWidth() * self.getHeight()