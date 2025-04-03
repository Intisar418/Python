                                                #### All programs from chapter 8 ####
def zareef():
    print("Hello World!")
zareef()

def username(hi):
    print(f"Hello, {hi.title()}")
username('zareef')

#pg 131
#exercise 8-1
def display_message(lm10):
    print(f"{lm10}")
display_message('Hello everyone I\'m learning functions')

#exercise 8-2
def favourite_book(title):
    print(f"One of my favourite book is {title}")
favourite_book('Alice in Wonderland')

#not available in exercise
def my_pet(animal_type,animal_name):
    print(f"I have a {animal_type} "
          f"\nMy {animal_type}'s name is {animal_name}")
my_pet('Cat','Murgi')

def animal(x, y):
    print(f"I have a {x} \nHis name is {y}")
animal(x="Dog",y="Hasina")

pg 137

exercise 8-3
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


                    #### Returning a Simple Value #####

def returning_value(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

if __name__ == '__main__':
    student = returning_value('zareef', 'intisar')
    print(student)

                #### Making an Argument Optional #####

def my_name(first, last, middle=""):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

if __name__ == '__main__':
    student = my_name('zareef', 'xenon', 'intisar')
    print(student)
    student = my_name('zareef', 'intisar')
    print(student)

            #### Returning a Dictionary #####

def return_dictionary(first_name, last_name):
    dct = {'first': first_name, 'last':last_name}
    return dct

if __name__ == '__main__':
    player = return_dictionary('Lionel', 'Messi')
    print(player)

            #### Function with a while Loop #####

def my_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

if __name__ == '__main__':
    while True:
        print("\nPlease tell me your name: ")
        f_name = input("Enter you first name: ")
        l_name = input("Enter your last name: ")

        name = my_name(f_name, l_name)

        print(f"\nHello, {name}!")
        loop = input("Do you want to continue? (yes/no)")
        if loop == 'no':
            break

            #### Passing a List #####

def greet_user(names):
    for i in names:
        print(f"Hello, {i.title()}!")


if __name__ == '__main__':
    nicknames = ['zareef', 'intisar', 'xenon']
    greet_user(nicknames)

            #### Modifying a list in Function #####

current_designs = ['Phone case', 'Kuromi doll', 'Neko chan']
completed_design = []
while current_designs:
    printing_designs = current_designs.pop()
    print(f"Printing designs: {printing_designs}")
    completed_design.append(printing_designs)
print(f"\nThis designs have been printed: ")
for i in completed_design:
    print(i)

