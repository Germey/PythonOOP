from attr import attrs, attrib
from cattr import unstructure, structure


@attrs
class Point(object):
    x = attrib(type=int, default=0)
    y = attrib(type=int, default=0)


if __name__ == '__main__':
    point = Point(x=1, y=2)
    json = unstructure(point)
    print('json:', json)
    obj = structure(json, Point)
    print('obj:', obj)
