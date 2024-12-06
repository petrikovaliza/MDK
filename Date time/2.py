import time

my_local_time = time.localtime()
my_time =  time.strftime('%A %m %B %Y %X', my_local_time)
my_time_2 = time.strftime("%d.%m.%Y", my_local_time)
print(my_time)
print(my_time_2)
