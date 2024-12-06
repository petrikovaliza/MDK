class restaurant():
    
    def __init__(self, restaurant_name, cuisine_type ):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
           
main_restaurant = restaurant('sashlukov','first')

main_restaurant.describe_restaurant()
main_restaurant.open_restaurant()
