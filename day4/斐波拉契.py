def fib(MAX):
    n,a,b = 0,0,1
    while n<MAX:
        yield (b)
        a,b = b,a+b
        n= n+1
    return "done"

print(fib(10))
f = fib(10)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print("-------")
print(f.__next__())