# Uses python3
result = 0


def mpp(n, a):
    result = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    return result

def mppf(n, a):
    max1 = -1
    for i in range(n):
        if a[i] > a[max1] or max1 == -1:
            max1 = i



    max2 = -1
    for i in range(n):
        if i != max1 and(a[i] > a[max2] or max2 == -1):
            max2 = i

    return a[max1]*a[max2]


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == n)

    print(mppf(n, a))