from time import time

def time_it(func):
    def timed(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function took {(t2-t1):.4f} seconds to run')
        return result
    return timed
