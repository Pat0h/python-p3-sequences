#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print('[]')
        return []
    elif length == 1:
        print('[0]')
        return [0]
    elif length == 2:
        print('[0, 1]')
        return 1
    else:
        fib_sequence = [0,1]
        for i in range(2,length):
            next=fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next)
        print(f"[{', '.join(str(num) for num in fib_sequence)}]")
        return fib_sequence
print_fibonacci(10)
