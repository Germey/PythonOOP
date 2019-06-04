from attr import attrs, attrib


@attrs
class SmartClass(object):
    a = attrib()
    b = attrib()


class RoughClass(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "RoughClass(a={}, b={})".format(self.a, self.b)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.a, self.b) == (other.a, other.b)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.a, self.b) < (other.a, other.b)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.a, self.b) <= (other.a, other.b)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.a, self.b) > (other.a, other.b)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.a, self.b) >= (other.a, other.b)
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.__class__, self.a, self.b))
