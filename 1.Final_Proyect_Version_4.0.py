#Store web / Invoice generator ---> Final Proyect
#First of all we start by importing os and json that will help us in the future
import os
import json

#Then we start by putting a welcome message
print("")
print("Welcome to your store!")
print("")
 
#We use this 2 lines of code to read the json files that we have to storage the products
#Our products consist basically of a dictionary with list
with open ("2.products.json","r") as p:
    products = json.load(p)

basket = {
} 

#We maintain this function the same, that show the products and also check
# if the category that the user is inputing is correct and exist and give 2 options: 1-->choose a category, 2---> exit to the main menu
# if the choosen category exist it will show the products of that category and will return an error if the doesnt exist and give the option to try again         
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


#In this function basically we validate that the product that the user is choosing exist and is the sames as in the products list
# If it isnt the same we give the user a preview of the products so he can know what products he can choose 
def get_and_check_products(category, products): 
    product_names = [product["name"].capitalize() for product in products[category]]
    while True:
        user_input = input("Enter the product name: ").strip().capitalize()      
        if user_input in product_names:
            return next(product for product in products[category] if product["name"].capitalize() == user_input)
        else:
            print(f"Invalid product. Please select a product from: {", ".join(product_names)}\n")


#In this function basically we check that the product the user is choosing is writted correctly and also if it exist in the basket
# if it isnt the function will give an message and will show the products in the basket
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
            

#In this function we basically check that the user dont insert more than 20 units of 1 product to the basket
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
        

#so this time we do a little change with this function--> we add the current_units variable that basically will help us solve the problem
# of adding less than 20 units of a product to the basket
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

    
#In this function we basically create a submenu that will give 3 options and depending on the choosen option will do different things
# 1. ---> will give the option of add another product of the same category ----> we need to fix these one
# 2. ---> will return to the add_products function and will run it again to add a product of a different category without having to go to the main menu 
# 3. ---> will return to the main menu if the user doesnt want to add another product
# else will give and error message and will give the user the submenu to try again
def buy_another_product(basket, products, current_category=None): 
    while True:
        print("")
        print("Sub menu: ")
        print("1. To add another product of the same category") 
        print("2. To add products of another category")
        print("3. To return to main menu")
        
        try:
            option = int(input("Choose an option: "))
            if option == 1:
                if current_category:
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
                    print("No current category selected. Please select option 2 to choose a new category.")
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
                print("Invalid Input, please enter (yes/no).")
        except ValueError:
            print("Invalid input, please enter a number betwween 1-3")
            print("")
   
#In this function is basically the same as add_products but reversed ---> if the basket is empty it will give an error message and will return to the main menu
#If basket have some products it will show the products on basket and will enter the get_and_check_product_in_basket function that will ask the user the name of 
# the product he want to delete and also check that this exist and is writted correctly if doesnt exist will appear a error messsage and show the products of basket
# and the user will have the possibility to try again ---> if this goes right, will enter a while loop where basically we are going to check that the units inserted are
# more less than the units on the basket and more than 1 if this goes wrong it will appear a message giving the option to delete all units instead or trying again
# finally the remaining units will update to the basket and will apear the delete_another_function 
def delete_products(basket): 
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
   

#In this function we basically gave the option to delete another product if the user writte no it eill give a finish deleting products messsage and will return to the main menu
# If the user inserted yes, it will enter the delete_products function again but with the none after the basket if products is not used, ex: no items in basket
# and a error message if the user put something that is not yes-no and will have the option to try again
def delete_another_product(basket):
    while True:
        print("")
        user_input = (input("Do you want to delete another product? (yes/no): ")).strip().lower()
        if user_input == ("no"):
            print("You have finished deleting products.")
            print("Returning to the main menu...")
            break
        elif user_input == ("yes"):
            delete_products(basket ,None)
            break
        else:
            print("")
            print("Invalid Input, please enter (yes/no).")


