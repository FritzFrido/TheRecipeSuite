# RECIPE SELECTION

def main():
    
    from time import sleep

    # Welcome statement to user
    sleep(1.0)
    print("")
    print("Welcome! This is the desert suite. We offer the following recipes:")
    print("")
    print("––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
    print("")

    # Recipe statements
    
    sleep(1.0)
    print("Banana Bread")
    sleep(0.5)
    print("")
    print("Subway Cookies")
    sleep(0.5)
    print("")
    print("Iced Vanilla Cocoa")
    print("")
    print("––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
    print("")
    sleep(1.0)


    # Get input from user
    select = input("Please enter the recipe you’d like to try: ")

    # Process the user input
    match select:
        case "Banana Bread":
            BanBr()
        # case "Subway Cookies":
            # SubCoo()
        # case "Iced Vanilla Cocoa":
            # IcedVanCo()
        case _:
            print("I’m sorry - seems like we dont have your recipe in stock! Please choose again .. ")



# DEFINE the functions for each individual recipe incl portion calculation
def BanBr():
    from time import sleep
    sleep(1.0)
    print("")
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
    print("")
    print(f"For {e1} friends, you need the following ingrediences: ")
    print("")
    print("")
    sleep(1.0)
    print((str(bananas) + " ripe bananas"))
    sleep(0.5)
    print(str(map_syrup) + " mililiters of maple syrup")
    sleep(0.5)
    print(str(vegan_butter) + " grams of vegan butter")
    sleep(0.5)
    print(str(plant_milk) + " mililiters of plant milk")
    sleep(0.5)
    print(str(apple_cider_vinegar)+ " mililiters of apple cider vinegar")
    sleep(0.5)
    print(str(oats) + " grams of oats")
    sleep(0.5)
    print(str(whole_grain_flour) + " grams of whole grain flour")
    sleep(0.5)
    print(str(wallnut) + " grams of crushed wallnuts")
    sleep(0.5)
    print(str(cashew) +  " grams of curshed cashews")
    sleep(0.5)
    print(str(baking_powder) + " grams of baking powder")
    sleep(0.5)
    print(str(salt) + " pinches of salt")
    sleep(0.5)
    print(str(cinnamon) + " grams of cinnamon")
    sleep(0.5)
    print(str(choco) + " grams of chocolat chips")
    sleep(0.5)
    print("")
    print("")
    print("And now for the instructions")
    sleep(1.0)
    print("")
    print("––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
    print("")
    print("1. Preheat oven to 180 degree celsius")
    print("")
    sleep(0.5)
    print("2. Grease a 20 centimeter loaf pan with a bit of oil then line with parchment paper")
    print("")
    sleep(0.5)
    print("3. Mash the bananas in a large bowl until smooth and mix with all other wet ingredients")
    print("")
    sleep(0.5)
    print("4. Add the crushed nuts and the other dry ingredients to the wet mixture and stir until just combined")
    print("")
    sleep(0.5)
    print("5. Put the batter into the loaf pan and spread evenly")
    print("")
    sleep(0.5)
    print("6. Bake for 30 to 35 minutes")
    print("")
    sleep(0.5)
    print("7. Conduct the fork test: If no batter is sticking to the fork your banana bread is ready to take out and cool for a bit")
    sleep(1.0)
    print("")
    print("")
    print(" * * * Enjoy your banana bread! * * *")
    print("")
    print("")

# def SubCoo():
    # from time import sleep

# def IcedVanCo():
   # from time import sleep




main()
