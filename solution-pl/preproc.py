import pandas as pd
import polars as pl

#df = pl.read_csv("input.csv")
df = pd.read_csv("input.csv")
damage_types = df["dmg_type"].unique()

df = pl.from_pandas(df)
damage_types = pl.DataFrame({"dmg_type": damage_types})
df.write_parquet("input.parquet")
damage_types.write_parquet("damage_types.parquet")
