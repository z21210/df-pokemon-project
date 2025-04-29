import streamlit as st
import pandas as pd
import plotly.express as px

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
    
    # Create columns for the metrics
    col1, col2, col3, col4 = st.columns(4)

    # Display metrics in each column
    with col1:
        st.metric(label="Height", value=f"{selected["height_m"].values[0]}m")
    with col2:
        st.metric(label="Weight", value=f"{selected["weight_kg"].values[0]}kg")
    with col3:
        st.metric(label="Generation", value=f"{selected["generation"].values[0]}")
    with col4:
        st.metric(label="Status", value=f"{selected["status"].values[0]}")

    display_types(selected)
    
def display_types(selected):
    colour_chart = {
        'Normal':'gray',
        'Fire':'red',
        'Water':'blue',
        'Grass':'green',
        'Electric':'orange',
        'Ice':'blue',
        'Fighting':'orange',
        'Poison':'violet',
        'Ground':'orange',
        'Flying':'blue',
        'Psychic':'violet',
        'Bug':'green',
        'Rock':'orange',
        'Ghost':'gray',
        'Dragon':'red',
        'Dark':'gray',
        'Steel':'gray',
        'Fairy':'violet'
    }
    
    # Display Type as badges
    type1 = selected['type_1'].iloc[0]
    type2 = selected['type_2'].iloc[0]

    markdown = f"Type  \n:{colour_chart[type1]}-badge[{type1}]"
    
    # Checks for a second type
    if pd.notnull(type2):
        markdown += f" :{colour_chart[type2]}-badge[{type2}]"
    
    # Display the type
    st.markdown(markdown)

def display_graph(selected):
    #stat   hp  atk def spe_atk spe_def speed
    #min	1	5	5	10	    20	    5
    #max	255	190	250	194	    250	    200

    attributes = {
        "HP":selected["hp"].values[0],
        "Attack":selected["attack"].values[0],
        "Defense":selected["defense"].values[0],
        "Special Attack":selected["sp_attack"].values[0],
        "Special Defense":selected["sp_defense"].values[0],
        "Speed":selected["speed"].values[0]
    }

    fig = px.data.gapminder().query

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
