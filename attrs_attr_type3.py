from attr import attrs, attrib, Factory
import typing


@attrs
class Point(object):
    x = attrib(type=int, default=0)
    y = attrib(type=int, default=0)


@attrs
class Line(object):
    name = attrib()
    points = attrib(type=typing.List[Point])


if __name__ == '__main__':
    points = [Point(i, i) for i in range(5)]
    print(points)
    line = Line(name='line1', points=points)
    print(line)
