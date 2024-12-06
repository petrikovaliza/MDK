#16.2

prompt = "\nВведите свой возраст: "
prompt += "\n(Введите '0' для завершения программы)"
while True:
    age = int(input(prompt))
    
    if age == 0:
        break
    elif 0 <= age <= 3:
        print("Билет бесплатный")
    elif 3 <= age <= 12:
        print("Билет стоит 10$")
    elif age > 12:
        print("Билет стоит 15$")