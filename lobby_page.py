import streamlit as st



def lobby_page(products):
    
    st.subheader("Welcome to the Lobby!")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("images/show_products.png", use_container_width=True)
        if st.button("Show Products", key=f"show_products_btn", use_container_width=True):
            st.session_state.current_page = "Show products"
        

    with col2:
        st.image("images/add_products.png", use_container_width=True)
        if st.button("Add Products", key=f"add_products_btn",use_container_width=True):
            st.session_state.current_page = "Add products"
        
    with col3:
        st.image("images/delete_products.png", use_container_width=True)
        if st.button("Delete Products", key=f"delete_products_btn", use_container_width=True):
            st.session_state.current_page = "Delete products"
        
    col4, col5 = st.columns(2)

    with col4:
        st.image("images/show_basket.png", use_container_width=True)
        if st.button("Show Basket", key=f"show_basket_btn", use_container_width=True):
            st.session_state.current_page = "Show basket"
        

    with col5:
        st.image("images/checkout.png", use_container_width=True)
        if st.button("Checkout", key=f"checkout_btn", use_container_width=True):
            st.session_state.current_page = "Proceed to checkout"
        
