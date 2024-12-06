class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"In restaurant {self.restaurant_name} {self.cuisine_type} cuisine")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")



class IceCreamStand(Restaurant):
    
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanila', 'cherry']
        
    def flavors_type(self):
        print(f'Restaurant have: ')
        for flavor in self.flavors:
            print(f'{flavor}')
        
ice_restaurant = IceCreamStand('Baskin robins', 'russian')
ice_restaurant.describe_restaurant()
ice_restaurant.open_restaurant()
ice_restaurant.flavors_type()

    