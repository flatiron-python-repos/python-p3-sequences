#!/usr/bin/env python3

def print_fibonacci(length):
    n1 = 0
    n2 = 1
    fib = [n1]
    # if (not length or length == 1):
    #     print([0])
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        for i in range(length - 1):
            fib.append(n2)
            nth = n1 + n2
            n1 = n2
            n2 = nth

        print(fib)


print_fibonacci(1)
