#Uses python3

import sys

def firstdigit(elem):
    return elem[0]

def isgore(a, maxb):
    a = str(a) + str(maxb)
    maxb = str(maxb) + str(a)
    if a > maxb:
        return True
    else:
        return False




def largest_number(a):
    answer = []
    while a != []:
        maxdigit = int('-99999')
        for digit in a:
            digit = int(digit)
            if isgore(digit, int(maxdigit)):
                maxdigit = digit
        answer.append(maxdigit)
        a.remove(maxdigit)


    res = ""
    for x in answer:
        res += str(x)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    a = data[1:]
    print(largest_number(a))
