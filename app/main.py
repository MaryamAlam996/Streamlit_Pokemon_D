import streamlit as st
from data_processing import extract_from_csv
from data_processing import extract_and_clean_data
from data_processing import add_url_as_new_column


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
    df = extract_and_clean_data('data/pokemon.csv')
    print('Data extraction complete')
    
    df = add_url_as_new_column(df)
    st.dataframe(df)
    
    
    
    
if __name__ == "__main__":
    main()
