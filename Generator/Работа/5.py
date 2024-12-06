people = {'Nightwalker': 22, 'obstul': 16, 'John Cena': 19, 'Diana': 14} 
new_dict = {key : value for key, value in people.items() if value > 18}
print(new_dict)