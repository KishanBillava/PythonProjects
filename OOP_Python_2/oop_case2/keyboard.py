from items import Item



class Keyboard(Item):
    pay_rate = 0.7 # overriding the class attribute at the child class 
    def __init__(self, name: str, price: float, quantity=0):
        # keyworded arguments
        # call to super funcation to have access to all attributes / methods
        super().__init__(name, price, quantity)
