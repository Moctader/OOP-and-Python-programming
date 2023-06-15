# x = (int(x) for x in input("Enter multiple values: ").split())
# print("Number of list is: ", x)


# def print_digit_rigth_left(n):
#     num_str=str(n)
#     for digit in num_str[::-1]:
#         print(digit, end=" ")

# print_digit_rigth_left(x)

test_case=int(input())
for n in range(test_case):
    n=input()

    Num_str=str(n)
    for digit in Num_str[::-1]:
        print(digit, end=" ")
