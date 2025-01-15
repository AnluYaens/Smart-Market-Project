import json
import streamlit as st
from add import add_products
from delete import delete_products
from show_and_checkout import show_products, show_your_basket, proceed_to_check_out



def read_products():
    try:
        with open ("json_files/products.json","r") as p:
            return json.load(p)
    except FileNotFoundError:
        st.error("Products file not found")
        return{}
    except json.JSONDecodeError:
        st.error("Invalid json file format")
        return {}
    
def save_basket():
    try:
        with open("json_files/basket.json", "w") as p:
            json.dump(st.session_state.basket, p, indent=4)
    except Exception as e:
        st.error(f"The basket could not be saved: {e}")

def initialize_basket():
    if "basket" not in st.session_state:
        st.session_state.basket = {}


def main():
    st.title("Welcome to your Store!")
    st.sidebar.title("Main menu")

    products = read_products()
    if not products:
        return
    
    initialize_basket()
    
    menu = ["Show products", "Add products", "Delete products", "Show basket", "Proceed to checkout"]
    option = st.sidebar.selectbox("Select an option:", menu)


    if option ==  "Show products":
        show_products(products)
       
         
    elif option == "Add products":
        add_products(st.session_state.basket, products)

    elif option == "Delete products":
        delete_products(st.session_state.basket)   

    elif option == "Show basket":
        show_your_basket(st.session_state.basket)
    
    elif option == "Proceed to checkout":
        proceed_to_check_out()
        save_basket()
        
                    

if __name__ == "__main__":
    main()




