import streamlit as st
from src.load import load_pokemon
from src.streamlit import *

# Read in pokemon
df = load_pokemon()

st.title("Streamlit Pokemon Project")

number = st.number_input("Choose a Pokedex Number", 1, 898, placeholder="Please enter a number between 1 and 898")

# Filter the DataFrame based on the selected filters
filtered_df = get_pokemon(df, number)
names = filtered_df["name"].values

variant = st.segmented_control("Variations", filtered_df["name"].values, default = names[0])
selected = get_variant(filtered_df, variant)

display_metrics(selected, variant)

