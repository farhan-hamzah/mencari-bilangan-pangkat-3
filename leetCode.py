N = int(input())
if N <= 0:
    T = False
while N%3 == 0:
    N //= 3
if N == 1:
    T = True
else:
    T = False
print(T)