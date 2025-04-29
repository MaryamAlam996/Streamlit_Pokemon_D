import streamlit as st
import plotly.express as px

# User input field 

st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")
poke = st.text_input("Pokemon name", "")
st.write("Your selected Pokemon is", poke)

# Pokemon stats functions

# Fetch Pokemon image url
poke_image = 

# Pokemon stats display
st.header(f"You caught {poke_name}!")
st.image(poke_image)
col1, col2, col3 = st.columns(3)
col1.metric("Species", )
col2.metric("Height", )
col3.metric("Weight", )
st.divider()
st.dataframe()