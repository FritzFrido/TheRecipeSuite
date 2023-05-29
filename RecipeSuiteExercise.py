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
def BanBr:
    sleep(1.0)
    eatersB = input("Good choice! How many frieds would you like to serve with your Banabread? ")


def SubCoo:
    x

def IcedVanCo:
    x




main()
