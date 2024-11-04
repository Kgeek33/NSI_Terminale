def trouve_iter(x: any, lst: list[any]):
    a = 0
    for i in lst:
        if x == i:
            a += 1

    return None if a == 0 else a

assert trouve_iter(3, [3, 3, 3]) == 3


def trouve_rec(x: any, lst: list[any]):
    if x not in lst:
        return None
    
    return trouve_rec(x, lst[:-1])

assert trouve_rec(3, [3, 3, 3]) == 3
