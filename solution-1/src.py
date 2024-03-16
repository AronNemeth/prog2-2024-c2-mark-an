import pandas as pd
from scipy.spatial import KDTree

if __name__ == "__main__":
    df = pd.read_csv("input.csv")
    query_df = pd.read_csv("query.csv")

    damage_types = df["dmg_type"].unique()
    out = []

    # saving indicies from the original df
    trees = {dt: (KDTree(df.loc[df["dmg_type"] == dt, ["x", "y"]]), df.loc[df["dmg_type"] == dt].index) for dt in damage_types}

    for idx, row in query_df.iterrows():
        out_row = {}
        for dt in damage_types:
            tree, indices = trees[dt]
            sub_df = df.loc[df["dmg_type"] == dt]

            # finding nearest point
            _, nearest_index = tree.query([row["x"], row["y"]], k=1)
            original_index = indices[nearest_index] 

            # check if in range
            closest_point = sub_df.loc[original_index]
            if closest_point["dmg"] >= row["dmg_min"] and closest_point["dmg"] <= row["dmg_max"]:
                out_row[dt] = closest_point["dmg"]
            else:
                out_row[dt] = 0

        out.append(out_row)

    pd.DataFrame(out).to_csv("out.csv", index=False)

