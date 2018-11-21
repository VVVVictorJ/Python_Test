class restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served=0
    def describle_restaurant(self):
        print("这家餐厅叫" + self.restaurant_name + "\n口味是" + self.cuisine_type)
    def open_restaurant(self):
        print("\n目前正在营业")
    def set_number_served(self,couldserved):
        if couldserved>=self.number_served:
            self.number_served=couldserved
        else:
            print("error data")
    def increment_number_serverd(self,add):
        self.number_served +=add
    def read_number(self):
        print("today we accept "+str(self.number_served))
my_restaurant = restaurant('君豪', '广东风味')
print(my_restaurant.cuisine_type + " " + my_restaurant.restaurant_name)
print(my_restaurant.describle_restaurant())
print(my_restaurant.open_restaurant())

first_restaurant = restaurant('KFC', 'fastfood')
second_restaurant = restaurant('白天鹅', '广式酒家')
print(first_restaurant.describle_restaurant())
print(second_restaurant.describle_restaurant())

new_restaurant=restaurant('鹌鹑村','十二小风味')
new_restaurant.set_number_served(10)
new_restaurant.read_number()
new_restaurant.increment_number_serverd(5)
new_restaurant.read_number()
new_restaurant.set_number_served(-1)