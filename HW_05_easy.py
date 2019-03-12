import os
#task1

def create_dir(name, Q_dir):
    for i in range(1,Q_dir+1):
        name_dir=name+str(i)
        os.mkdir(name_dir)
    return i
def del_dir(name,Q_dir):
    for i in range(1,Q_dir+1):
        name_dir=name+str(i)
        os.rmdir(name_dir)
    return i

def list_dir():
    return os.listdir(os.getcwd())

#print(str(create_dir('dir',3))+' dirctories were created')
#print(str(del_dir('dir',3))+' dirctories were deleted')
print(list_dir())