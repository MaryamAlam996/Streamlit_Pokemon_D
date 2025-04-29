import streamlit as st
import plotly.express as px

# User input field 

st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")
poke = st.text_input("Pokemon name", "")
st.write("Your selected Pokemon is", poke)

# Pokemon stats functions

# Pokemon stats display

