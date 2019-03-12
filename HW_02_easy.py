#task1
print("Task1:")
lst1=["apple", "bananas", "kiwi", "watermelon","melon", "pineapple", "orange"]
n=0
for i in lst1:
    n+=1
    print('{}. {}'.format(n,i))

#task2
print("Task2:")
lst2=["apple", "kiwi","orange"]
n=0
for i in lst1:
    if i == lst2[0]:
        lst1.pop(n)
    elif i == lst2[1]:
        lst1.pop(n)
    elif i == lst2[2]:
        lst1.pop(n)
    n+=1
print(lst1)

#task3
print("Task3:")
lst3=[10,5,2,8,1,9,6,7,4,3]
new_lst=[]
for i in lst3:
    if i%2==0:
        n=i/4.0
    else:
        n=i*2
    new_lst.append(n)
print(new_lst)