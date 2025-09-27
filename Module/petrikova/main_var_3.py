from paket import module_1, module_2
import importlib
importlib.reload(module_1,module_2)

print(f'Среднее авриметическое чисел 5 и 9: {module_1.sa(5,9)}')
print(f'a * sa(a, 4) + sa(a+b, 1) при a = 4, b = 14: {module_1.fun(4,14)}')

print(f'Все ли буквы в строке нижнего регистра: {module_2.st("бла бла бла")}')
print(f'Все ли буквы в строке нижнего регистра: {module_2.st("Кочерга")}')