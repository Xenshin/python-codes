from turtle import width


class Rectangle:
    def __init__ (self, length, width):
        self.__length = length
        self.__width = width
    
    def area(self):
        area = self.__length*self.__width
        return area

    def perimeter(self):
        perimeter = 2*(self.__length + self.__width)
        return perimeter