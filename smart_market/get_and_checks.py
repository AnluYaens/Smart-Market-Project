"""
Provides utility functions for selecting and validating product categories and individual products.

"""
import streamlit as st


def get_and_check_products(category, products): 
    """
    Retrieves and validates the product selected by the user from a given category.

    Args:
        category (str): The category of products to select from.
        products (dict): A dictionary of product categories and their respective products.

    Returns:
        dict or None: Details of the selected product, or None if no product is selected.
    """
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
    """
    Retrieves and validates the category selected by the user.

    Args:
        products (dict): A dictionary of product categories.

    Returns:
        str or None: The selected category key, or None if no category is selected.
    """
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
            
            

           
             

