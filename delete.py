from get_and_checks import get_and_check_product_in_basket
import streamlit as st


def delete_products(basket, Products): 
    if not basket:
        st.warning("Your basket is empty. Try adding some products!")
        return
    
    st.write("Your basket")
    for name, details in basket.items():
        st.write(f"{name}: {details["units"]} units")
   

    product_name = st.selectbox("Select the product you want to delete: ", list(basket.keys())).strip().capitalize()
    if not product_name:
        st.warning("No product selected.")
        return
    
    max_units = basket[product_name]["units"]
    units = st.number_input(f"How many units of {product_name} you want to delete: ", min_value=1, max_value=max_units, step=1)

    remaining_units = basket[product_name]["units"] - units
    if remaining_units == 0:
        del basket[product_name]
        st.success(f"All units of {product_name} deleted successfully from the basket")       
    else:
        basket[product_name]["units"] = remaining_units
        st.success(f"{units} units of {product_name} deleted successfully from the basket! ")
        
    
    submenu_option = st.radio(
       "Do you want to delete another product?", ["Yes", "No"]
    )
   
    if submenu_option == "Yes":
        delete_products(basket, Products)
    
    else:
        st.info("Returning to the main menu...")

