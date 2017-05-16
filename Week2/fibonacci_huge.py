# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fib_huge_mod(n, m):
    if (n == 0):
        return 0

    fib = {0:0, 1:1}
    mod = {0:0, 1:1}

    i = 2

    while True:
        fib.setdefault(i, (mod[i-2] + mod[i-1]) % 10)
        mod.setdefault(i, fib[i] % m)


        if(mod[i-1] == 0 and mod[i] == 1):
            break
        i += 1
    print(fib)
    print(mod)
    remainder = n % (i-1)
    return fib[remainder] % m





if __name__ == '__main__':
    # input = sys.stdin.read();
    input = input();
    n, m = map(int, input.split())
    print(get_fib_huge_mod(n, m))
