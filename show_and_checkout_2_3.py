#---------------------------------------------(Show_and_Checkout module)-------------------------------------------------------
#-----So here because of the change of the structure by dividing the code in modules we dont have changes in the code----------
#-----The only change is how we explained the code and here we dont import functions to this module----------------------------
#-----The 2 first get_and_checks functions remain exactly the same as the version before---------------------------------------


def show_products(products):
    print("\nCategories of products:")
    for index, category in enumerate(products.keys(), 1):
        print(f"{index}. {category}")
    print("")
    
    while True:
        choose_category = input("Choose a Category (1/9) or type (exit) to return to the main menu: ").strip().lower()
        if choose_category == "exit":
            print ("Returning back to the main menu...\n")
            return None
        
        if choose_category.isdigit() and 1 <= int(choose_category) <= len(products):
            category_key = list(products.keys())[int(choose_category) -1]
            print(f"\nProducts from {category_key}:")
            for product in products[category_key]:
                print(f"{product["name"]} - {product["price"]:.2f}€ per unit")
            print("")
            return category_key
        else:
            print("Invalid category selected. please enter a valid number (1-9) or type (exit).\n")               


def show_your_basket(basket): 
    if not basket:
        print("Your basket is empty. Try adding some products")
        print(", ".join(basket.keys()))
        print("")
        return

    print("Your basket:")     
    print("")           
    total = 0
    for name, details in basket.items():
        product_total_price = details["price"] * details["units"]
        print(f"{name}: {details["price"]:.2f}€ per unit, total units: {details["units"]}, product total price: {product_total_price:.2f}€") 
        total += product_total_price
    iva = total * 0.21
    total_with_iva = total + iva
    print(f"Total (Withous Tax): {total:.2f}€")
    print(f"Total (With Tax): {total_with_iva:.2f}€")
    print("")


#--------------------------------------------(proceed_to_checkout function)----------------------------------------------------
#-----Here we change first that the introducing message is outside the loop----------------------------------------------------
#-----This will help us if the user introduce something different than 1 or 2 it instead give the introducing message----------
#-----It will give the question directly and also change the string option into a integer option-------------------------------

def proceed_to_check_out(): 
    print("")
    print("Select you payment method to proceed: ")
    while True:
        payment_method = int(input("Enter 1 for Debit/Credit card or 2 for Paypal: "))
        if payment_method == 1:
            print("You choose Debit/Credit card.")
            print("")
            break
        elif payment_method == 2:
            print("You choose Paypal.")
            print("")
            break
        else:
            print("")
            print("Invalid payment method selected. Please select between (1-2)")
            print("")