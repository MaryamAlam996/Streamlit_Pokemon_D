import streamlit as st
from extract import extract_from_csv


def main():    
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Pokemon Dashboard",
        page_icon="❤️",
        layout="wide",
        initial_sidebar_state="auto",
    )
    # Set the title of the app
    st.title("Pokemon Dataset Explorer")
    
    print('Extracting data')
    df = extract_from_csv('data/pokemon.csv')
    print('Data extraction complete')
    


if __name__ == "__main__":
    main()
