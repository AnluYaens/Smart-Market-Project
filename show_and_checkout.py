import streamlit as st
from get_and_checks import get_and_check_category_key

# Function that display available product categories and their products
def show_products(products):
    st.subheader("Categories of products")
    # Allow the use to select a category
    category_key = get_and_check_category_key(products)

    if category_key:
        # inform the user of the selected category they are viewing
        st.info(f"Currently viewing products in the {category_key} category.")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
    else:
        # This message will appear until a product is selected
        st.warning("Please choose a category. :smile:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
             

# Function that display the contents of the basket
def show_your_basket(basket): 
    if not basket:
        # Notify the user if the basket is empty
        st.warning("Your basket is empty. Try adding some products. :shopping_trolley:")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return

    # Display the basket contents
    st.write("Your basket:")               
    total = 0
    # Initialize total cost
    for name, details in basket.items():
        # Calculate the total price of each product
        product_total_price = details["price"] * details["units"]
        st.write(f"{name}: {details["price"]:.2f}€ per unit, total units: {details["units"]}, product total price: {product_total_price:.2f}€") 
        total += product_total_price # Sum the total of all the products to the total cost

    # Calculate and display (IVA) and total cost with it
    iva = total * 0.21
    total_with_iva = total + iva
    st.write(f"Total (Without IVA): {total:.2f}€")
    st.write(f"IVA (21%): {iva:.2f}€")
    st.write(f"Total (With IVA): {total_with_iva:.2f}€")
    
    # Allow the user to proceed to checkout if the button is clicked
    if st.button("Proceed to checkout", key="proceed_to_checkout_btn", use_container_width=True):
        st.session_state.current_page = "Proceed to checkout"
    st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")

    
# Function to handle the checkout process
def proceed_to_check_out(basket):
    if not basket:
        # Notify the user if the basket is empty
        st.warning("Your basket is empty. add some products to proceed!")
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
        return
    
    st.header("Proceed to checkout")
    
    # Calculate the total cost
    total = sum(details["price"] * details["units"] for details in basket.values())
    iva = total * 0.21
    total_with_iva = total + iva

    # Display the total cost with and without (IVA)
    st.write(f"Total (Without Tax): {total:.2f}€")
    st.write(f"IVA (21%): {iva:.2f}€")  
    st.write(f"Total (With Tax): {total_with_iva:.2f}€")

    # Display payment method options
    payment_method = st.selectbox("Payment Method:", ["Debit/Credit Card", "Paypal"])
    
    # Confirm the payment process if the button is clicked
    if st.button("Confirm payment"):
        st.success(f"payment processed successfully! :white_check_mark:")
        st.success("Thanks for shopping with us! :sparkles: Hope to see you soon! :dizzy:")
    else:
        # Provide info about the navigation bar so the user can go back to lobby
        st.info("If you want to go back to the lobby use the (:house:) button on the sidebar!.	:top:	:rewind:")
