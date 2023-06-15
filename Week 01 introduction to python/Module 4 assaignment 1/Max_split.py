def split_string(s):
    count=0
    cur_str=""
    result=[]

    for ch in s:
        cur_str+=ch

        if ch=='R':
            count+=1
        else:
            count-=1
        if count==0:
            result.append(cur_str)
            cur_str=""
    return result

s=input()
balance_string=split_string(s)
print(len(balance_string))

for string in balance_string:
    print(string)