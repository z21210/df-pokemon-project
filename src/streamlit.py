import streamlit as st

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
    
'''
stat   hp  atk def spe_atk spe_def speed
min	1	5	5	10	    20	    5
max	255	190	250	194	    250	    200

st.divider()
st.header("Components")

st.write("Pokemon Name")
st.write("Abilities")
abilities1, abilities2 = st.columns(2)
'''