class DataBaseError(Exception):
    
    def __init__(self, code, message):
        self.code = code
        self.message = message
        
    def __str__(self):
        return f'{self.code}: {self.message}'
   
class ConnectToDataBase():
    
    def __init__(self, id_connect):
        if id_connect == 0:
            self.id_connect = id_connect
        else:
            raise DataBaseError('DataBaseError', 'Не удалось подключиться к базе данных')
           
    def print_connect(self):
        print(f"Подключение успешно")
           
try:
    connect = ConnectToDataBase(0)
    connect.print_connect()
    connect = ConnectToDataBase(1)
    connect.print_connect()
    
except DataBaseError as e:
    print(e)
            