#18.1

def favorite_book(title):
    print(f'One of my favorite books is {title.title()}')
    
favorite_book('Alice in Wonderland')

#18.2

def make_shirt(size=input('Введите размер: '),text=input('Введите текст для принта: ')):
    print('Размер:',size,'текст:',text)

make_shirt()
# size = input('ВВедите размер футболки:')
# text = input('Введите текст для футболки:')

make_shirt(size='48', text='111111')
make_shirt(text='111111', size='48')


#18.3

def make_shirt(size,text):
    print('Размер:',size,'текст:',text)

make_shirt('L','I love Python')

#18.4

def describe_city(city = input('Введите город: '), country = 'Россия'):
    print(city, 'находится в стране', country)
    
describe_city()
describe_city(city = 'Лос-Анджелес', country = 'США')

#18.5

def user(car = input("Какую машину вы хотели бы взять напрокат? ")):
    print("Попробую найти для вас", car)

user()