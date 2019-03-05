#task1
def ind_data(name, age, city):
    a=str('{}, {} years old, lives in city {}'.format (name, age, city))
    return a
print('Task 1')
print(ind_data('Tom', 20, 'Moscow'))

#task2
data=[]
x=data.append(input('Enter 3 comma separeted numbers:'))
result = list(map(max,data))
print('Task 2')
print(result)

#task3
def strings(*args):
    return max(args, key=len)

print('Task 3')
print(strings('hi','hello','hello everybody','hello everyone'))
