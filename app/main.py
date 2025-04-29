import streamlit as st



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


if __name__ == "__main__":
    main()
