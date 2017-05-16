# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    vw = []
    for i in range(len(weights)):
        vw.append((values[i], weights[i], (values[i])/weights[i]))
    # print(vw)
    vws = sorted(vw, key=lambda x:x[2], reverse=True)


    for i in vws:
        if capacity == 0:
            break
        else:
            amount = min(i[1], capacity)
            value += (amount*i[2])
            capacity = capacity - amount
    return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
