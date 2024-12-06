def unzip_lists(num_char_zipped):
    return list(zip(*num_char_zipped))

data = [('a', 1), ('b', 2), ('c', 3)]
num_list,char_list = unzip_lists(data)
print(num_list)
print(char_list)