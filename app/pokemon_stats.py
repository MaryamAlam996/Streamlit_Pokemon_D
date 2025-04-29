import streamlit as st
from data_processing import extract_and_clean_data
from transform_image import  get_image


# User input field 

df = extract_and_clean_data('../data/pokemon.csv')


def enter_pokemon_id(df):
    poke = st.number_input("Enter Pokemon ID")
    df.loc[poke,'name']
    st.write("Your selected Pokemon is", poke)
    st.header(f"You caught {poke}!")
    return df.loc[poke,'name']


# Fetch Pokemon image url
def display_image(df,pokemon_name):
    poke_image = get_image(df.loc[pokemon_name,"image_url"])
    st.image(poke_image,width=200)

# Pokemon stats display

def display_stat_columns(df,pokemon_name):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label ="Species", value=df.loc[pokemon_name,'species'])
    with col2:
        st.metric("Height (m)", value=df.loc[pokemon_name,'height_m'])
        
    with col3:
        st.metric("Weight (kg)", df.loc[pokemon_name,'weight_kg'])
    
def display_df(df,pokemon_name):    
    st.divider()
    st.dataframe(df.loc[pokemon_name])