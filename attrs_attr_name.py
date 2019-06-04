from attr import attrs, attrib, fields


@attrs
class Point(object):
    x = attrib()
    y = attrib()

print(fields(Point))
