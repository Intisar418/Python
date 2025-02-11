                                #### All programs of chapter 6 ####
# #pg 99
# #exercise 6-1
person = {
    'first_name': input("Enter your first name: "),
    'last_name': input("Enter your last name: "),
    'age': int(input("Enter your age: ")),
    'city': input("Enter the name of your city: "),
}
print("\n\n")
print(f"First name: {person['first_name']}")
print(f"Last name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']} ")


# #exercise 6-2
favourite_number = {'Messi_1': 10,
                    'Messi_2': 19,
                    'Messi_3': 18,
                    'Messi_4': 30,
                    'Penaldo': 7
}

for name, number in favourite_number.items():
    print(f"Favourite number of {name} is {number}")

# pg 105
# #exercise 6-5
rivers = {'Nile': 'Egypt', 'Amazon RIver': 'Brazil',
          'Mississippi River': 'USA'}
for river, country in rivers.items():
    print(f"The {river} runs through {country}")








