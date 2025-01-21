import streamlit as st

# Function to select and validate a product from a given category
def get_and_check_products(category, products): 
    # Create a list of products in the selected category
    product_list = [product["name"] for product in products[category]]
    
    # Display a dropdown for the user to select a product
    user_input = st.selectbox(
        "Select a product:", [""] + product_list
    )   
    if user_input:
        # Return the selected product details if a product is chosen
        return next(
            product for product in products[category] if product["name"] == user_input
        )
    # Return None if no product is selected
    return None

# Function to select and validate a category
def get_and_check_category_key(products): 
    # Get a list of avaliable categories
    categories = list(products.keys())
    
    # Display a dropdown for the user to select a category
    category_key = st.selectbox(
        "Select a category:", [""] + categories
    )
    
    if category_key:
        # Display the products from the selected category
        st.write(
            f"Products from {category_key}"
        )
        for product in products[category_key]:
            st.write(
                f"{product["name"]} - {product["price"]:.2f}€ per unit"
            )
    # Return the selected category key
    return category_key
            
            

           
             

