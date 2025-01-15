import streamlit as st

def show_products(products):
    categories = list(products.keys())
    category_key = st.selectbox("Choose a category:", [""] + categories)
    
    if category_key:
        st.write(f"Products from {category_key}:")
        for product in products[category_key]:
            st.write(f"{product["name"]} - {product["price"]:.2f}€ per unit")
    return category_key            


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

    st.write("Select your payment method to proceed: ")
    payment_method = st.selectbox(["Payment Method:", ["Debit/Credit Card", "Paypal"]])
    st.success(f"You chose {payment_method}. Thanl you for shopping!")


