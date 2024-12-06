#Глобальные и локальные переменные

z = 1

def modify():
    z = 5
    print("Значение z: ", z,)

def modify_1():
    global z
    print("Значение z: ", z)
    
modify()
modify_1()
