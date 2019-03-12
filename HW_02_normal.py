import math
import random
import datetime
#task1
lst1=[-10,5,2,8,1,9,6,7,4,3]
new_lst1=[]
#print(type(lst1[0]))
for i in lst1:
    if i >= 0:
        #n=math.sqrt(i)
        n=pow(i, .5)
        if n%1 == 0:
            new_lst1.append(int(n))
print(new_lst1)

#task2
print(datetime.date.today().strftime("%d/%m/%Y"))

#task3
new_lst3=[]
i=10
while len(new_lst3)<i:
    new_lst3.append(random.randint(-100,100))
print(new_lst3)

#task4
lst4=[9,3,2,8,1,9,6,7,1,3]
print(set(lst4))