import pickle
import pandas as pd
import numpy as np

with open("trees.pickle", "rb") as f:
    trees = pickle.load(f)

query_df = pd.read_csv("query.csv")
df = pd.read_csv("input.csv").reset_index().rename(columns={'index': 'row_index'})

out_rows = []

for index, row in query_df.iterrows():
    out_row = {}
    x, y, dmg_min, dmg_max = row["x"], row["y"], row["dmg_min"], row["dmg_max"]
    
    for dt, (tree, indices) in trees.items():
        # nearest neighbours
        distances, nearest_indices = tree.query([[x, y]], k=len(indices))
        found = False
        for distance, nearest_index in zip(distances[0], nearest_indices[0]):
            original_index = indices[nearest_index]
            # select the nearest which matches the criteria
            closest_point = df.loc[(df['row_index'] == original_index) & (df['dmg_type'] == dt) & (df['dmg'] >= dmg_min) & (df['dmg'] <= dmg_max)]
            if not closest_point.empty:
                out_row[dt] = closest_point.iloc[0]["dmg"]
                found = True
                break
        if not found:
            out_row[dt] = 0

    out_rows.append(out_row)

result_df = pd.DataFrame(out_rows)
result_df.to_csv("out.csv", index=False)