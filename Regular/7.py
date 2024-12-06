import re

text = """
For example, suppose the temperature is 80 degrees Fahrenheit and you want to know what the figure would be in Celsius. Use the above three steps:

80 F - 32 = 48
5 x 48 = 240
240 / 9 = 26.7 C

So the temperature in Celsius is 26,7 C
"""

numbers = re.findall(r"[-+]?\d*\.?\,?\d+", text)
print(numbers)

lst = []
for i in numbers:
    lst.append(float(i.replace(',', '.'))) 

print(lst)