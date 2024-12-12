#------------------------------------(Store_Web--Invoice_Generator----> Final Proyect)-----------------------------------------
#----So in this version we change basically the structure of our proyect by dividing the entire code in differents modules-----
#----And also we change the form we express and explain the code by organizing it in a better way------------------------------
#----This will help us with optimizing and versatily at the time of debuging, adding or deleting some part of our code---------
#----First we import os and json librays that will help us with the json files-------------------------------------------------
#----Because we separate the code in modules we have to import the functions of the other modules so the code can run----------
#----We also change the way the json fiel of products is organized to make it easier to change---------------------------------


#-----We can see here how we call the 2 libraries we are going to use in this proyect------------------------------------------
#-----And also we can see here an example of calling functions from other modules so the code can run properly-----------------
import os
import json
from add_2_1 import add_products
from delete_2_2 import delete_products
from show_and_checkout_2_3 import show_products, show_your_basket, proceed_to_check_out

#-----Then we start the coding by introducing the user with a welcome message so we have interaction with it-------------------

print("")
print("Welcome to your store!")
print("")

#-----Here we use our first json file, which storage all of our products-------------------------------------------------------

with open ("2.products.json","r") as p:
    products = json.load(p)

#-----We remain the same here by using a dictionary for the basket(probably will change this in the future)--------------------
basket = {
} 


#-----To conclude this module we have our main function, that will basically be the heart of our proyect-----------------------
#-----This function contain our main menu where all the magic and structure of our code happen---------------------------------
#----------------------------------------------------------We have 5 options--------------------------------------------------- 
#-----------------------(1.Show products--> Here we use the show_products function, but also we implement some code; first we-- 
#-----------------------create a variable that will help us dont run innecesary code(for example: The user choose exit instead-
#-----------------------of a category so this variable help us exit the loop, then we use a simple code that will show a-------
#-----------------------message to the user if he want to see another category and will give an output depending on yes or no)-
#-----------------------(2.Add a product to the basket--> Here we only access to the add_products function)--------------------
#-----------------------(3.Delete a product from the basket--> Here we only access to the delete_products function)------------
#-----------------------(4.Show your basket--> Here we start by calling the show_your_basket function)
def main():
    while True:
        print("Menu:")
        print("1. Show products")
        print("2. Add a product to the basket")
        print("3. Delete a product from the basket")
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

#-----Here we finish our main function by calling it---------------------------------------------------------------------------
main()

#-----And to conclude our main module, we uses this code to basically create our second json file------------------------------
#-----It will create a summary of all the sells registered succesfully in the store so we can know what we sell and how many---
#-----We also need to fix some things here, for example: that right now the file only registered the last sell made------------

if os.path.isfile("3.basket.json") and os.access("3.basket.json", os.R_OK):

    with open ("3.basket.json","r") as p:
        old_basket = json.load(p)
        

else:
    with open("3.basket.json","w") as p:
        basket = json.dumps(basket)
        p.write(basket)
