import streamlit as st
import pandas as pd

def load_pokemon():
    df = pd.read_csv("data/pokemon.csv")
    df.drop(columns=['base_friendship', 'base_experience'], inplace=True)
    return df

def get_pokemon(df, number):
    return df[
        (df["pokedex_number"] == number)
    ]

def get_variant(df, variant):
    return df[
        (df["name"] == variant)
    ]

def display_metrics(selected, variant):
    st.header(variant)
    st.write("Pokedex Number #", selected["pokedex_number"].values[0])
    st.image(f"https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/{number:03}.png", width=100)
    st.caption(selected["japanese_name"].values[0])
    st.metric(label="HP", value=selected["hp"].values[0])
    st.metric(label="Attack", value=selected["attack"].values[0])
    st.markdown(
        "Type  \n"
        ":green-badge[:material/grass: Grass] :violet-badge[Poison]"
    )

def display_defences(variant):
    st.write("Defences against types of damage")
    defences = [s for s in df.columns if s.startswith('against')]
    st.table(get_variant(variant).rename(columns = {d:d.split('_')[1].title() for d in defences})[defences])

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

display_defences(variant)