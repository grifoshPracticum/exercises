import time

a = ['alex', 'bob', 'john']
b = ['alice', 'bob', 'anna']


def merge_unique_arrays(*arrays):
    return list(
        set(
            [element for array in arrays for element in array]
        ))


print(merge_unique_arrays(a, b))


def decorator_factory(argument):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(func.__name__, argument)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@decorator_factory('sec')
def cpu_consumer():
    time.sleep(2)
