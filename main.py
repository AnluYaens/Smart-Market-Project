import json
import streamlit as st
from add import add_products
from delete import delete_products
from show_and_checkout import show_products, show_your_basket, proceed_to_check_out
from lobby_page import lobby_page

#----------Intruction to run the programm----------------------------------------
#Introduce the command below on the terminal to run de program. Hope you like it!
#Command: "python -m streamlit run main.py"


# Function that read the products from the JSON file
def read_products():
    try:
        # Load the products from the JSON file
        with open ("json_files/products.json","r") as p:
            return json.load(p)
    except FileNotFoundError:
        st.error("Products file not found")
        # Display an error if the file is not found
        return{}
    except json.JSONDecodeError:
        # Display an error if the file format is invalid
        st.error("Invalid json file format")
        return {}

# Function that save the current basket into a JSON file    
def save_basket():
    try:
        # Write the basket data to a file
        with open("json_files/basket.json", "w") as p:
            json.dump(st.session_state.basket, p, indent=4)
    except Exception as e:
        # Handle any unexpected errors during saving
        st.error(f"The basket could not be saved: {e}")

#Function that initialize session state for the basket and current page
def initialize_basket():
    if "basket" not in st.session_state:
        st.session_state.basket = {} 
        # Initialize an empty basket
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Lobby"
        # Set the default page to lobby


# Main function that control de entire program
def main():
    
    # Load the products from the JSON file
    products = read_products()
    if not products:
        # Stop execution if no products are loaded
        return
    
    # Initialize session state
    initialize_basket()

    # Program tittle and description
    st.title(":shopping_bags: Smart Market")
    st.markdown("### Bringing the store to your home!")
    st.markdown("---")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    if st.sidebar.button(":house:", key="lobby_btn_sidebar"):
        # Set the current page to the lobby when the home button is clicked
        st.session_state.current_page = "Lobby"
        
    # Create tabs for the main sections
    tab1, tab2, tab3 = st.tabs(["Lobby", "Contact", "About"])

    # Tab 1: Main navigation through the lobby and product options
    with tab1:
        if st.session_state.current_page == "lobby":
            lobby_page(products)
        elif st.session_state.current_page == "Show products":
            show_products(products)
        elif st.session_state.current_page == "Add products":
            add_products(st.session_state.basket, products)
        elif st.session_state.current_page == "Delete products":
            delete_products(st.session_state.basket)
        elif st.session_state.current_page == "Show basket":
            show_your_basket(st.session_state.basket)
        elif st.session_state.current_page == "Proceed to checkout":
            proceed_to_check_out(st.session_state.basket)
            save_basket()
            # Save the basket after checkout
            
        else:
            # Default to the lobby page if no valid page is set
            st.session_state.current_page = "Lobby"
            lobby_page(products)

    #Tab 2: Contact information
    with tab2:
            st.header("Contact us")
            st.write("Email: your.favorite.store.at.home@gmail.com")
            st.write("Phone: 151-.......")
            st.write(" Address: in your heart :heart:")

    # Tab 3: About the project    
    with tab3:
            st.header("About us")
            st.write("Welcome to Smart Market! My name is Angel Jaen and I am excited to share this project with you. As a freshman Software Engineering major, this is my very first step into the world of technology and innovation.")
            st.write("Smart Market is more than just a project, it is a reflection of my passion, curiosity, and dedication to learning and creating. I have carefully designed every feature and written every line of code with the goal of providing you with a seamless and enjoyable experience.")
            st.write("I sincerely hope that you find this project useful and inspiring. If you enjoy using Smart Market, I would be incredibly grateful if you would explore my other projects and share them with your friends and family. Your support and feedback means the world to me and plays a crucial role in helping me grow as a developer.")
            st.write("Here is my GitHub link: https://github.com/AnluYaens?tab=repositories :eyes:")
            st.write("Hope you enjoy your shopping experience with us!:sparkles:")

    # Create another section in the sidebar        
    st.sidebar.markdown("---")
    st.sidebar.markdown("Smart Market © 2025")
    
# Entry point of the program
if __name__ == "__main__":
    main()




