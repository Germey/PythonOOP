from attr import attrs, attrib, Factory
import typing


@attrs
class Point(object):
    x = attrib(type=int)
    y = attrib(type=typing.List[int])
    z = attrib(type=Factory(list))


if __name__ == '__main__':
    print(Point('100', 2, [1, 2, 4]))
