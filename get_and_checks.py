import streamlit as st
from show_and_checkout import show_products


def get_and_check_products(category, products): 
    product_names = [product["name"].capitalize() for product in products[category]]
  
    user_input = st.selectbox("Select a product: ", product_names)   
    if user_input:
        return next(product for product in products[category] if product["name"].capitalize() == user_input)
    return None


def get_and_check_product_in_basket(basket, user_input):
    return st.selectbox(user_input, list(basket.keys()))
            


def get_and_check_numeric(units, current_units=0): 
    max_units = 20 - current_units
    return st.number_input(units, min_value=1, max_value=max_units, step=1)
           
             

def get_and_check_category_key(products):
    
    submenu_option = st.radio(
        "Do you want to see another category?", ["Yes","No"] 
    )
    if submenu_option == "Yes":
        show_products(products)
    
    else:
        st.info("Returning to the main menu...")