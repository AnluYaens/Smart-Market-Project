import streamlit as st


def delete_products(basket): 
    if not basket:
        st.warning("Your basket is empty. Try adding some products!")
        return
    
    st.write("Your basket")
    user_input = st.selectbox("Select the product you want to delete: ", [""] + list(basket.keys()))
    if not user_input:
        st.warning("No product selected.")
        return
    
    max_units = basket[user_input]["units"]
    units = st.number_input(
        f"How many units of {user_input} you want to delete: ", 
        min_value=1, max_value=max_units, step=1
    )

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

