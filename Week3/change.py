# Uses python3
import sys

def get_change(m):
    if m != 0:
        d = 0
        n = 0
        p = 0

        if m >=10:
            d = m//10
            m = m - (d*10)

        if m >= 5:
            n = m//5
            m = m - (n*5)

        if m >=1:
            p = m//1

    else:
        return 0


    return d+n+p

def get_change_better(m):
    result = 0
    result += m//10
    m = m % 10
    result += m//5
    m = m % 5
    result += m
    return result

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = int(input())
    print(get_change_better(m))

