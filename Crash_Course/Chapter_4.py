                                            #### All programs from chapter 4 ####
# #pg 56
# exercise 4-1
pizza = ["BBQ Chicken Pizza", "Four Cheese Pizza", "Hawaiian Pizza"]
for p in pizza:
    print(p)
for m in pizza:
    print(f"I like {m} ")
print("""Pizza is my favourite food. Pizaa isn't good for health. That's why I
don't eat pizza too much. My favourite pizza types are given below""")
for i in pizza:
    print(i)

#exercise 4-2
animals = ['Dog', 'Cat', 'Bird']
for k in animals:
    print(k)
for a in animals:
    print(f"A {a} is a very good animal.")

#pg 60
#exercise 4-3
for i in range(1, 21):
    print(i)

# #exercise 4-4
m = list(range(1, 1000001))
for i in m:
    print(i)

# #exercise 4-5
hi = list(range(1, 1000001))
print(min(hi))
print(max(hi))
print(sum(hi))

# #exercise 4-6
m = list(range(1, 21, 2))
for i in m:
    print(i)

#exercise 4-7
k = list(range(3, 31, 3))
for i in k:
    print(i)

#exercise 4-8
c = list(range(1, 11, 1))
z = []
for i in c:
    k = i**2
    z.append(k)
print(z)

#pg 65
# #exercise 4-10
cars = ['Tesla', 'Ford', 'BMW', 'Audi', 'Mercedes', 'Bentley', 'Aston Martin', 'Cadillac', 'Rolls-Royce']
print("The first three items in my list are:")
for i in cars[0:3]:
    print(f"{i}")
print("Three items from the middle of my list are:")
for z in cars[3:6]:
    print(z)
print("The last three items in my list are:")
for m in cars[6:]:
    print(m)

# #exercise 4-11
pizza = ["BBQ Chicken Pizza", "Four Cheese Pizza", "Hawaiian Pizza"]
friend_pizzas = pizza[:]
pizza.append('Cheese Pizza')
friend_pizzas.append('Italian pizza')
print("My favourite pizzas are:")
for i in pizza:
    print(f"\t {i}")
print("My friend's favourite pizzas are:")
for m in pizza:
    print(f"\t {m}")

#pg 68
# #exercise 4-13
t = ('Burger', 'Pizza', 'Shawarma', 'Sandwich', 'Chicken fry')
for z in t:
    print(z)
t = ('Chicken nuggets', 'Pizza', 'Shawarma', 'Sandwich', 'Mozzarella Sticks')
for m in t:
    print(m)


