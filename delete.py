import streamlit as st

# Function that delete products from the basket 
def delete_products(basket): 
    if not basket:
        # Check if the basket is empty
        st.warning("Your basket is empty. Try adding some products! :shopping_trolley:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return
    
    # Display the basket contents
    st.write("Your basket")
    for name, details in basket.items():
        # Calculate the total price of each product in the basket
        product_total_price = details["price"] * details["units"]
        st.write(f"{name}: {details["price"]:.2f}€ per unit, total units: {details["units"]}, product total price: {product_total_price:.2f}€") 
    # Allow the user to select the product they want to delete
    user_input = st.selectbox("Select the product you want to delete: ", [""] + list(basket.keys()))
    if not user_input:
        st.warning("Please select the item you want to delete. :smile:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return
    
    # Ask the user how many units they want to delete of the product selected 
    max_units = basket[user_input]["units"]
    units = st.number_input(
        f"How many units of {user_input} you want to delete: ", 
        min_value=1, max_value=max_units, step=1
    )

    # When the button is clicked, the specified units are deleted
    if st.button("Delete from the basket"):
        remaining_units = basket[user_input]["units"] - units
        if remaining_units == 0:
            # Remove the product entirely from the basket if no units remain
            del basket[user_input]
            st.success(
                f"All units of {user_input} deleted successfully from the basket"
            )       
        else:
            # Update the remaining units in the basket
            basket[user_input]["units"] = remaining_units
            st.success(
                f"{units} units of {user_input} deleted successfully from the basket! "
            )
            
    # Display the updated basket or inform the user if it’s empty
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
