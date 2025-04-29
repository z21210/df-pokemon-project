import streamlit as st
import pandas as pd

st.title("Streamlit Pokemon Project")

# Read in CSV
df = pd.read_csv("data/pokemon.csv")

# Data Display
st.write("OG Dataframe")
df

# Summary Stats found not useful outside of data analysis
# st.write(df.describe())

'''markdown
###

# copied in from demo 5 to implement filters
# INSERT sidebar code here:
# Add a sidebar for filters
st.sidebar.header("Filters")
# Passenger Class filter
pclass_filter = st.sidebar.multiselect(
    "Select Passenger Class",
    options=sorted(df["Pclass"].unique()),
    default=sorted(df["Pclass"].unique()),
)
# Embarked Port filter
embarked_filter = st.sidebar.multiselect(
    "Select Embarked Port",
    options=sorted(df["Embarked"].unique()),
    default=sorted(df["Embarked"].unique()),
)

# END INSERT sidebar

# MODIFY CODE BELOW WITH filtered_df
# Total Passengers
# total_passengers = df["PassengerId"].nunique()
total_passengers = filtered_df["PassengerId"].nunique()
# Overall Survival Rate
# overall_survival_rate = df["Survived"].mean()
overall_survival_rate = filtered_df["Survived"].mean()
# Average Age
# average_age = df["Age"].mean()
average_age = filtered_df["Age"].mean()
# Survival Rate by Gender
# survival_rate_by_gender = df.groupby("Sex", observed=False)["Survived"].mean()
survival_rate_by_gender = filtered_df.groupby("Sex", observed=False)[
    "Survived"
].mean()
# END MODIFY df
### '''
number = st.number_input("Choose a Pokedex Number", 1, 898, placeholder="Please enter a number between 1 and 898")

st.write("Current pokedex number is ", number)

# Filter the DataFrame based on the selected filters
filtered_df = df[
    (df["pokedex_number"] == number)
]

filtered_df
names = filtered_df["name"].values

st.header(names[0])
st.write("Pokedex Number #", filtered_df["pokedex_number"])
st.image(f"https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/{number:03}.png", width=100)
st.caption(filtered_df["japanese_name"].values[0])
st.metric(label="HP", value=filtered_df["hp"].values[0])
st.markdown(
    "Type  \n"
    ":green-badge[:material/grass: Grass] :violet-badge[Poison]"
)
st.segmented_control("Variations", filtered_df["name"].values)

st.divider()
st.header("Components")

st.write("Pokemon Name")
st.segmented_control("Variations", filtered_df["name"].values)
col1, col2, col3, col4 = st.columns(4)
col1.metric("HP", 60, border=True)
col2.metric("A metric", 40, "something", delta_color="off")
col3.metric("A metric", 41, 2, border=True)
col4.metric("Another", 2)
st.divider()

with col1:
    st.metric(label="HP", value=HP)