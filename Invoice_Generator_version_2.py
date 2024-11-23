# Invoice Generator
# Hacer un json files que contenga todos los productos de la tienda para que
# la persona sepa que puede comprar (tratar de separarlos por secciones)
# tambien buscar y estudiar data structures
# Entender las datas structures and stremalit para hacer el frontend en un
# futuro. 

print("")
print("Welcome to your store!")

products = {
    "Peach": 1.5,
    "Apple": 1.5,
    "Orange": 2.0,
    "Milk": 1.2,
    "Bread": 0.8,
    "Water": 0.5
}

basket = {} 


def get_and_check_products(user_product): #In this function basically we validate that the product that the user is choosing exist and is the sames as in the products list
    while True:                            # If it isnt the same we give the user a preview of the products so he can know what products he can choose if he hasnt seen them
        try:
            user_input = input(user_product).capitalize()
            if user_input not in products:
                print("Input not valid, please select a product of the list: ")
                print(", ".join(products.keys()))
                print("")
            else:
                return user_input
        except ValueError:
            print("Input not valid, please enter a number")
            print("")


def get_and_check_numeric(units): #This function basically is created to validate that the units of the products are >1 or <20 
    while True:
        try:
            user_input = int(input(units))
            if 0 >= user_input > 20:
                print("Invalid amount entered, (units= (1-20))")
                print("")
            else:
                return user_input
        except ValueError:
            print("Input not valid, please enter a number between (1-20)")
            print("")

def show_your_basket(basket): #In this function we can validaate first if exist something in the basket or not, and within that give an option or other 
    print("Your basket: ")    # And calculate the total of the products in the basket and call the proceed to checkout function to give the user option to pay or go to the main menu. 
    print("")           
    if not basket:
        print("Your Basket is empty! try adding some products of the list: ")
        print(", ".join(products.keys()))
        print("")
    else:
        total = 0
        for name, (price, units) in basket.items():
            product_total_price = price * units
            print(f"{name}: {price:.2f}€ per unit, total units: {units}, {product_total_price:.2f}€") 
           
            total += product_total_price
        iva = total * 0.21
        total_with_iva = total + iva
        print(f"Total: {total:.2f}€")
        print(f"Total with iva: {total_with_iva:.2f}€")
        print("")

        proceed_to_check_out()

 
def proceed_to_check_out(): #So in this one we create a fucntion where we have a main loop and a sub loop that validate 
    while True:              #if the consumer want to proceed to check out and validate his payment method or return to the main menu.
        
        user_input = input("Do you want to proceed to checkout? (yes/no):").strip().lower()
        if user_input == "no":
            print("Returning to the main menu...")
            return   
        elif user_input == "yes":
            while True:
                try:
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
                except ValueError:
                    print("")
                    print("Invalid input. Please enter a number (1 or 2).")
           
            print("")
            print("Thank you for shopping! Goodbye!.")
            print("Hope to see you soon!")
            break
        else:
            print("")
            print("Invalid Input, please enter (yes/no).")
      


def add_products(basket): #We use this function so we can add any product of the list to the basket and use other functions to validate like get and check products and numeric.
    product_name = get_and_check_products("Enter the product name: ")
    units = get_and_check_numeric(f"How many {product_name} units you getting: ")
    basket[product_name] = (products[product_name], units)
    print("")
    print(f"{units} units of {product_name} added successfully at {products[product_name]:.2f}€ per unit to the basket.")
    buy_another_product(basket)


def delete_products(basket): #We use this function so we can delete any product of the basket or quantity of the product.
    product_name = get_and_check_numeric("Enter the product name: ")
    basket[product_name] = products[product_name]
    print(f"Product {product_name} deleted successfully of the basket! ")
        

def buy_another_product(basket): #We create this function basically to ask the consumer if he want another product and validate the input to not get an error.
    while True:
            user_input = (input("Do you want to add another product? (yes/no): ")).lower().strip()
            if user_input == ("no"):
                print("You have finished adding products.")
                print("Returning to the main menu...")
                break
            elif user_input == ("yes"):
                add_products(basket)
            else:
                print("")
                print("Invalid Input, please enter (yes/no).")
                buy_another_product(basket)
            break       
           


def main():   #This is the main function where we will find mainly the main menu that is the heart of this proyect and a loop where he can choose wherever option he wants and within that
    while True:  # He will be able to do different things, including getting out of the store.
        print("")
        print("Menu:")
        print("1. Show products")
        print("2. Add a product to the basket")
        print("3. Delete a product of the basket")
        print("4. Show your basket")
        print("5. Exit")

        try:
            option = int(input("Choose an option: "))
            print("")

            if option == 1:
                print("Avaliable products: ")
                for name, price in products.items():
                    print(f"{name}: {price:.2f}€")
            elif option == 2:
                add_products(basket)
            elif option == 4:
                show_your_basket(basket)
                break
            elif option == 5:
                print("Thank you for shopping! Goodbye!.")
                print("Hope to see you soon!")
                break
            else:
                print("Invalid option, please choose between 1-5")
        except ValueError:
            print("Invalid input, please enter a number betwween 1-5")


main()
