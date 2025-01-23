"""
Handles the functionality for adding products to the shopping basket.

"""
import streamlit as st
 

def add_products(basket, products):
    """
    Adds products to the shopping basket.

    This function allows users to:
    - Select a category of products.
    - Choose a product from the selected category.
    - Specify the number of units to add (with a maximum limit of 20 per product).
    - Update the shopping basket with the selected products and quantities.

    Args:
        basket (dict): Current shopping basket with product details (name, price, units).
        products (dict): Available products organized by categories.

    Returns:
        None
    """ 
    st.write("Add products to the basket:")
    
    # Allow the user to select a product category
    category_key = st.selectbox("Select a category: ", [""] + list(products.keys()))
    if not category_key:
        st.warning("Please select a category. :smile:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return

    # Show the products available in the selected category
    product_list = [product["name"] for product in products[category_key]]
    user_input = st.selectbox(f"Select a product from {category_key}", [""] + product_list)
    if not user_input:
        st.warning("Please select a product. :100:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return
    
    # Retrieve the selected product details 
    product = next((prod for prod in products[category_key] if prod["name"] == user_input), None)
    if not product:
        st.error("Product not found. Please try again!")
        return
    
    # check the current units in the basket and limit to 20
    current_units = basket.get(user_input, {}).get("units", 0)
    max_units = max(1,20 - current_units)
    
    if current_units >= 20:
        st.warning(f"You already have the maximum allowed (20 units) of {user_input}, try adding other products!")
        return
    
    # Allow the user to specify the number of units to add
    units = st.number_input(
        f"How many {product["name"]} units are you getting: ", 
        min_value=1, max_value=max_units, step=1
    )

    # Add the product to the basket
    if st.button("Add product to the basket"):
        if user_input in basket:
            basket[user_input]["units"] += units
        else:
            basket[user_input] = {"price": product["price"], "units": units}

        st.success(f"{units} units of {user_input} added successfully at {product["price"]:.2f}€ per unit to the basket.")
    
    
    

    # Display the updated basket
    st.write("Your basket have been updated")
    
    for item, details in basket.items():
        st.write(
            f"{item}: {details["units"]} units, {details["price"]:.2f}€ per unit"
        )
    
    # Provide info about the navigation bar so the user can go back to lobby
    st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
    
   