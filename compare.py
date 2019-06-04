from attr import attrs, attrib


@attrs
class Point(object):
    x = attrib()
    y = attrib()


if __name__ == '__main__':
    p1 = Point(1, 2)
    print(p1)
    p2 = Point(x=1, y=2)
    print(p2)
    print('Same:', Point(1, 2) is Point(1, 2))
    print('Equal:', Point(1, 2) == Point(1, 2))
    print('Not Equal(ne):', Point(1, 2) != Point(3, 4))
    print('Less Than(lt):', Point(1, 2) < Point(3, 4))
    print('Less or Equal(le):', Point(1, 2) <= Point(1, 4), Point(1, 2) <= Point(1, 2))
    print('Greater Than(gt):', Point(4, 2) > Point(3, 2), Point(4, 2) > Point(3, 1))
    print('Greater or Equal(ge):', Point(4, 2) >= Point(4, 1))
