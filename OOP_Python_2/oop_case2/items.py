from asyncore import read
import csv

class Item:
    pay_rate = 0.8 # the pay rate after 20% discount 
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        
        # assert is statement keyword, to check for match based on input 
        assert price >=0, f" Price {price} is not greater then Zero"
        assert quantity >=0, f" quantity {quantity} is not greater then Zero"
        
        self.__name = name  # cannot access this attribute (private)
        self.__price = price 
        self.quantity = quantity

        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    # this will increment the price 
    # lets say increment by 20% that is increment_value = 0.2
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value



    @property  # property decorator --> here we are stating name is Read-Only Attribute   
    def name(self):
        print('execute everything within this Read-Only Attribute function ')
        return self.__name

    @name.setter  # we still want to set a value even though it is property 
    def name(self, value):
        # here when user provide the value for name it will execute for __name 
        # assign the name value to __name 
        print('execute everything within this settter Attribute function ')
        if len(value) > 10:
            raise Exception(" The name is too long")
        else:
            self.__name = value



    def calculate_total_price(self):
        return self.__price * self.quantity



    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # count out the floats with point zero : 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False



    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}','{self.__price}','{self.quantity}')"


    # this is private method  and can only be accessed within the class 
    def __connect(self, smpt_server):
        pass 

    def __prepare_body(self):
        return f"""
        Hello someone,
        We have {self.name} {self.quantity} times.
        Regards, Kishan
        """

    def __send(self):
        pass

    # here to send email we have to go though lot of processes 
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()





