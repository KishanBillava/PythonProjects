from items import Item
from phone import Phone
from keyboard import Keyboard



# Encapsulation 
# restricting the ability to override the values for your objects within your setter
# here we modify the value without accessing the element 

item1 = Item('MyItem', 750)
# item1.price = -900
item1.apply_increment(0.2)

item1.name = "OtherItem"  # setter 
print(item1.name)  # getter 
print(item1.price) 


# Abstraction
# here we show only necessary artibute and hide unnecessary artibute
# item1.__connect() #  user should not have access this, hece convert to private 
item1.send_email()


# Inheritance
# here we reuse the code accros the classes 
# Phone class 
item2 = Phone("Iphone", 1000, 3)
item2.apply_increment(0.2)
print(item2.price) 


# Polymorphism
# it refers to use of a single type entity to represent different types in differnt scenarios 
# two use case of the len function : number of char and lenght of the list 
name = "Kishan"
print(len(name))  # number of char 

some_list = ["some", "name"]
print(len(some_list))  # lenght of the list 

# once single entity that can be used for muliple object 
# here phone does not have  apply_discount  but get it from Item class 
item2 = Phone("Iphone", 1000, 3)
item2.apply_discount()

# +++++++++

item3 = Keyboard('first_key', 1000, 3)
#  allowing Polymorphism and Inheritance together 
item2.apply_discount()  # overriding the class attribute at the child class 
print(item3.price)



# find about abstract classes --> template for a class on how a class should be designed 
# this is implemented in different areas in the whole python programming language



# -------  testing --------------# 

#------Item
# Item.instantiate_from_csv()
# print(Item.all)


# for instance in Item.all:
#    print(instance.name)
# print(Item.is_integer(7.0))


#-------phone
# Inheritance

# phone1 = Phone("Phone10", 500, 5, 1)
# print(phone1.calculate_total_price())
# phone2 = Phone("Phone20", 700, 5, 1)

# print(Item.all)
# print(Phone.all)

# for instance in Phone.all:
#     print(instance.name)



# -------- main 
# Item.instantiate_from_csv()
# print(Item.all)



#item2 = Item("Iphone2", 500, 2)

# setting an Attribute
# item2.name = "NotPhone210"

# getting an Attribute
# print(item2.name)


# encapsulation -- restrict direct access 
# 
#item2.apply_increment(0.2)

#print(item2.price)


# Abstraction -- hide info from the user 

#item2.send_email()

#item2.__connect()

# Inheritance 
#item3 = Phone("Iphone", 100, 3)

#item3.send_email()

# polymorphism 
# two use case of the len function
#name = "Kishan"
#print(len(name))

#some_list = ["some", "name"]
#print(len(some_list))





# -------- testing end ------------#