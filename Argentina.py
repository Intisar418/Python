                              ########## calculator made by intisar ##########

# t = True
# while t:
#     try:
#         x= int(input("enter a number: "))
#         y= int(input("enter another number: "))
#         m= input("enter the operator : ")
#         if m =="+":
#             print("the result of addition is =", x+y)
#         elif m == "-":
#             if x<y:
#                 print("the first number can't be smaller than the second number...try again")
#             else:
#                 print("the value of subtraction is =", x-y)
#         elif m == "*":
#             print("the result of multiplication is = :", x*y)
#         elif m == "/":
#             if x<y:
#                 print("the first number can't be smaller than the second number...try again")
#             else:
#                 print("the result of division is =", x/y)
#         else:
#             t = False
#             print("calculator error")
#     except ValueError:
#         print("input can't br string....only enter a number or an operator")


                            ####### Date 3.10.2024 practicing python (chapter2) #######

# jousrif = 'normal badminton player'
# print(jousrif.title())
# shopnoneer = '   i told my father that "we need to build a new pc"        '
# print(shopnoneer.strip())
# messi = 'messi is the real goat'
# print(messi.capitalize())
# print(messi.upper())
# print(f"{jousrif} {messi.upper()}")
# zareef = "one at night zareef was sleeping"
# print(zareef.removeprefix("one"))
# print("3.10.2024 \nKazipara,Dhaka \nrespected vaiya\nHow are you? I hope you're well.\n\t HI")


                            ####### Date 4.10.2024 practicing python (chapter3) #######

# cars = ['rolls royce', 'lamborghini', 'Ferrari', 'Mercedes', 'cadillac', 'Aston Martin', 'Porsche', 'Bugatti', 'Nissan', 'alpha romeo']
# print(cars)
# cars[4]= "Mclaren"
# print(cars)
# cars.append("Tesla")
# print(cars)
# jousrif = f"my first car was a {cars[3].title()}  now i use {cars[0].title()} a few days later i'll buy a {cars[4]}"
# print(jousrif)

                            ####### Date 7.10.2024 practicing python (chapter3)######

# dinner = ['Sowad', 'Kafi', 'Ahnaf']
# for i in dinner:
#     print("\ndear".capitalize(), i, """i have got a job in google as a software engineer.So I have decided to arrange
# a dinner party.You are requested to join in my dinner party.""")
# print("\n")
# print(dinner[2], "can't join the party, so i need to add a new member")
# dinner.remove('Ahnaf')
# dinner.insert(2, "Tawfiq")
# print("\n")
# for i in dinner:
#     print("\ndear".capitalize(), i, """i have got a job in google as a software engineer.So I have decided to arrange
# a dinner party.You are requested to join in my dinner party.""")
# print("\n")
# for i in dinner:
#     print("\n",i, 'I have found a larger dining table. So Iam going to call 3 more guests')
# dinner.insert(2, "Abrar")
# dinner.insert(0, "Radif")
# dinner.append("Tamim")
# print("\n")
# for i in dinner:
#     print("\n dear".capitalize(), i, """i have got a job in google as a software engineer.So I have decided to arrange
# a dinner party.You are requested to join in my dinner party.""")
#
# print("\n")
# for i in range(len(dinner)-1, 1, -1):
#     print(f"{dinner[i]}", "I'm very sorry the party has been cancelled")
#     dinner.pop(i)
#     print(dinner)
                                ###### Date 24.10.2024 practicing python (chapter3)######

# m = ['Brazil', 'Uruguay', 'Portugal', 'France', 'Saudi', 'Argentina', ]
# m.sort()
# print(m)
# for i in range(1,3):
#     print(m[i])
# l=  f"{m[0]} is my favourite team"
# print(l)
# message = f"My favourite team is {m[0]}"
# print(message)
# message = f"My favorite team....{m}"
# print(message)
# del m[1]
# print(m)
# m.pop()
# print(m)
# m.append("brazil")
# print(m)
# print(m[-5])
#
# b = "this teams will play in 2026 world cup "
# for i in range(0,3):
#     print(m[i], "best team" )
#
# b= True
# while b:
#     print(m)
#     b =  False
# result = []
# for i in range(0,11,2):
#     m = (i**2)
#     result.append(m)
# print(result)
# digits = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(min(digits))
# print(max(digits))
# print(sum(digits))
                                        ##### Date:26.10.2024 practicing python #####
#### Making a Calculator (with using sense not memorizing) ####

