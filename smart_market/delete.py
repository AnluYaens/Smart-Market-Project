"""
Handles the functionality for deleting products from the shopping basket.

"""
import streamlit as st


def delete_products(basket): 
    """
    Deletes products or reduces the quantity of products in the shopping basket.

    This function allows users to:
    - View the contents of the current basket.
    - Select a product to delete.
    - Specify how many units to remove from the basket.
    - Update the basket accordingly.

    Args:
        basket (dict): Current shopping basket with product details (name, price, units).

    Returns:
        None
    """
    if not basket:
        st.warning("Your basket is empty. Try adding some products! :shopping_trolley:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return
    
    # Display the basket contents
    st.write("Your basket")
    for name, details in basket.items():
        product_total_price = details["price"] * details["units"]
        st.write(f"{name}: {details["price"]:.2f}€ per unit, total units: {details["units"]}, product total price: {product_total_price:.2f}€") 
    
    # Select a product to delete
    user_input = st.selectbox("Select the product you want to delete: ", [""] + list(basket.keys()))
    if not user_input:
        st.warning("Please select the item you want to delete. :smile:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return
    
    # Specify the number of units to delete
    max_units = basket[user_input]["units"]
    units = st.number_input(
        f"How many units of {user_input} you want to delete: ", 
        min_value=1, max_value=max_units, step=1
    )

    # removed the specified units
    if st.button("Delete from the basket"):
        remaining_units = basket[user_input]["units"] - units
        if remaining_units == 0:
            del basket[user_input]
            st.success(
                f"All units of {user_input} deleted successfully from the basket"
            )       
        else:
            basket[user_input]["units"] = remaining_units
            st.success(
                f"{units} units of {user_input} deleted successfully from the basket! "
            )
            
    # Display the updated basket 
    if basket:
        st.write(
            "Your basket have been updated"
        )
        for item, details in basket.items():
            st.write(
                f"{item}: {details["units"]} units, {details["price"]:.2f}€ per unit"
            )
    else:
        st.write(
            "The basket is empty"
        )

    # Provide info about the navigation bar so the user can go back to lobby
    st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
