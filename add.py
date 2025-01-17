import streamlit as st
 
def add_products(basket, products): 
    st.write("Add products to the basket:")
    
    category_key = st.selectbox("Select a category: ", [""] + list(products.keys()))
    if not category_key:
        st.warning("Please select a category. :smile:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return

    product_list = [product["name"] for product in products[category_key]]
    user_input = st.selectbox(f"Select a product from {category_key}", [""] + product_list)
    if not user_input:
        st.warning("Please select a product. :100:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return
    
    product = next((prod for prod in products[category_key] if prod["name"] == user_input), None)
    if not product:
        st.error("Product not found. Please try again!")
        return
    
    current_units = basket.get(user_input, {}).get("units", 0)
    max_units = max(1,20 - current_units)
    
    if current_units >= 20:
        st.warning(f"You already have the maximum allowed (20 units) of {user_input}, try adding other products!")
    
    units = st.number_input(
        f"How many {product["name"]} units are you getting: ", 
        min_value=1, max_value=max_units, step=1
    )
    
    if st.button("Add product to the basket"):
        if user_input in basket:
            basket[user_input]["units"] += units
        else:
            basket[user_input] = {"price": product["price"], "units": units}

        st.success(f"{units} units of {user_input} added successfully at {product["price"]:.2f}€ per unit to the basket.")
    
    
    


    st.write("Your basket have been updated")
    
    for item, details in basket.items():
        st.write(
            f"{item}: {details["units"]} units, {details["price"]:.2f}€ per unit"
        )
    st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
    
   