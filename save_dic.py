import pickle

def save(dict,f_path):
    with open(f_path,'wb') as file: #wb -> write binary
        pickle.dump(dict,file)

def load(f_path):
    with open(f_path,'rb') as file:
        return pickle.load(file)

test_dic = {1:'a',2:'b',3:'c'}
save(test_dic,'test_dic.txt')
print(load('test_dic.txt'))