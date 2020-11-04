read_data = open("data.txt", 'r')
write_data = open('data.txt', 'w')
data = read_data.readlines()

# for i in data:
#     print(i, end='')
# print(data[0].rstrip(),end='')
# print(data[1].rstrip(),end='')

# l = []
# num = input()
# l.append(num+'\n')
# apikey = input()
# l.append(apikey)
# f = open('data.txt', 'w')
# f.writelines(l)

if len(data)==0:
    num = input("Enter your phone number: ")+'\n'
    api = input("Enter your fast2sms api key: ")
    data.append(num)
    data.append(api)
    write_data.writelines(data)
else:
    print("data")
