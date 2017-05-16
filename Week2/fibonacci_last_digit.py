# Uses python3
import sys


def get_fibonacci_last_digit(n):
    f = [0, 1]
    if (n <= 1):
        return n
    else:
        c=1
        p=0
        for i in range(2, n + 1):
            c, p = (c+p) %10,c

        return c
if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit(n))
