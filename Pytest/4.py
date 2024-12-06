def check_permission(user_permissions):
    def requires_permission(permission):
        def decorator(input_func):
            def wrapper(*args, **kwargs):
                if permission in user_permissions:
                    return input_func(*args, **kwargs)              
                return "Error"
            return wrapper
        return decorator
    return requires_permission
                
user_permissions = ["admin", "user1", "user2", "user3", "user4"]         
       
@check_permission(user_permissions)("admin")
def start_func():
    return "Вам пришло сообщение!"
    
print(start_func())
    