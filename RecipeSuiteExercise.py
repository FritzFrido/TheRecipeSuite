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
    e1 = input("Good choice! How many frieds would you like to serve with your Banabread? ")
    sleep(0.5)
    print(f"For {e1} friends, you need the following ingrediences: ")
    sleep(0.5)
    print((e1 * 1) + "ripe bananas")
    print((e1 * 60) + "mililiters of maple syrup")



def SubCoo:
    from time import sleep

def IcedVanCo:
    from time import sleep




main()
