from attr import attrs, attrib, validators


def is_valid_gender(instance, attribute, value):
    if value not in ['male', 'female']:
        raise ValueError(f'gender {value} is not valid')
        # return False


def is_less_than_100(instance, attribute, value):
    if value > 100:
        raise ValueError(f'age {value} must less than 100')


@attrs
class Person(object):
    name = attrib()
    gender = attrib(validator=is_valid_gender)
    age = attrib(validator=[validators.instance_of(int), is_less_than_100])


if __name__ == '__main__':
    print(Person(name='Mike', gender='male', age=500))
