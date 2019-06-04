from attr import attrs, attrib


def to_int(value):
    try:
        return int(value)
    except:
        return None


@attrs
class Point(object):
    x = attrib(converter=to_int)
    y = attrib()


if __name__ == '__main__':
    print(Point('100', 3))
