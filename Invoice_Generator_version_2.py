# Invoice Generator
# Create an Virtual store with some products that after create an
# invoice of what you buy
# Hacer un json files que contenga todos los productos de la tienda para que
# la persona sepa que puede comprar (tratar de separarlos por secciones)
# tambien buscar y estudiar data structures
# Entender las datas structures and stremalit para hacer el frontend en un
# futuro. Hacer un file que guarde las variables del primer producto
# y consecuentes y sume al final el total de estas.

print("")
print("Welcome to your store!")
print("")

products = {
    "Peach": 1.5,
    "Apple": 1.5,
    "Orange": 2.0,
    "Milk": 1.2,
    "Bread": 0.8,
    "Water": 0.5
}

basket = {}


def get_and_check_products(user_product):
    while True:
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


def show_your_basket(basket):
    print("Your basket: ")
    print("")
    if not basket:
        print("Your Basket is empty! try adding some products of the list: ")
        print(", ".join(products.keys()))
        print("")

    else:
        total = 0
        for name, price in basket.items():
            print(f"{name}: {price:.2f}€")
            total += price
        iva = total * 0.21
        total_with_iva = total + iva
        print(f"Total: {total:.2f}€")
        print(f"Total with iva: {total_with_iva:.2f}€")
        print("")

        proceed_to_check_out()


def proceed_to_check_out():
    while True:
        try:
            user_input = input("Dou you want to proceed to checkout? (yes/no):").strip().lower()
            if user_input == "yes":
                print("")
                print("Which payment method would you like to use? ")
                print("1. Debit/Credit card")
                print("2. Paypal")

            elif user_input == "no":
                print("Returning to the main menu...")
                return
            else:
                print("")
                print("Invalid Input, please enter (yes/no).")
        except ValueError:
            print("")
            print("Invalid Input, please enter (yes/no).")


def add_products(basket):
    product_name = get_and_check_products("Enter the product name: ")
    basket[product_name] = products[product_name]
    print(f"Product {product_name} added successfully at {products[product_name]:.2f}€.")


def calculate_total_price(units, unit_price):
    total_price = units * unit_price
    return total_price


def get_and_check_numeric(units, unit_price=False):
    while True:
        try:
            value = float(input(units)) if unit_price else int(input(units))
            if value <= 0:
                print("The amount entered is not correct,(x>0)")
                print("")
                break
            else:
                return value
        except ValueError:
            print("Input not valid, please enter a number")
            print("")


def buy_another_products(another_product):
    while True:
        try:
            answers = (input(another_product))
            if answers == ("yes"):
                input(main())
                break
            else:
                return answers
        except ValueError:
            print("Input not valid, please enter a number")
            print("")


def main():
    while True:
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
            elif option == 5:
                print("Thank you for shooping! Goodbye!.")
                print("Hope to see you soon!")
                break
            else:
                print("Invalid option, please choose between 1-4")
        except ValueError:
            print("Invalid input, please enter a number betwween 1-4")


main()
