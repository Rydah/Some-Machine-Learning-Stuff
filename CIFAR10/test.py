def f(n, counter):
    i = 2
    while i <n:
        i = i * i
        for j in range(i):
            counter += 1
    return counter

print(f(1000000, 0))