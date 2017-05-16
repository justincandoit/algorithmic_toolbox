# Uses python3
def calc_fib(n):
    f=[0,1]
    if (n <= 1):
        return n
    else:
        for i in range(2, n + 1):
            f.append(f[i - 2] + f[i - 1])
        return (f[n])


n = int(input())
print(calc_fib(n))
