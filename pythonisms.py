  
import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


#########################################################################################333
@slow_down  ## using decorators to slow down below function
def factors1(n): ## to find the factorial (method 1)
    results = [ ]
    for k in range(1,n+1):
        if n % k == 0: results.append(k)
    return results
## Generator that produces the same numbers but under each other not in a list
@slow_down
def factors2(n):   ## to find the factorial (method 2)
    for k in range(1,n+1):
        if n % k == 0: 
            yield k

print(factors1(100))

## output : [1, 2, 4, 5, 10, 20, 25, 50, 100]
for factor in factors2(100):
    print(factor)







