# zip() с циклом for

def pairwise_sum(list1, list2):
    result = []
    for a, b in zip(list1, list2):
            result.append(a + b)
    return result
        
list1 = [1,2,3]
list2 = [4,5,6]
print(pairwise_sum(list1 , list2))