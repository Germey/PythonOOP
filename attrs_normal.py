from attr import attrs, attrib

@attrs
class Color(object):
    r = attrib(type=int, default=0)
    g = attrib(type=int, default=0)
    b = attrib(type=int, default=0)

if __name__ == '__main__':
    color = Color(255, 255, 255)
    print(color)