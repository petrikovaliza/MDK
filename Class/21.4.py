class restaurant():
    
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print(f"name: {self.restaurant_name},type: {self.cuisine_type}, served: {self.number_served} ")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
           
restaurant = restaurant('sashlukov','first', '5')

restaurant.describe_restaurant()
restaurant.open_restaurant()