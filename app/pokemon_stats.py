import streamlit as st
from data_processing import extract_and_clean_data
from transform_image import  get_image


# User input field 

#st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")

df = extract_and_clean_data('../data/pokemon.csv')
#print(df)


poke = st.number_input("Enter Pokemon ID")

pokemon = df[df['pokedex_number'] == poke]
#name = "".join(list(pokemon['name']))
name = df.loc[poke,'name']

st.write("Your selected Pokemon is", name)

print(pokemon['name'])
# Pokemon stats functions

# Fetch Pokemon image url
poke_image = get_image(df.loc[poke,"image_url"])

# Pokemon stats display
st.header(f"You caught {name}!")
print("".join(list(pokemon['species'])))
#st.image(poke_image)


col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label ="Species", value=df.loc[poke,'species'])
with col2:
   st.metric("Height (m)", value=df.loc[poke,'height_m'])
    
with col3:
    st.metric("Weight (kg)", df.loc[poke,'weight_kg'])
st.divider()
st.dataframe(df.loc[poke])