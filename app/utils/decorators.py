import functools
import time

def log_call(func):
    """Decorator: logs when a function is called."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper

def timeit(func):
    """Decorator: measures execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = (time.time() - start) * 1000
        print(f"[TIME] {func.__name__} took {elapsed:.2f} ms")
        return result
    return wrapper