from attr import attrs, attrib, validators


def is_valid_gender(instance, attribute, value):
    if value not in ['male', 'female']:
        raise ValueError(f'gender {value} is not valid')
        # return False


@attrs
class Person(object):
    name = attrib()
    gender = attrib(validator=is_valid_gender)
    age = attrib(validator=validators.instance_of(int))


if __name__ == '__main__':
    print(Person(name='Mike', gender='male', age=12))
    print(Person(name='Mike', gender='male', age='12'))
    print(Person(name='Mike', gender='mlae', age=12))
