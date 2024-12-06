def get_animal_sound(animal):
    # animal_sounds = {
    #     'кот':'мяу',
    #     'собака':'гав'
    # }
    
    # match animal:
    #     case a if animal in animal_sounds:
    #         return animal_sounds[animal]
    #     case _:
    #         return 'Неизвестное животное'
            
    match animal:
        case animal if animal in {'кот' : 'мяу'}:
            return 'мяу'
        case animal if animal in {'собака': 'гав'}:
            return 'гав'
        case animal if animal in {'корова':'му'}: 
            return 'му'
        case  _ : print('Неизвестное животное')
            
print(get_animal_sound('кот'))
print(get_animal_sound('собака'))
print(get_animal_sound('корова'))
