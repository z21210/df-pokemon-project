import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Mock Pokémon Data ---
# data = [
#     {"name": "Pikachu", "type": "Electric", "hp": 35, "attack": 55, "defense": 40},
#     {"name": "Charizard", "type": "Fire/Flying", "hp": 78, "attack": 84, "defense": 78},
#     {"name": "Bulbasaur", "type": "Grass/Poison", "hp": 45, "attack": 49, "defense": 49},
#     {"name": "Squirtle", "type": "Water", "hp": 44, "attack": 48, "defense": 65},
#     {"name": "Gengar", "type": "Ghost/Poison", "hp": 60, "attack": 65, "defense": 60},
#     {"name": "Calyrex Shadow Rider", "type": "Psychic/Ghost", "hp": 100, "attack": 165, "defense": 100}
# ]

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, '../data/pokemon.csv')
data = pd.read_csv(csv_path)

df = pd.DataFrame(data)

# --- Streamlit App Layout ---
st.title("Pokémon Stats Visualisation")

st.write("### View Raw Pokémon Data")

columns_to_show = ["pokedex_number", "name", "generation", "type_1", "type_2", "hp", "attack", "defense", "total_points"]
st.dataframe(df[columns_to_show])

# --- Filters ---
generations = sorted(df['generation'].unique())
selected_generation = st.selectbox("Filter by Generation", options=["All"] + generations)

type1_options = sorted(df['type_1'].dropna().unique())
type2_options = sorted(df['type_2'].dropna().unique())

selected_type_1 = st.selectbox("Filter by Type 1", options=["All"] + list(type1_options))
selected_type_2 = st.selectbox("Filter by Type 2", options=["All"] + list(type2_options))

search_name = st.text_input("Search by Pokémon Name (partial match allowed)")

filtered_df = df.copy()
if selected_generation != "All":
    filtered_df = filtered_df[filtered_df['generation'] == selected_generation]

if selected_type_1 != "All":
    filtered_df = filtered_df[filtered_df['type_1'] == selected_type_1]

if selected_type_2 != "All":
    filtered_df = filtered_df[filtered_df['type_2'] == selected_type_2]

if search_name:
    filtered_df = filtered_df[filtered_df['name'].str.contains(search_name, case=False, na=False)]

st.write("### Filtered Pokémon Data")
st.dataframe(filtered_df[columns_to_show])

# --- Visualisation ---
if not filtered_df.empty:
    st.write("### Compare Pokémon Stats")
    stat_option = st.selectbox("Select Stat to Visualise", options=["total_points", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed"])

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(filtered_df['name'], filtered_df[stat_option], color='lightgreen')
    ax.set_ylabel(stat_option.replace("_", " ").title())
    ax.set_title(f"{stat_option.replace('_', ' ').title()} Comparison")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
else:
    st.write("No Pokémon match the search criteria.")


