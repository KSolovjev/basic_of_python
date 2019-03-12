#task1
lst=[1, 2, 3, 4, 5]
res=[i**2 for i in lst]
print(res)

#task2
lst1=["apple", "bananas", "kiwi", "watermelon"]
lst2=["melon", "pineapple", "orange"]
res=lst1 + lst2
#res=[i for i in lst1,lst2]
print(res)

#task3
lst3=[-5,3,12,9,-3,16,25]
res1=[i for i in lst3 if i%3==0]
res2=[i for i in lst3 if i>=0]
res3=[i for i in lst3 if not i%4==0]
print(res1)
print(res2)
print(res3)
