
def possible_max_operation(A):
    max_oper=0
    
    is_even=all(num%2==0 for num in A)

    while is_even:
        A=[num//2 for num in A]
        max_oper+=1
        is_even=all(num%2==0 for num in A)
    return max_oper

N =int(input())
A=list(map(int, input().split()))

max_operation=possible_max_operation(A)
print(max_operation)
