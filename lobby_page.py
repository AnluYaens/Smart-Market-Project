import streamlit as st


# Function that display the lobby page with navigation options
def lobby_page(products):
    
    st.subheader("Welcome to the Lobby!")

    # Create columns to organize the layout of navigation buttons and images
    col1, col2, col3 = st.columns(3)
    
    # First column: Show Products
    with col1:
        st.image("images/show_products.png", use_container_width=True) # Display the image for Show products
        if st.button("Show Products", key=f"show_products_btn", use_container_width=True):
            # Set the current page to "Show products"
            st.session_state.current_page = "Show products"
        
    # Second column: Add Products
    with col2:
        st.image("images/add_products.png", use_container_width=True) # Display the image for Add products
        if st.button("Add Products", key=f"add_products_btn",use_container_width=True):
            # Set the current page to "Add products"
            st.session_state.current_page = "Add products"

    # Third column: Delete Products    
    with col3:
        st.image("images/delete_products.png", use_container_width=True) # Display the image for delete products
        if st.button("Delete Products", key=f"delete_products_btn", use_container_width=True):
            # Set the current page to "Delete products"
            st.session_state.current_page = "Delete products"

    # Create two additional colums for showing the basket and proceeding to checkout    
    col4, col5 = st.columns(2)

    # Fourth column: Show basket
    with col4:
        st.image("images/show_basket.png", use_container_width=True) # Display the image for show basket
        if st.button("Show Basket", key=f"show_basket_btn", use_container_width=True):
            # Set the current page to "Show basket"
            st.session_state.current_page = "Show basket"
        
    # Fifth column: Checkout
    with col5:
        st.image("images/checkout.png", use_container_width=True) #Display the image for checkout
        if st.button("Checkout", key=f"checkout_btn", use_container_width=True):
            # Set the current page to "Checkout"
            st.session_state.current_page = "Proceed to checkout"
        
