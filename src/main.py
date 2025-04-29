import streamlit as st
import pandas as pd

st.title("Streamlit Pokemon Project")

# Read in CSV
df = pd.read_csv("data/pokemon.csv")

number = st.number_input("Choose a Pokedex Number", 1, 898, placeholder="Please enter a number between 1 and 898")

st.write("Current pokedex number is ", number)

# Filter the DataFrame based on the selected filters
filtered_df = df[
    (df["pokedex_number"] == number)
]

names = filtered_df["name"].values

variant = st.segmented_control("Variations", filtered_df["name"].values, default = names[0])

selected = filtered_df[
    (filtered_df["name"] == variant)
]

selected

st.header(names[0])
st.write("Pokedex Number #", selected["pokedex_number"])
st.image(f"https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/{number:03}.png", width=100)
st.caption(selected["japanese_name"].values[0])
st.metric(label="HP", value=selected["hp"].values[0])
st.markdown(
    "Type  \n"
    ":green-badge[:material/grass: Grass] :violet-badge[Poison]"
)


st.divider()
st.header("Components")

st.write("Pokemon Name")
st.write("Abilities")
abilities1, abilities2 = st.columns(2)
st.pills("Tags", ["Type 1", "Type 2"])
st.badge("Type 1", color="green")
st.segmented_control("Variations", filtered_df["name"].values)
col1, col2, col3, col4 = st.columns(4)
col1.metric("HP", 60, border=True)
col2.metric("A metric", 40, "something", delta_color="off")
col3.metric("A metric", 41, 2, border=True)
col4.metric("Another", 2)
st.divider()
