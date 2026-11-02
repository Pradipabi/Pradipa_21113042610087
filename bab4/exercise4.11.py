pizzas = ["Pepperoni", "Margherita", "Hawaiian"]

friend_pizzas = pizzas[:]

pizzas.append("Meat Lovers")
friend_pizzas.append("Cheese Pizza")

print("Pizza favorit saya:")

for pizza in pizzas:
    print(pizza)

print("\nPizza favorit teman saya:")

for pizza in friend_pizzas:
    print(pizza)