"""
Handles the functionality for displaying products, the basket, and managing checkout.

"""
import streamlit as st
from smart_market.get_and_checks import get_and_check_category_key


def show_products(products):
    """
    Displays available product categories and the products within them.

    Args:
        products (dict): A dictionary of product categories and their respective products.

    Returns:
        None
    """
    st.subheader("Categories of products")
    category_key = get_and_check_category_key(products)

    if category_key:
        st.info(f"Currently viewing products in the {category_key} category.")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
    else:
        st.warning("Please choose a category. :smile:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
             


def show_your_basket(basket): 
    """
    Displays the contents of the shopping basket along with cost calculations.

    Args:
        basket (dict): The current shopping basket with product details.

    Returns:
        None
    """
    if not basket:
        st.warning("Your basket is empty. Try adding some products. :shopping_trolley:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return

    st.write("Your basket:")               
    total = 0
    for name, details in basket.items():
        product_total_price = details["price"] * details["units"]
        st.write(f"{name}: {details["price"]:.2f}€ per unit, total units: {details["units"]}, product total price: {product_total_price:.2f}€") 
        total += product_total_price 

    iva = total * 0.21
    total_with_iva = total + iva
    st.write(f"Total (Without IVA): {total:.2f}€")
    st.write(f"IVA (21%): {iva:.2f}€")
    st.write(f"Total (With IVA): {total_with_iva:.2f}€")
    
    if st.button("Proceed to checkout", key="proceed_to_checkout_btn", use_container_width=True):
        st.session_state.current_page = "Proceed to checkout"
    st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")

    
def proceed_to_check_out(basket):
    """
    Manages the checkout process for the shopping basket.

    Args:
        basket (dict): The current shopping basket with product details.

    Returns:
        None
    """
    if not basket:
        st.warning("Your basket is empty. add some products to proceed!")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return
    
    st.header("Proceed to checkout")
    
    total = sum(details["price"] * details["units"] for details in basket.values())
    iva = total * 0.21
    total_with_iva = total + iva

    st.write(f"Total (Without Tax): {total:.2f}€")
    st.write(f"IVA (21%): {iva:.2f}€")  
    st.write(f"Total (With Tax): {total_with_iva:.2f}€")

    payment_method = st.selectbox("Payment Method:", ["Debit/Credit Card", "Paypal"])
    if st.button("Confirm payment"):
        st.success(f"payment processed successfully! :white_check_mark:")
        st.success("Thanks for shopping with us! :sparkles: Hope to see you soon! :dizzy:")
    else:
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
