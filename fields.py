from attr import attrs, attrib, fields


@attrs
class Point(object):
    x = attrib()
    y = attrib()


print(fields(Point))

if __name__ == '__main__':
    p = Point(x=1, y=2)
    print(p)
