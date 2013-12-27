

def memoized(func):
    memory = {}

    def wrapped(*args):
        if args in memory:
            return memory[args]

        ret = func(*args)
        memory[args] = ret

        return ret

    return wrapped

def product(ns):
    total = 1
    for n in ns:
        total *= n
    return total
