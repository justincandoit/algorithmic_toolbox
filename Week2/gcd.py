# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
def GCD(a,b):
    if a>b:
        while b != 0:
            bb = b
            b = a%b
            a = bb
        return a
    elif b>1:
        while a != 0:
            aa = a
            a = b%a
            b = aa
        return b
    else: a = (1)
    return a


if __name__ == "__main__":
    # input = sys.stdin.read()
    input = input()
    a, b = map(int, input.split())
    print(GCD(a, b))
