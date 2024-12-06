import city_function
from city_function import city_country

city_country('тюмень','россия')

from city_function import city_country as citcou
citcou()

import city_function as city_coun
city_coun.city_country()

from city_function import *
city_function.city_country()