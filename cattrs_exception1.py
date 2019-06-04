from typing import Set
from attr import attrs, attrib
import cattr


@attrs
class Point(object):
    x = attrib(type=int, default=0)
    y = attrib(type=int, default=0)


def drop_nonattrs(d, type):
    if not isinstance(d, dict): return d
    attrs_attrs = getattr(type, '__attrs_attrs__', None)
    if attrs_attrs is None:
        raise ValueError(f'type {type} is not an attrs class')
    attrs: Set[str] = {attr.name for attr in attrs_attrs}
    return {key: val for key, val in d.items() if key in attrs}


def structure(d, type):
    return cattr.structure(drop_nonattrs(d, type), type)


json = {'x': 1, 'y': 2, 'z': 3}
print(structure(json, Point))
