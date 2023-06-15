test_case=int(input())

for i in range(test_case):
    x,y=map(int, input().split())

    sum=0

    start=min(x,y)+1
    end=max(x,y)

    for num in range(start,end):
        if num%2!=0:
            sum=sum+num
    
    print(sum)
