def count_numbers(N, M, A):
    count_dict = {}  # Dictionary to store count of each number

    for num in A:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    for i in range(1, M + 1):
        if i in count_dict:
            print(f"Number {i} appears {count_dict[i]} times.")
        else:
            print(f"Number {i} appears 0 times.")


# Example usage
N = 7
M = 5
A = [1, 3, 2, 3, 4, 2, 1]

count_numbers(N, M, A)

# list=[]
# n=int(input())
# for i in range(n):
#     k=input("Enter value: ")
#     list.append(int(k))
# print(list)