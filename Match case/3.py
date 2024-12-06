def day_of_week(number):
    match number:
        case 1:
            return 'Понедельник'
        case 2:
            return 'Вторник'
        case 3:
            return 'Среда'
        case 4:
            return 'Четверг'
        case 5:
            return 'Пятница'
        case 6:
            return 'Суббота'
        case 7:
            return 'Воскресенье'
        
        
print(day_of_week(5))
print(day_of_week(6))
print(day_of_week(8))
print(day_of_week(1))