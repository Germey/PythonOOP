from attr import attrs, attrib


@attrs
class Point(object):
    x = attrib(init=False, default=10)
    y = attrib()


if __name__ == '__main__':
    print(Point(1, 3))
