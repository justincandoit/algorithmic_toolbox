# Uses python3
# LCM(𝑎, 𝑏)· GCD(𝑎, 𝑏) = 𝑎 · 𝑏.
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

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

def LCM(a, b):
    gcd = GCD(a, b)
    return (a*b)//(gcd)




if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print((LCM(a, b)))

