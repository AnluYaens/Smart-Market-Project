#---------------------------------------------(Delete_Products module)---------------------------------------------------------
#-----So here because of the change of the structure by dividing the code in modules we dont have changes in the code----------
#-----The only change is how we explained the code and that we import a get_and_check function---------------------------------

from get_and_checks_2_4 import get_and_check_product_in_basket


#-----------------------(1. We maintain the same delete_products function of the version before)-------------------------------
#-----------------------The only change is taht we incorporate the products variable to it but this change is been studied-----


def delete_products(basket, Products): 
    if not basket:
        print("Your basket is empty. Try adding some products!")
        print("")
        return
    
    print("\nYour basket:")
    for name, details in basket.items():
        details["price"] * details["units"]
        print(f"{name}, total units: {details["units"]}")
    print("")

    product_name = get_and_check_product_in_basket(basket, "Enter the product name to delete: ").strip().capitalize()
    
    while True:
        try:
            units = int(input(f"How many units of {product_name} you want to delete: "))
            if units > basket[product_name]["units"] or units < 1:
                print(f"Input not valid. You have {basket[product_name]["units"]} units.")
                choice = input("Do you want to delete all units intead? (yes/no): ").strip().lower()
                if choice == "yes":
                    units = basket[product_name]["units"]
                    break 
                elif choice == "no":
                    print("")
                    continue     
                else:
                    print("Invalid Input, please enter (yes/no).")
                    return
            else:
                break
        except ValueError:
            print(f"Input not valid. You have {basket[product_name]["units"]} units.")
            print("")

    remaining_units = basket[product_name]["units"] - units
    if remaining_units == 0:
        del basket[product_name]
        print(f"All units of {product_name} deleted successfully from the basket")       
    else:
        basket[product_name]["units"] = remaining_units
        print(f"{units} units of {product_name} deleted successfully from the basket! ")
        print("")
    
    delete_another_product(basket)
   
#-----------------------(3. Here we also maintain the same function as the version before)-------------------------------------

def delete_another_product(basket):
    while True:
        print("")
        user_input = (input("Do you want to delete another product? (yes/no): ")).strip().lower()
        if user_input == ("no"):
            print("You have finished deleting products.")
            print("Returning to the main menu...")
            print("")
            break
        elif user_input == ("yes"):
            delete_products(basket ,None)
            break
        else:
            print("")
            print("Invalid Input, please enter (yes/no).")
