import time
import contextlib
import traceback

def ctime():
    return int(time.time())

@contextlib.contextmanager
def error_block(**kwargs):
    try:
        yield
    except Exception as e:
        traceback.print_exc(e)
