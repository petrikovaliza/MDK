from django.shortcuts import render

def index(request):
    return render(request, "index.html", context={"body": "<h1>Hello World</h1>"})







# def about(request):
#     return render(request, "about.html")

# def contact(request):
#     return render(request, "contact.html")


# # установка куки
# def set(request):
#     # получаем из строки запроса имя польззоавтеля
#     username = request.GET.get("username", "Undefined")
#     # Создаем объект ответа
#     response = HttpResponse(f"Hello {username}")
#     # передаем его в куки
#     response.set_cookie("username", username)
#     return response


# # получение куки
# def get(request):
#     #получаем куки с ключом username
#     username = request.COOKIES["username"]
#     return HttpResponse(f"Hello {username}")

# class Person:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# class PersonEncoder(DjangoJSONEncoder):
    
#     def default(self,obj):
#         if isinstance(obj, Person):
#             return {"name": obj.name, "age": obj.age}
#         # return obj.__dict__
#         return super().default(obj)
        













# def index(request, id):
#     people = ["Tom", "Bob", "Sam"]
#     #если пользователь найден, возвращаем его
#     if id in range(0, len(people)):
#         return HttpResponse(people[id])
#     # если нет, то возвращаем ошибку 404
#     else:
#         return HttpResponseNotFound("Not Found")
    
# def access(request, age):
#     # если возраст НЕ входит в диапозон 1-110, посылаем ошибку 404
#     if age not in range(1, 111):
#         return HttpResponseBadRequest("Некорректные данные")
#     # если возвраст больше 17, то доступ разрешен
#     if (age > 17):
#         return HttpResponse("Доступ разрешен")
#     # если нет, то возвращаем ошибку 403
#     else:
#         return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")

