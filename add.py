import streamlit as st
 
# Function that add products to the basket
def add_products(basket, products): 
    st.write("Add products to the basket:")
    
    # Allow the user to select a product category
    category_key = st.selectbox("Select a category: ", [""] + list(products.keys()))
    if not category_key:
        # This message will appear until a category is selected
        st.warning("Please select a category. :smile:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return

    # Show the products available in the category selected
    product_list = [product["name"] for product in products[category_key]]
    user_input = st.selectbox(f"Select a product from {category_key}", [""] + product_list)
    if not user_input:
        # This message will appear until a product is selected
        st.warning("Please select a product. :100:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return
    
    # Check if the selected product exists 
    product = next((prod for prod in products[category_key] if prod["name"] == user_input), None)
    if not product:
        # If the product dont exist this error will be displayed
        st.error("Product not found. Please try again!")
        return
    
    # Evaluate how many units can be added, following the max limit of 20
    current_units = basket.get(user_input, {}).get("units", 0)
    max_units = max(1,20 - current_units)
    
    if current_units >= 20:
        # If someone insert more than 20 units of a product, this message will be displayed
        st.warning(f"You already have the maximum allowed (20 units) of {user_input}, try adding other products!")
    
    # Allow the user to select the quantity they wants to add
    units = st.number_input(
        f"How many {product["name"]} units are you getting: ", 
        min_value=1, max_value=max_units, step=1
    )

    # When the button is clicked the products will be added to the basket 
    if st.button("Add product to the basket"):
        if user_input in basket:
            # Update existing units of the product
            basket[user_input]["units"] += units
        else:
            # Add new product to the basket
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
    
   