# In this function we basically are going to show the products that are on the basket, if the basket is empty will gave a message error and will show the category of products we can add
# if the basket got something it will call with a for loop item for item with the name and details of each and after it will calculate the (total-iva- and total_with_iva)
# and will print all the products with their name and unit price, also the total units with price and the total price of the products without and with taxes (iva)
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


#In this function we basically are going to ask the user which payment method he want to use to check_out
# the user will have the options and after this will appear a message saying which payment method he use and a goodbye message that we will see in the main function
# if an invalid payment method is inserted will apear a message error with the payment methods he can use and the user will try again
def proceed_to_check_out(): 
    while True:
        print("")
        print("Select you payment method to proceed: ")
        payment_method = input("Enter 1 for Debit/Credit card or 2 for Paypal: ").strip()
        if payment_method == "1":
            print("You choose Debit/Credit card.")
            print("")
            break
        elif payment_method == "2":
            print("You choose Paypal.")
            print("")
            break
        else:
            print("")
            print("Invalid payment method selected.")
     

#This is the main function where all the magic happen, basically the heart of this store, where we will find the main menu --> that will give us 5 options
#1. Show products --> where we create a variable named category key instead of just putting the show_products option, because, if the user insert exit and this category key isnt in
#none it will gave us an error and a basically and infinite loop.
#2. Add a product to the basket --> Where we basically just put the add_products function explained before
#3. Delete a product from the basket --> As same as before just put the function (delete_products) explained before
#4. Show your basket --> Here the thing change, because instead of just putting the show_your_basket function we first put the show your basket funcion after this finish we put if basket, 
# refering if are products in the basket so if doesnt this doesnt run, give the user the option to proceed to checkout if yes will enter the proceed_to_checkout function and will appear
# an goodbye message; if the answer is no will return to the main menu and if the asnwer is something else a message error will appear, showing the corrects inputs and the user will try again
#5. It will give a goodbye message and will exit the program
def main():
    while True:
        print("Menu:")
        print("1. Show products")
        print("2. Add a product to the basket")
        print("3. Delete a product of the basket")
        print("4. Show your basket")
        print("5. Exit")

        try:
            option = int(input("Choose an option: "))

            if option == 1:
                while True:
                    category_key = show_products(products)
                    if category_key is None: 
                        break
                    
                    while True:
                        user_input = (input("Do you want to see another category? (yes/no): ")).strip().lower()
                        if user_input == ("no"):
                            print("Returning to the main menu...\n") 
                            break   
                        elif user_input == ("yes"):
                            break
                        else:
                            print("Input not valid. Please enter (yes/no)")
                    if user_input == "no":  
                        break
                                    
            elif option == 2:
                add_products(basket, products)

            elif option == 3:
                delete_products(basket, products)   

            elif option == 4:
                show_your_basket(basket)
                if basket:
                    while True:
                        user_input = input("Do you want to proceed to checkout? (yes/no): ").strip().lower()
                        if user_input == "yes":
                            proceed_to_check_out()   
                            print("Thank you for shopping! Goodbye!.")
                            print("Hope to see you soon!")
                            return
                        elif user_input == "no": 
                            print("Returning to the main menu...") 
                            break
                        else:     
                            print("")
                            print("Invalid Input, please enter (yes/no).")   

            elif option == 5:
                print("")
                print("Thank you for shopping! Goodbye!.")
                print("Hope to see you soon!")
                print("")
                break
            else:
                print("Invalid option, please choose between 1-5")
                print("")
        except ValueError:
            print("Invalid input, please enter a number betwween 1-5")
            print("")

#We call the main function
main()

#Here it will check if the json files of the basket is created if it is it will read and write the new one
#(We need to fix the error that it only save the last result and not all of them)
#If it is no file it will create it and will save the result in this json file

if os.path.isfile("3.basket.json") and os.access("3.basket.json", os.R_OK):

    with open ("3.basket.json","r") as p:
        old_basket = json.load(p)
        print(type(old_basket))
        
    
    with open("3.basket.json","w") as p:
        basket = json.dumps(basket)
        p.write(basket)

else:
    with open("3.basket.json","w") as p:
        basket = json.dumps(basket)
        p.write(basket)
