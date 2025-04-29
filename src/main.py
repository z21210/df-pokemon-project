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

def get_pokemon_by_name(df, name):
    return df[
        (df["name"].str.contains(name, case=False, na=False))
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

# Read in pokemon
df = load_pokemon()

st.title("Streamlit Pokemon Project")

number = st.number_input("Choose a Pokedex Number", 1, 898, placeholder="Please enter a number between 1 and 898")
search_name = st.text_input("Search by Pokémon Name (partial match allowed)")
if search_name:
    filtered_df = get_pokemon_by_name(df, search_name)
    if not filtered_df.empty:
        variant = st.selectbox("Select Variation", filtered_df["name"].values)
        number = filtered_df["pokedex_number"].values[0]
        selected = get_variant(filtered_df, variant)
        display_metrics(selected, variant)


# Filter the DataFrame based on the selected filters
else:
    filtered_df = get_pokemon(df, number)
    names = filtered_df["name"].values

    variant = st.segmented_control("Variations", filtered_df["name"].values, default = names[0])
    selected = get_variant(filtered_df, variant)

    display_metrics(selected, variant)

