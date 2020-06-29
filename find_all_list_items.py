example = [[[1,2,3],2,[1,3]],[1,2,3]]

def find_element(given_list,item):
    indexes = []
    for i in range(len(given_list)):
        if given_list[i] == item:
            indexes.append([i])
            #indexes.append(i)
        elif isinstance(given_list[i],list):
            for j in find_element(given_list[i],item):
                indexes.append([i]+j)
    return indexes
print(find_element(example,2))
