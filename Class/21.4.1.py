class restaurant():
    
    def __init__(self, restaurant_name, cuisine_type,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"name: {self.restaurant_name},type: {self.cuisine_type} ")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
        
    def set_number_served(self, number_served):
        self.hz_served = number_served
        print(f'Обслуженные гости: {self.hz_served}')
        
           
restaurant = restaurant('sashlukov','first',)
restaurant.describe_restaurant()

restaurant.set_number_served(58)




