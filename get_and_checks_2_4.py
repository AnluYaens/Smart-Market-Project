#---------------------------------------------(Get_and_checks module)----------------------------------------------------------
#-----So here because of the change of the structure by dividing the code in modules we dont have changes in the code----------
#-----The only change is how we explained the code and here we dont import functions to this module----------------------------
#-----This 3 get_and_checks functions remain exactly the same as the version before--------------------------------------------

def get_and_check_products(category, products): 
    product_names = [product["name"].capitalize() for product in products[category]]
    while True:
        user_input = input("Enter the product name: ").strip().capitalize()      
        if user_input in product_names:
            return next(product for product in products[category] if product["name"].capitalize() == user_input)
        else:
            print(f"Invalid product. Please select a product from: {", ".join(product_names)}\n")


def get_and_check_product_in_basket(basket, user_input):
    while True:
        product_name = input(user_input).strip().capitalize()
        if product_name in basket:
            return product_name
        else:
            print("Product not found in the basket. Please enter a valid product from your basket.")
            print("Your basket: ")
            for name, details in basket.items():
                details["price"] * details["units"]
                print(f"{name}, total units: {details["units"]}")
            print("")
            


def get_and_check_numeric(units, current_units=0): 
    while True:
        try:
            user_input = int(input(units))
            if 1 <= user_input <= 20 and current_units + user_input <= 20:
                return user_input
            elif current_units + user_input > 20:
                print(f"Cannot add more than 20 units. You already have {current_units} units.") 
            else:
                print("Invalid amount entered, (units= (1-20))")
                print("")
        except ValueError:
            print("Input not valid, please enter a number between (1-20)")
            print("")