# l = True
# while l:
#     m = int(input("Enter a Number: "))
#     i = int(input("Enter another NUmber: "))
#     z = input("Enter the Operation: ")
#     if z == '+':
#         print("The Result of Multiplication is = ", m+i)
#     elif z == '-':
#         if m<i:
#             print('The first number can\'t be smaller than the second number')
#         else:
#             print("The Result of Subtraction is = ", m-i)
#     elif z =='*':
#         print("The Result of Multiplication is = ", m*i)
#     elif z == '/':
#         if z<i:
#             print('The first number can\'t be smaller than the second number')
#         else:
#             print("The Result of Multiplication is = ", m/i)
#
#     else:
#         z = int
#         print("CALCULATOR ERROR")
#         l = False
                                    ##### Date 27.10.2024 practicing python  #####

##### before #####
# s = []
# for i in range(0,11):
#     k = i**2
#     s.append(k)
# print(s)
#
#
#
# s = [i**2 for i in range(1,11)]
# print(s)
# football_team = ['Zareef', 'Isam', 'Tawfiq', 'Rafsan', 'Sami', 'Abdullah', ]
# print(football_team[0:5])
# print(" Here are the name of some best players of my team")
# for i in football_team [3:]:
#     print(i, 'vaiya')
                                    ##### Date 29.10.2024 practicing python  #####
# #### list copying ####
# france_football= ['Rodri', 'Vinicius Junior', 'Jude Bellingham']
# ballondior = france_football
# ballondior.append('Lamine Yamal')
# print(france_football)
# print(ballondior)
# #### using tuples ####
# best_of_this_season = ('Rodri', 'Vinicius Junior', 'Jude Bellingham')
# print(best_of_this_season)
# #### exercise 4.10-4.12 ####
# laptops = ['Lenovo', 'Asus', 'Acer', 'Microsoft', 'Apple', 'HP', 'Dell', 'MSI', 'Razer']
# print(f'The first three items in the list are :{laptops[0:3]}')
# print(f'The middle three items in the list are:{laptops[3:6]}')
# print(f'The last three items of my list are:{laptops[6:]}')
#
# vehicles = ['car', 'bike', 'plane']
# vehicles.append('ships')
# #### football team ####
# main_team = ['ovy vaiya',  'zareef', 'ocean', 'hamim', 'osaifi']
# sub_team = ['intisar', 'tanzim', 'naimul']
# full_team = sub_team + main_team
# print(full_team)
# print(main_team)
# print(sub_team)
                              ###### Date:1.11.2024 practicing python for exam ######
# cars= ["tesla", "ford", "chevrolet", "bmw", "audi", "mercedes", "toyota", "honda", "nissan"]
# cars.insert(5,'rolls royce')
# print(cars)
# m = len(cars)
# print(m)
# cars.sort(reverse = True)
# print(cars)
# print(cars)
# for i in cars:
#     print(f'{i} hi')
# for i in cars:
#     if i == 'bmw':
#         print(i.upper())
#     else:
#         print(i.title())cars
#
# #### practicing exercixe 4-13(pg-68) ####
#
# r = ('pizza', 'burger', 'hot dogs', 'tacos', 'nuggets')
# r = ('pizza', 'burger', 'chicken fries', 'sandwiches', 'nuggets')
# for i in r:
#     print(i)

                                ###########  Date:9.11.2024 ###########
# study_tour_champions = 'Madrid'
# if study_tour_champions != 'Barcalona':
#     print('Better Luck Next Time Barca!')
# number_of_players = 11
# if number_of_players!= 12:
#     print('The number of players isn\'t okay')
#
# m = int(input('Enter Your Age: '))
# if m>= 18:
#    print('You Can Vote!')
# else:
#     print("You Can't Vote!")
#
# b = True
# while True:
#     m = int(input("Enter Your Age Number: "))
#     if m < 4:
#         print("Your Admission Fee is $0")
#     elif m < 18:
#         print("Your Admission Fee is $25")
#     else:
#         print("Your Admission Fee is $40")
#
# #food
# foods = ['pizza', 'burger', 'sandwich']
# if 'pizza' in foods:
#     print("Pizza is available in our restaurant")
# if 'burger' in foods:
#     print("Sorry Burger isn't available in our shop. PLease order somthing else")
# if 'sandwich' in foods:
#     print("Sandwich is available in our shop")
# #alien_color 1
# alien_color = 'green'
# if alien_color == 'green':
#     print("+5 points")
# if alien_color != "green":
#
# #alien_colors 2
# alien_color = 'red'
# if alien_color == 'green':
#     print("+5 points")
# if alien_color != "green":
#     print("+10 points")
#
# #alien_colors 3
# alien_color = "yellow"
# if alien_color == "green":
#     print("+5 points")
# elif alien_color == "yellow":
#     print("+10 points")
# elif alien_color == "red":
#     print("+15 points")
#
#
# #stages of life
# m = True
# while m:
#     age = int(input("Enter Your Age: "))
#     if age < 2:
#         print("The person is a baby")
#     elif age in range(2, 5):
#         print("The person is toddler")
#     elif age in range(4, 14):
#         print("The person is a kid")
#     elif age in range(13, 21):
#         print("The person is a teenager")
#     elif age in range(20, 66):
#         print("The person is an adult")
#     else:
#         print("The person is an elder")
#
# #favorite fruit
# favorite_fruits = ['mango', 'strawberry', 'lychee', 'dragon',]
# if 'mango' in favorite_fruits:
#     print("You really like mangoes!")
# if 'strawberry' in favorite_fruits:
#     print("You really like strawberries!")
# if 'lychee' in favorite_fruits:
#     print('You really like lychees!')
# if 'dragon' in favorite_fruits:
#     print("You really like dragon fruit!")

                    ###### Date:12.11.2024 ######

