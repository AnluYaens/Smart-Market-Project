#---------------------------------------------(Add_Products module)------------------------------------------------------------
#----So here because of the change of the structure by dividing the code in modules we change some little things like----------
#-----------------------(1. not having some others functions that we need so we call them from the others modules-------------- 

from get_and_checks_2_4 import get_and_check_numeric, get_and_check_products
from show_and_checkout_2_3 import show_products


#-----------------------(2--> We maintain the same add_product function of the version before so not much change here)--------
#-----------------------(2.1--> The only change we have is adding that current_category = category_name)----------------------
#-----------------------(2.1-->This little change will solve the problem we have with the current_category variable)----------
 
def add_products(basket, products): 
    print("Add products to the basket:")

    category_name = show_products(products)

    if category_name is None:
        return

    product = get_and_check_products(category_name, products)
    current_units = basket[product["name"]]["units"] if product["name"] in basket else 0

    units = get_and_check_numeric(f"How many {product["name"]} units are you getting: ", current_units)
    
    if product["name"] in basket:
        basket[product["name"]]["units"] += units
    else:
        basket[product["name"]] = {"price": product["price"], "units": units}
    
    print("")
    print(f"{units} units of {product["name"]} added successfully at {product["price"]:.2f}€ per unit to the basket.")
    
    buy_another_product(basket, products, current_category = category_name)
    
#-----------------------(3--> Here we have a little improve that will solve the problem that we have with the current category--
#-----------------------by adding that the current_category = to category_name in the add_products function)--------------------
#-------------------------------------------(Sub-menu explained)----------------------------------------------------------------
#-----------------------(1. To add another product of the same category--> like the name says it basically give the option to---
#-----------------------the user to add a product of the same category without having to choose it again)-----------------------
#-----------------------(2. To add products of another category--> So here we basically just access the add_products function---
#-----------------------and basically just run that function the time the user wants)-------------------------------------------
#-----------------------(3. Return to main menu--> Basically print some message of finishing adding and return to the main menu)

def buy_another_product(basket, products, current_category=None): 
    while True:
        print("")
        print("Sub menu: ")
        print("1. To add another product of the same category") 
        print("2. To add products of another category")
        print("3. Return to main menu")
        
        try:
            option = int(input("Choose an option: "))
            if option == 1:
                if current_category:
                    print("")
                    product = get_and_check_products(current_category, products)
                    current_units = basket[product["name"]]["units"] if product["name"] in basket else 0

                    units = get_and_check_numeric(f"How many {product['name']} units are you getting: ", current_units)

                    if product["name"] in basket:
                        basket[product["name"]]["units"] += units 
                    else:
                        basket[product["name"]] = {"price": product["price"], "units": units}
                    
                    print("")
                    print(f"{units} units of {product['name']} added successfully at {product['price']:.2f}€ per unit to the basket.")
                else:
                    print("No current category selected. Please select option 2 to choose a new category or option 3 to return to the main menu.")
                continue
           
            elif option == 2:
                add_products(basket, products)
                break

            elif option == 3:
                print("You have finished adding products.")
                print("Returning to the main menu...")
                print("")
                break
            else:
                print("")
                print("Invalid Input, please enter a number between (1-3).")
        except ValueError:
            print("Invalid input, please enter a number betwween (1-3)")
            print("")
   