import restaurant
class IceCreamStand(restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
    def IceCreamList(self):
        flavor=['柠檬奶油味','香草味','抹茶味','五羊味']
my_IceCreamStore=IceCreamStand('帝龙冰厂','粤滋味')
# my_IceCreamStore.IceCreamList()
