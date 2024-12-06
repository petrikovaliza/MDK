class restaurant():
    
    def __init__(self, restaurant_name, cuisine_type ):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}, тип кухни {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
           
first_restaurant = restaurant('Sashlukov','type_1')
second_restaurant = restaurant('Burger King','type_2')
third_restaurant = restaurant('KFC','type_3')

first_restaurant.open_restaurant()
second_restaurant.open_restaurant()
third_restaurant.open_restaurant()
