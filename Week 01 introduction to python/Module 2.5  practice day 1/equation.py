x, n=map(int, input().split())

sum=0
for i in range(2, n, 2):
    value=x**i
    sum=sum+value

print(sum)