from attr import s, ib

@s
class Color(object):
    r = ib(type=int, default=0)
    g = ib(type=int, default=0)
    b = ib(type=int, default=0)

if __name__ == '__main__':
    color = Color(255, 255, 255)
    print(color)