


class ShapeException(Exception):
    pass


def shape(n):
    return len(n), len(n[1])



def vector_add(x, y):
     """
    [a b]  + [c d]  = [a+c b+d]
    Matrix + Matrix = Matrix
    """
    return [x[n] + y[n] for n in range(len(x))]




def vector_sub(x, y):
     """
    [a b]  - [c d]  = [a-c b-d]
    Matrix - Matrix = Matrix
    """
    return [x[n] - y[n] for n in range(len(x))]

def vector_sum(*args):
    res = list(zip(*args))
    for n in *args[1:]:
        res =vector_add()
    return [sum(n) for n in zip(*args)]



def dot(x, y):
    return sum([x[n] * y[n] for n in range(len(a))])

def vector_multiply(x, y):
    return [n * y for n in x]


def vector_mean():
    pass

def magnitude():
    pass
