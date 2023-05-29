# RECIPE SELECTION

def main():
    
    from time import sleep

    # Welcome statement to user
    sleep(2.0)
    print("Welcome! This is the desert suite. We offer the following recipes:")

    # Recipe statements
    sleep(1.0)
        print("Banana Bread")
    sleep(0.5)
        print("Subway Cookies")
    sleep(0.5)
        print("Iced Vanilla Cocoa")

    # Get input from user
    select = input("Please type the recipe you’d like to try:")

    # Process the user input
    match select:
        case "Banana Bread"
            Banbr()
        case "Subway Cookies"
            SubCoo()
        case "Iced Vanilla Cocoa"
            IcedVanCo()
        case _:
            print("I’m sorry - seems like we dont have your recipe in stock! Please choose again .. ")



# DEFINE the functions for each individual recipe incl portion calculation
def BanBr(e1):
    from time import sleep
    sleep(1.0)
    e1 = int(input("Good choice! How many frieds would you like to serve with your Banabread? "))

    # Calculations of Ingredient Amounts
    bananas = 1 * e1
    map_syrup = 60 * e1
    vegan_butter = 40 * e1
    plant_milk = 50 * e1
    apple_cider_vinegar = 40 *e1
    oats = 20 * e1
    whole_grain_flour = 40 * e1
    wallnut = 20 * e1
    cashew = 20 * e1
    baking_powder = 2 * e1
    salt = 1 * e1
    cinnamon = 1 * e1
    choco = 10 * e1



    sleep(0.5)
    print(f"For {e1} friends, you need the following ingrediences: ")
    sleep(1.0)
    print((str(bananas) + " ripe bananas"))
    sleep(0.5)
    print((map_syrup) + " mililiters of maple syrup")
    sleep(0.5)
    pring((vegan_butter) + " grans of vegan butter")



def SubCoo():
    from time import sleep

def IcedVanCo():
    from time import sleep




main()
