import re

text = """
Macbook Pro в мои мечтах стоит 500$.
А микрофон Blue Yeti 10999р.
Но лучше, конечно, использовать евро.
1€ равен 83р. или чуть больше 1$.
"""

prices = re.findall(r"(\d+)\s*([€$р\.])", text)
print(prices)

for i, (price, currency) in enumerate(prices):
    if currency == "$":
        prices[i] = (str(int(price) * 80), "р.")

print(prices)