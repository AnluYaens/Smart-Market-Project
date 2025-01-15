import json
import streamlit as st
from add import add_products
from delete import delete_products
from show_and_checkout import show_products, show_your_basket, proceed_to_check_out
from get_and_checks import get_and_check_category_key


def read_products():
    with open ("json_files/products.json","r") as p:
        return json.load(p)
    
def save_basket(basket):
    with open("json_files/basket.json", "w") as p:
        json.dump(basket, p, indent=4)



def main():
    st.title("Welcome to your Store!")
 
    products = read_products()
    if not products:
        st.warning("No products found. Please check the json file.")
        return
    
    basket = {}
    
    menu = ["Show products", "Add products", "Delete products", "Show basket", "Proceed to checkout"]
    option = st.sidebar.selectbox("menu", menu)


    if option ==  "Show products":
        st.subheader("Product categories")
        category_key = show_products(products)
        if category_key:
            get_and_check_category_key(products)
         
    elif option == "Add products":
        st.subheader("Add products")
        add_products(basket, products)

    elif option == "Delete products":
        st.subheader("Delete product from basket")
        delete_products(basket, products)   

    elif option == "Show basket":
        st.subheader("Your basket")
        show_your_basket(basket)
    
    elif option == "Proceed to checkout":
        st.subheader("Checkout")
        proceed_to_check_out()
        st.success("Thank you for shopping! Goodbye!")
        save_basket(basket)
        st.stop()
                    

    # elif option == 5:
    #     print("")
    #     print("Thank you for shopping! Goodbye!.")
    #     print("Hope to see you soon!")
    #     print("")
    #     break
    # else:
    #     print("Invalid option, please choose a number between 1-5")
    #     print("")'

if __name__ == "__main__":
    main()




