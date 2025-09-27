def armstrong_number(number):
    digits = str(number)
    sum_of_cubes = 0
    for digit in digits:
        sum_of_cubes += int(digit) ** len(digits)
    
    if sum_of_cubes == number:
        print(f"{number} является числом Армстронга.")
    else:
        print(f"{number} не является числом Армстронга.")

armstrong_number(5)

    