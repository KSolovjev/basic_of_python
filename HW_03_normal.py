import os

name=['Vasiliy', 'Petr', 'Roman', 'Ivan']
salary=[550000, 300000, 250000, 400000]
res=dict(zip(name, salary))
#path = os.path.join('HW_03','salary.txt')
#file=open(path, 'w', encoding='UTF-8')
file = open('salary.txt', 'w')
for k,v in res.items():
    if v <500000:
        file.write('{} - {}\n'.format(k,v))
with open('salary.txt','r') as f:
    for line in f:
        a=line.split('-')
        print(a)
f=open('salary.txt','r')
print(f.readlines())
