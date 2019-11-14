from typing import Dict
from functools import lru_cache
from typing import Generator
#1
'''def fib2(n):
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)
print(fib2(5))




#2

memo: Dict[int,int] = {0:0,1:1}

def fib3(n):
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]

if __name__ == "__main__":
    print(fib3(400))

#3

@lru_cache(maxsize=None)
def fib4(n):
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)
if __name__ == "__main__":
    print(fib4(10))


#4

def fib5(n):
    if n == 0:
        last: int = 0
        next: int = 1
        

        for _ in range(1,n):
            last,next = next, last+ next
        return next
if __name__ == "__main__":
    print(fib5(10))
 

#5

def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next # главный этап генерации
if __name__ == "__main__":
    for i in fib6(50):
        print(i)



        

