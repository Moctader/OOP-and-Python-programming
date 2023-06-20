
def count_numbers(N, M, A):
    count_dict={}

    for num in A:
        if num not in count_dict:
            count_dict[num]=1
        else:
            count_dict[num]+=1


    for i in range(1, M+1):
        if i in count_dict:
            print(f'{i} appears {count_dict[i]} times in an array')
        # else:
        #     print(f"Number {i} appears 0 times.")

    

N=int(input())
M=int(input())
A=[]
for i in range(N):
    k=input("Enter value")
    A.append(int(k))

count_numbers(N,M,A)