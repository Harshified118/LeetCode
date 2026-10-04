# sub=10
# add=1
# num = 7
# while sub >0:
#     tab = num *add
#     add +=1
#     sub -=1
#     print(tab)

num =int(input("Enter the Number : "))
change = str(num)
while len(change) >0:
    for i in change:
        change2 = int(str)
        change2 += i
        print(change2)


a=[]
len=int(input("Enter the number of element you want to add : "))
for i in range (len):
    ele=int(input("Enter the Element : "))
    a.append(ele)
print("Array After changing ",a)