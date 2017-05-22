import math

class Point:
    """
    Represents a point in 2-D geometric space
    """

    def __init__(self,x=0, y=0):
        """
        Initializes the position of a new point.
        If they are not specified, the point defaults to the origin
        :param x:
        :param y:
        """

        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        """
        Calculate the distance from this point to a second point passed as a parameter.
        This function uses the Pythagorean Theorem to calculate the distance between the two points
        :param other_point: second point to calculate distance
        :return: The distance between two points (float)
        """

        return math.sqrt(
            ((other_point.x-self.x)**2)+((other_point.y-self.y)**2))

    def reset(self):
        """
         Reset the point to the origin
        :return: Nothing
        """

        self.x=0
        self.y=0

    def move(self, x,y):
        """
         Move a point to a new location in 2D space
        :param x: x-
        :param y:
        :return:
        """

        self.x = x
        self.y = y



def main():
    p1 = Point()
    print(p1.x, p1.y)
    p2 = Point(5, 8)
    print(p2.x, p2.y)
    p2.reset()
    print(p2.x, p2.y)
    p2.move(9, 10)
    print(p2.x, p2.y)
    print(p1.calculate_distance(p2))
    # Test tool (assert)
    # program will exit if False (or zero, empty, None)
    assert (p2.calculate_distance(p1) ==
            p1.calculate_distance(p2))


if __name__ == '__main__':
    main()
    exit(0)
