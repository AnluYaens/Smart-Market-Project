import streamlit as st


def get_and_check_products(category, products): 
    product_list = [product["name"] for product in products[category]]
    
    user_input = st.selectbox(
        "Select a product:", [""] + product_list
    )   
    if user_input:
        return next(
            product for product in products[category] if product["name"] == user_input
        )
    return None


def get_and_check_category_key(products): 
    categories = list(products.keys())
    
    category_key = st.selectbox(
        "Select a category:", [""] + categories
    )
    
    if category_key:
        st.write(
            f"Products from {category_key}"
        )
        for product in products[category_key]:
            st.write(
                f"{product["name"]} - {product["price"]:.2f}€ per unit"
            )
    
    return category_key
            
            

           
             

