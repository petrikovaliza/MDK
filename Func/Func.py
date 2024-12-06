#21.1

def make_sandwich(*components):
    print(components)
    
make_sandwich('cheese')
make_sandwich('sausage','avocado','eggs')
make_sandwich('mushrooms','onion')

#21.2

def build_profile(name, surname, **user_info):
    user_info['first_name'] = name
    user_info['surname'] = name
    return user_info

user_profile = build_profile(
'Liza','Petrikova',
location = 'Tyumen',
speciality = 'Programmer')

print(user_profile)

#21.3

def make_car(manufacturer, model_name, **car_info):
    car_info['Manufacturer'] = manufacturer
    car_info['Model'] = model_name
    return car_info

car_profile = make_car(
'Trulala', '45G',
colour = 'White',
tow_package = True)

print(car_profile)