# with open('message.txt','w') as file:
#     file.write('it\'s amazing')

# with open('message.txt','a') as file:
#     file.write('it\'s amazing \n')

with open('message.txt','r') as file:
    text=file.read()
    print(text)