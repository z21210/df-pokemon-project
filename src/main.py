import pandas as pd

df = pd.read_csv('data/pokemon.csv')

df.set_index('pokedex_number')

# get which columns contain nulls
df.columns[df.isna().any()]
# 'type_2', 'weight_kg', 'ability_1', 'ability_2', 'ability_hidden', 'catch_rate', 'base_friendship', 'base_experience', 'growth_rate', 'egg_type_1', 'egg_type_2', 'percentage_male', 'egg_cycles'

# assert there are no null type_2 where there shouldn't be
assert all(df['type_number'] == 1*df['type_1'].notna() + 1*df['type_2'].notna())

# check what has null weight_kg
print(df[df['weight_kg'].isna()])
# Eternatus Eternamax has weight_kg as null for lore reasons; null is appropriate

# assert there are no null ability_n where there shouldn't be
assert all(df['abilities_number'] == 1*df['ability_1'].notna() + 1*df['ability_2'].notna() + 1*df['ability_hidden'].notna())

# check what has null catch_rate
print(df[df['catch_rate'].isna()])
# Galarians should have catch_rate equivalent to their normal variants; data transformation needed

# check what has null base_friendship
print(df[df['base_friendship'].isna()])
# Galarians and latest gen in dataset; bad nulls, will drop column entirely

# check what has null base_experience
print(df[df['base_experience'].isna()])
# Galarians and latest gen in dataset; bad nulls, will drop column entirely

# check what has null growth_rate
print(df[df['growth_rate'].isna()])
# Galarian Darmanitan Zen Mode has growth_rate as null for lore reasons; null is appropriate

# assert there are no null egg_type where there shouldn't be
assert len(df[df['type_number'] != 1*df['type_1'].notna() + 1*df['type_2'].notna()]) == 0

# percentage_male
print(df[df['percentage_male'].isna()])
# Galarians should have percentage_male equivalent to their normal variants; data transformation needed
# Others are genderless; appropriate nulls

# check what has null percentage_male
print(df[df['percentage_male'].isna()])
# Galarian Darmanitan Zen Mode has percentage_male as null for lore reasons; null is appropriate
