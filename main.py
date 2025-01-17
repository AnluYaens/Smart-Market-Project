import json
import streamlit as st
from add import add_products
from delete import delete_products
from show_and_checkout import show_products, show_your_basket, proceed_to_check_out
from lobby_page import lobby_page
import time
# python -m streamlit run main.py


def read_products():
    try:
        with open ("json_files/products.json","r") as p:
            return json.load(p)
    except FileNotFoundError:
        st.error("Products file not found")
        return{}
    except json.JSONDecodeError:
        st.error("Invalid json file format")
        return {}
    
def save_basket():
    try:
        with open("json_files/basket.json", "w") as p:
            json.dump(st.session_state.basket, p, indent=4)
    except Exception as e:
        st.error(f"The basket could not be saved: {e}")

def initialize_basket():
    if "basket" not in st.session_state:
        st.session_state.basket = {}
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Lobby"


def main():
    
    products = read_products()
    if not products:
        return
    
    initialize_basket()
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Lobby"

    st.title(":shopping_bags: Smart Market")
    st.markdown("### Bringing the store to your home!")
    st.markdown("---")
    
    
    st.sidebar.title("Navigation")
    if st.sidebar.button(":house:", key="lobby_btn_sidebar"):
        st.session_state.current_page = ":house:"
        

    tab1, tab2, tab3 = st.tabs(["Lobby", "Contact", "About"])

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
            
        else:
            st.session_state.current_page = "Lobby"
            lobby_page(products)

    with tab2:
            st.header("Contact us")
            st.write("Email: your.favorite.store.at.home@gmail.com")
            st.write("Phone: 151-.......")
            st.write(" Address: in your heart :heart:")
        
    with tab3:
            st.header("About us")
            st.write("Welcome to Smart Market! My name is Angel Jaen and I am excited to share this project with you. As a freshman Software Engineering major, this is my very first step into the world of technology and innovation.")
            st.write("Smart Market is more than just a project - it is a reflection of my passion, curiosity, and dedication to learning and creating. I have carefully designed every feature and written every line of code with the goal of providing you with a seamless and enjoyable experience.")
            st.write("I sincerely hope that you find this project useful and inspiring. If you enjoy using Smart Market, I would be incredibly grateful if you would explore my other projects and share them with your friends and family. Your support and feedback means the world to me and plays a crucial role in helping me grow as a developer.")
            st.write("Thank you for being part of my journey. Your encouragement inspires me to keep learning, improving, and creating. Together we can bring more innovative ideas to life!.")
            st.write("Here is my GitHub link: https://github.com/AnluYaens?tab=repositories :eyes:")
            st.write("Hope you enjoy your shopping experience with us!:sparkles:")
            
    st.sidebar.markdown("---")
    st.sidebar.markdown("Smart Market © 2025")
    
    
   
                    

if __name__ == "__main__":
    main()




