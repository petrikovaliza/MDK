#14.1

people_0 = {'name':'Лиза','age':'24','city':'Тюмень'}
people_2 = {'name':'Света','age':'43','city':'Москва'}
people_3 = {'name':'Катя','age':'32','city':'Челябинск'}

peoples = [people_0, people_2, people_3]

for people in peoples:
    print(f"{people['name']}, {people['age']} года, живет в городе {people['city']}")
    
#14.2

numbers = {
'Катя': [5,3],
'Настя': [9,28],
'Света': [47,90],
'Надежда': [29,1],
'Любовь': [101,101]}

for name, value in numbers.items():
    print(f"{name}")
    for people_numbers in value:
        print(people_numbers)
    
  
# for value in numbers.values():
#     print(f"{name}, её любимое число: {numbers[value]}")
    
#14.3

cities = {
    'Тюмень':{
        'country':'Россия',
        'population':'861 100 человек',
        'fact':'"Это первый русский город в Сибири'
    },

    'Флоренция':{
        'country':'Италия',
        'population':'360 930 человек',
        'fact':'"Этот город был воссоздан в игре Assasing Creed'
    },    
    'Портленд':{
        'country':'США',
        'population':'652 503 человек',
        'fact':'"Здесь снимались Сумерки'
    }
}
for city, city_info in cities.items():
    print(city)
    print(f"\tСтрана - {city_info['country']}")
    print(f"\tНаселение - {city_info['population']}")
    print(f"\tФакт - {city_info['fact']}\n")