import streamlit as st
from get_and_checks import get_and_check_category_key

def show_products(products):
    st.subheader("Categories of products")
    get_and_check_category_key(products)
             


def show_your_basket(basket): 
    if not basket:
        st.warning("Your basket is empty. Try adding some products.")
        return

    st.write("Your basket:")               
    total = 0
    for name, details in basket.items():
        product_total_price = details["price"] * details["units"]
        st.write(f"{name}: {details["price"]:.2f}€ per unit, total units: {details["units"]}, product total price: {product_total_price:.2f}€") 
        total += product_total_price

    iva = total * 0.21
    total_with_iva = total + iva
    st.write(f"Total (Withous Tax): {total:.2f}€")
    st.write(f"Total (With Tax): {total_with_iva:.2f}€")
    


def proceed_to_check_out(): 
    payment_method = st.selectbox("Payment Method:", ["Debit/Credit Card", "Paypal"])
    if st.button("Proceed with the payment"):
        st.success(f"You chose {payment_method}. Thank you for shopping!")
        st.success("Hope to see you soon!")

