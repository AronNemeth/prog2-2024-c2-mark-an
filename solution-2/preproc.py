import pandas as pd
from scipy.spatial import cKDTree
import pickle

# modify column
df = pd.read_csv("input.csv")
df.columns = df.columns.str.replace('\r', '', regex=False)

damage_types = df["dmg_type"].unique()
trees = {}

for dt in damage_types:
    sub_df = df[df["dmg_type"] == dt].copy()
    # keep indices for reference later
    sub_df = sub_df.reset_index().rename(columns={'index': 'original_index'})
    tree_data = sub_df[["x", "y"]].to_numpy()
    tree = cKDTree(tree_data)
    # using original index
    indices = sub_df['original_index'].to_numpy()
    trees[dt] = (tree, indices)

with open("trees.pickle", "wb") as f:
    pickle.dump(trees, f)