## stages of life ##

# m = True
# while m:
#     age = int(input("Enter Your Age: "))
#     if age < 2:
#         print("The person is a baby")
#     elif age <= 4:
#         print("The person is toddler")
#     elif age <= 13:
#         print("The person is a kid")
#     elif age <= 20:
#         print("The person is a teenager")
#     elif age <= 65:
#         print("The person is an adult")
#     else:
#         print("The person is an elder")

                ###### Date:14.11.2024 of learning python ######

# colors = {'green': 'yellow', 'white': 14}
# print(colors['green'])
# print(colors['white'])
#
# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

                              ###### Date:14.11.2024 of learning python ######
#q6

# x = 90
# y = 80
# if x>y>100:
#     print("the condition is true")
# else:
#     print("the condition is not true")
#
# #q7
#
# flag = True
# if flag == False:
#     print("false")
# elif flag == True:
#     print("true")
# else:
#     print("didn't match")
#
# #q8
# a = "xzy"
# if "z" in a < "x":
#     print("condition met")
# else:
#     print("condition didn't met")
#
# #q9
#
# if not True:
#     print("hi")
# else:
#     print("bye")
#
#
# #q10
# value = 100
# if value == "100":
#     print("not ok")
# elif value == int(100):
#     print("ok")
# else:
#     print("your code has genjam ")
#
# #q11
#
# x = 999999
# for i in range(x):
#     print(x)
#     x -= 10
#
# #q12
# m = [1,2,3,4,5,6]
# for i in m:
#     m.append(i*2)
#     if len(m) == 20:
#         break
# print(m)
#
# #q13
# m = 10
# while m < 100:
#     m -= 10
#     print(m)
#
#
# #q14
#
# items = [0, 1, 2, 3]
# new_items = [item**2 for item in items if item % 2]
# print(new_items)
#
# #q15
# # i tried so hard and got so far but in the end i got an error
#
# #q16
# # we didn't learn
#
# #q17
#
# intisar = 20
# while intisar < 90:
#     intisar += 10
# else:
#     print("zareef")


                                        ########## Date: 1.1.2025 ##########

# favourite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'ruby',
#     'phill' : 'pikachu'
# }
# m = favourite_languages['phill']
# print(f"phill's favourite language is {m}")


# name = {
#     'nickname' : 'jousrif',
#     'first name' : 'zareef',
#     'last name' : 'intisar'
# }
# for k, v in name.items():
#     print(f"\nk:{k}")
#     print(f"v:{v}")


# favourite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'ruby',
#     'phill' : 'pikachu',
# }
# for i in favourite_languages:
#     print(i)

                              ########## Date: 4.1.2025 ##########

#
# favourite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'ruby',
#     'phill' : 'pikachu',
# }
# for i in favourite_languages:
#     print(i)
#
# for name in favourite_languages.keys():
#     print(f"{name.title()}, you are a noob.")

# messi = {'name': 'lionel messi', 'ballon di\'or': 8}
# ronaldo = {'name': 'cristiano ronaldo', 'ballon di\'or': 5}
# neymar = {'name': 'neymar', 'ballon di\'or': 0}
#
#
# players = [messi, ronaldo, neymar]
# for i in players:
#     print(i)
# for player in range(40):
#     print(player)



# user = {
# 'zareef':{
#     'first': 'ayman',
#     'last': 'intisar',
#     'location': 'dhaka',
# },
# 'jousrif': {
#     'first': 'intisar',
#     'last': 'xenon',
#     'location': 'bangladesh',
# }
# }

                    ########## Date: 10.1.2025 ##########


# while True:
#     print("if you say anything to me, i will tell it to you again!")
#     fun = input("tell me some thing: ")
#     print(fun)






