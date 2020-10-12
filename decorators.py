from functools import wraps

def lowerize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_value = func(*args, **kwargs)
        return original_value.lower()
    return wrapper

def camelize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_value = func(*args, **kwargs)
        return original_value.title()
    return wrapper


@camelize
@lowerize
def fun_with_words(first_noun, second_noun, verb):
    return f"{first_noun}s love  {verb}ing ALL the {second_noun}s"


print(fun_with_words('Dog','Banana','PLAY'))

