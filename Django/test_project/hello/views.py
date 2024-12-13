from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseForbidden, HttpResponseBadRequest

def index(request, id):
    people = ["Tom", "Bob", "Sam"]
    #если пользователь найден, возвращаем его
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    # если нет, то возвращаем ошибку 404
    else:
        return HttpResponseNotFound("Not Found")
    
def access(request, age):
    # если возраст НЕ входит в диапозон 1-110, посылаем ошибку 404
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    # если возвраст больше 17, то доступ разрешен
    if (age > 17):
        return HttpResponse("Доступ разрешен")
    # если нет, то возвращаем ошибку 403
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")

