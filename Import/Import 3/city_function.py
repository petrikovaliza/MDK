def city_country(city,country):
    full_city_country = f"{city}, {country}"
    return full_city_country.title()

trip = city_country('Тюмень', 'Россия')
print(trip)
trip = city_country('Портленд', 'США')
print(trip)
trip = city_country('Флоренция', 'Италия')
print(trip)