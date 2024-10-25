def fibo(n):
    # u=[1,1]
    # for i in range(n - 1):
    #     u.append(u[i] + u[i + 1])
    # return u[len(u) - 1]
    u=1
    v=1
    w=None
    if n == 0:
        return u
    
    if n == 1:
        return v
    
    for i in range(n-1):
        w = u
        u += v
        v = w
    
    return u

assert fibo(7) == 21

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)
    
assert fibonacci(8) == 21
