#                                                 #### All programs from chapter 8 ####
# def zareef():
#     print("Hello World!")
# zareef()
#
# def username(hi):
#     print(f"Hello, {hi.title()}")
# username('zareef')
#
# #pg 131
# #exercise 8-1
# def display_message(lm10):
#     print(f"{lm10}")
# display_message('Hello everyone I\'m learning functions')
#
# #exercise 8-2
# def favourite_book(title):
#     print(f"One of my favourite book is {title}")
# favourite_book('Alice in Wonderland')
#
# #not available in exercise
# def my_pet(animal_type,animal_name):
#     print(f"I have a {animal_type} "
#           f"\nMy {animal_type}'s name is {animal_name}")
# my_pet('Cat','Murgi')
#
# def animal(x, y):
#     print(f"I have a {x} \nHis name is {y}")
# animal(x="Dog",y="Hasina")

#pg 137
#exercise 8-3
def make_shirt(size, message):
    print(f"The size of the shirt is {size} and the message on it is {message}")
make_shirt(size='L', message='print("Hello World!")')

#exercise 8-4
def make_shirt(size, message):
    print(f"The size of the shirt is {size} and the message on it is {message}")
make_shirt('XL', 'I love python')

#exerise 8-5
def describe_city(x, y="Bangladesh"):
    print(f"{x} is in {y}")
describe_city('Dhaka')
describe_city('Sylhet')
describe_city('Japan', 'Tokyo')

