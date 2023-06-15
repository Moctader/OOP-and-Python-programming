from collections import Counter

def min_num_removed(values):
    count=Counter(values)
    removed_num=0

    for x in count:
        if count[x]>x:
            removed_num+=count[x]-x
        elif count[x]<x:
            removed_num+=x-count[x]
    return removed_num


N=int(input())

values=list(map(int, input().split()))

removed=min_num_removed(values)
print(removed)