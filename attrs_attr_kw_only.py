from attr import attrs, attrib, fields


@attrs
class Point(object):
    x = attrib(default=0)
    y = attrib(kw_only=True)


if __name__ == '__main__':
    print(Point(1, 3))
