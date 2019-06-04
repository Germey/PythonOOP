class Color(object):
    """
    Color Object of RGB
    """

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        """
        to string
        :return:
        """
        return f'{self.__class__.__name__}(r={self.r}, g={self.g}, b={self.b})'

    def __lt__(self, other):
        """
        :param other:  the other Color object to compare with
        :return: bool
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.r, self.g, self.b) < (other.r, other.g, other.b)


if __name__ == '__main__':
    color = Color(255, 255, 255)
    print(color)
