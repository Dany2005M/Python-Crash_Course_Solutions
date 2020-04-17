class Restaurant:



    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant_name and cuisine_type attributes.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        '''Method that describes the restaurant.'''
        print(f'The restaurant is called {self.restaurant_name.title()} and it offers {self.cuisine_type} cuisine.')
        

    def open_restaurant(self):
        '''Simulate the opening of the restaurant.'''
        print(f'{self.restaurant_name} is OPEN!')


restaurant = Restaurant('Franklin Barbeque', 'barbeque')
restaurant_1 = Restaurant('Pizza Hut', 'pizza')
restaurant_2 = Restaurant('KFC', 'fast food')

restaurant.describe_restaurant()
print()
restaurant_1.describe_restaurant()
print()
restaurant_2.describe_restaurant()


