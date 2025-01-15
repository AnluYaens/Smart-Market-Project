from get_and_checks import get_and_check_products
from show_and_checkout import show_products
import streamlit as st
 
def add_products(basket, products): 
    st.write("Add products to the basket:")
    category_name = show_products(products)

    if category_name is None:
        st.warning("No category selected. Returning to main menu!")
        return

    product = get_and_check_products(category_name, products)
    if not product:
        st.warning("Invalid product selected. Please try again.")
        return
    
    current_units = basket[product["name"]]["units"] if product["name"] in basket else 0

    units = st.number_input(f"How many {product["name"]} units are you getting: ", min_value=1, max_value=20, step=1, value=1)

    if units + current_units > 20:
        st.warning(f"Cannot add more than 20 units of a product. You already have {current_units} units")
        return 
    
    if product["name"] in basket:
        basket[product["name"]]["units"] += units
    else:
        basket[product["name"]] = {"price": product["price"], "units": units}
    
    st.success(f"{units} units of {product["name"]} added successfully at {product["price"]:.2f}€ per unit to the basket.")
    
    submenu_option = st.radio(
        "Select an option"
        ["Add another product of the same category", "Add a product from a different category", "Return to main menu"]
    )
    
    if submenu_option == "Add another product of the same category":
        add_products_same_category(basket, products, category_name)
    
    elif submenu_option == "Add a product from a different category":
        add_products(basket, products)
    
    else:
        st.info("Returning to the main menu...")


def add_products_same_category(basket, products, current_category):
    st.write(f"Adding another product from the category: {current_category}")
    product = get_and_check_products(current_category, products)
    if not product:
        st.warning("Invalid product selected")
        return
    
    current_units = basket[product["name"]]["units"] if product["name"] in basket else 0

    units = st.number_input(f"How many {product["name"]} units are you getting: ", min_value=1, max_value=20, step=1, value=1)

    if units + current_units > 20:
        st.warning(f"Cannot add more than 20 units of a product. You already have {current_units} units")
        return 
    
    if product["name"] in basket:
        basket[product["name"]]["units"] += units
    else:
        basket[product["name"]] = {"price": product["price"], "units": units}
    
    st.success(f"{units} units of {product["name"]} added successfully at {product["price"]:.2f}€ per unit to the basket.")