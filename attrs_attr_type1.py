from attr import attrs, attrib


@attrs
class Point(object):
    x = attrib(type=int)
    y = attrib()


if __name__ == '__main__':
    print(Point(100, 3))
    print(Point('100', 3))
