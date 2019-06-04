from attr import attrs, attrib, fields


@attrs
class Point(object):
    x = attrib(default=None)
    y = attrib(default=100)

print(fields(Point))
if __name__ == '__main__':
    print(Point(x=1, y=3))
    print(Point())
