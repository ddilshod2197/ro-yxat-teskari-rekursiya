import time
from functools import wraps

def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funksiya {func.__name__} bajarilish vaqti: {end_time - start_time} sekund")
        return result
    return wrapper

@time_decorator
def example_function():
    time.sleep(2)
    print("Funksiya bajarildi")

example_function()
