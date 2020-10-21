water = 400
milk = 540
coffeebeans = 120
disposablecups = 9
money = 550


def printAll():
    print("The coffee machine has:")
    print(water, " of water ")
    print(milk, " of milk ")
    print(coffeebeans, " of coffeebeans ")
    print(disposablecups, " of disposablecups ")
    print(money, " of money ")


printAll()

while True:
    s = ''
    while not(s in ["buy", "fill", "take"]):
        s = input("Write action (buy, fill, take):\n> ")

    if s == 'buy':
        m = 0
        while not(m in ["1", "2", "3"]):
            m = input(
                "What do you want to buy? 1.espresso 2.latte 3.cappuccino:\n> ")
        if m == '1':
            water -= 250
            milk -= 0
            coffeebeans -= 16
            disposablecups -= 1
            money += 4

        elif m == '2':
            water -= 350
            milk -= 75
            coffeebeans -= 20
            disposablecups -= 1
            money += 7

        elif m == '3':
            water -= 200
            milk -= 100
            coffeebeans -= 12
            disposablecups -= 1
            money += 6
        printAll()

    if s == 'fill':
        water += int(input("Write how many ml of water do you want to add:\n> "))
        milk += int(input("Write how many ml of milk do you want to add:\n> "))
        coffeebeans += int(input("Write how many grams of coffee beans do you want to add:\n> "))
        disposablecups += int(input("Write how many disposable cups of coffee do you want to add:\n> "))
        printAll()

    if s == 'take':
        print("I gave you $", money)
        money = 0
        printAll()

    i = ' '
    while not(i in ["1", "2"]):
        i = input("1.exit 2.return:\n> ")
    if i == '1':
        break
