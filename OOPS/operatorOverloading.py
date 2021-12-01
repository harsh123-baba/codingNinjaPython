
import math
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "this the point class ("

    def get(self):
        print(self.__x, self.__y)

    def __add__(self, point_object):
        return Point(self.__x + point_object.__x, self.__y + point_object.__y)

    def __lt__(self, point_object):
        return math.sqrt(self.__x**2 + self.__y**2) < math.sqrt(point_object.__x**2+point_object.__y**2)

p1 = Point(2, 3)
p2 = Point(3, 3)
p3 = p1+p2

print(p3)
p3.get()
print(p1<p2)



