import datetime
from attr import attrs, attrib
import cattr

TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


@attrs
class Event(object):
    happened_at = attrib(type=datetime.datetime)


cattr.register_unstructure_hook(datetime.datetime, lambda dt: dt.strftime(TIME_FORMAT))
cattr.register_structure_hook(datetime.datetime,
                              lambda string, _: datetime.datetime.strptime(string, TIME_FORMAT))

event = Event(happened_at=datetime.datetime(2019, 6, 1))
print('event:', event)
json = cattr.unstructure(event)
print('json:', json)
event = cattr.structure(json, Event)
print('Event:', event)
