from attr import attrs, attrib
from typing import List
from cattr import structure, unstructure


@attrs
class Point(object):
    x = attrib(type=int, default=0)
    y = attrib(type=int, default=0)


@attrs
class Color(object):
    r = attrib(default=0)
    g = attrib(default=0)
    b = attrib(default=0)


@attrs
class Line(object):
    color = attrib(type=Color)
    points = attrib(type=List[Point])


if __name__ == '__main__':
    line = Line(color=Color(), points=[Point(i, i) for i in range(5)])
    print('Object:', line)
    json = unstructure(line)
    print('JSON:', json)
    line = structure(json, Line)
    print('Object:', line)
