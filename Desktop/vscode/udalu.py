n = int(input())
m = int(n // 2)
for p in range(1,m+2):
    print("*" * p)
for i in range(n-m-1,0,-1):
    print("*" * i)