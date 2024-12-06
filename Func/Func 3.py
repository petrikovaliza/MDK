#19.1

def city_country(city,country):
    full_city_country = f"{city}, {country}"
    return full_city_country.title()

trip = city_country('Тюмень', 'Россия')
print(trip)
trip = city_country('Портленд', 'США')
print(trip)
trip = city_country('Флоренция', 'Италия')
print(trip)

#19.2

def make_album(artist_name,album_title):
    music = {'artist': artist_name, 'album': album_title}
    return music

musician =  make_album('Mylene farmer', 'En concert')
print(musician)
musician =  make_album('Mylene farmer', 'Lautre')
print(musician)
musician =  make_album('Mylene farmer', 'Sans contrefacon')
print(musician)

#19.3

def make_album(artist_name,album_title,number_tracks = None):
    music = {'artist': artist_name, 'album': album_title, 'number_tracks' : None}
    return music

musician =  make_album('Mylene farmer', 'En concert', '6')
print(musician)

#19.4

def make_album(artist_name,album_title):
    music = f"{artist_name},{album_title}"
    return music.title()

while True:
    print("\n")


