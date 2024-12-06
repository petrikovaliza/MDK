

import threading
import os
import time
from concurrent.futures import ThreadPoolExecutor

def read_file(path):
    with open(path, 'r') as file:
        contents = file.read()
        print(contents)

# Список путей к файлам
paths = 'file1.txt', 'file2.txt', 'file3.txt'

# Создание пула потоков
pool = ThreadPoolExecutor(max_workers=len(paths))

# Запуск задач в пуле потоков
for path in paths:
    pool.submit(read_file, path)

# Ожидание завершения всех задач в пуле
pool.shutdown(wait=True)
