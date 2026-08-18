'''
    Author: Aaramva Acharya
    Program Title: T-Shirt Shop Tracker App
    File Description: This program allows the user to purchase T-shirts, track statistics, and display total sales using functions and input validation.
'''
import time as t

# FUNCTION: show_menu
# Displays the main menu and validates user input
# Returns: 1, 2, or 3

def show_menu():
    print("\n     MAIN MENU     ")
    print("1. Purchase a T-Shirt")
    print("2. Show Statistics")
    print("3. Exit")

    # Asking user for a choice
    choice = int(input("Select a command (1-3): "))

    # Validating input
    while choice not in [1, 2, 3]:
        print("\n *Invalid choice. Please enter 1, 2, or 3.* ")
        choice = int(input("Select a command (1-3): "))

    return choice

# FUNCTION: purchase_t_shirt
# Asks user for style and size, and validates both
# Calculates price, and returns style, size, price

def purchase_t_shirt():

    print("\n     STYLES     ")
    print("1. Basic ($12.99)")
    print("2. Graphic ($16.99)")
    print("3. Tour/Band ($24.99)")

    style = int(input("Select your style (1-3): "))

    # Validating style
    while style not in [1, 2, 3]:
        print("\n *Invalid style. Please choose 1, 2, or 3.* ")
        style = int(input("Select your style (1-3): "))

    # Determining base price
    if style == 1:
        price = 12.99
    elif style == 2:
        price = 16.99
    else:
        price = 24.99

    print("\n     SIZES     ")
    print("1. Small (+$0)")
    print("2. Medium (+$2)")
    print("3. Large (+$4)")

    size = int(input("Select your size (1-3): "))

    # Validating size
    while size not in [1, 2, 3]:
        print("\n*Invalid size. Please choose 1, 2, or 3.*")
        size = int(input("Select your size (1-3): "))

    # Adding extra cost for size
    if size == 2:
        price += 2.00
    elif size == 3:
        price += 4.00

    # Returning all needed values to main()
    return (style, size, price)

# FUNCTION: show_stats
# Displays all statistics and total sales

def show_stats(style_basic, style_graphic, style_band, size_small, size_medium, size_large, total_sales):

    print("\nT-Shirt Style Statistics")
    print(f"Basic: {style_basic}")
    print(f"Graphic: {style_graphic}")
    print(f"Tour/Band: {style_band}")

    print("\nT-Shirt Size Statistics")
    print(f"Small: {size_small}")
    print(f"Medium: {size_medium}")
    print(f"Large: {size_large}")

    print(f"\nTotal Store Sales: ${total_sales:.2f}")


# MAIN FUNCTION
# Controls the entire program

def main():

    # Initializing counters
    style_basic = 0
    style_graphic = 0
    style_band = 0

    size_small = 0
    size_medium = 0
    size_large = 0

    total_sales = 0.0

    # Looping until user chooses Exit
    while True:

        choice = show_menu()  # Getting user's choice

        if choice == 1:
            # User wants to purchase a shirt
            style, size, price = purchase_t_shirt()

            # Updating style counters
            if style == 1:
                style_basic += 1
            elif style == 2:
                style_graphic += 1
            else:
                style_band += 1

            # Updating size counters
            if size == 1:
                size_small += 1
            elif size == 2:
                size_medium += 1
            else:
                size_large += 1

            # Addding to total sales
            total_sales += price

            print(f"\nT-shirt purchased! Price: ${price:.2f}")

        elif choice == 2:
            # Showing statistics
            show_stats(style_basic, style_graphic, style_band, size_small, size_medium, size_large, total_sales)

        else:
            # Exiting program
            print("\nExiting the program...")
            t.sleep(2)
            print("Thank You!")
            exit()
            return

# Starting the program
main()