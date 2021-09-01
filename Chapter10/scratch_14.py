def fibo():
    cur, prev = 0, 1
    while True:
        yield cur
        cur, prev = cur + prev, cur
fib = fibo()
for i in range(21):
    print(next(fib))
