import polars as pl
import pandas as pd
from flask import Flask

app = Flask(__name__)

# Ez az oszlopok felcserélése miatt van így
#df = pl.read_csv("input.csv")
df = pd.read_csv("input.csv")
damage_types = df["dmg_type"].unique()
df = pl.from_pandas(df)
damage_types = pl.DataFrame({"dmg_type": damage_types})


@app.route("/ping")
def ping():    
    query_df = pl.read_csv("query.csv")

    out = []
    for row in query_df.iter_rows():
        out_row = {}
        for dt in damage_types["dmg_type"]:
            sub_df = df.filter(
                (pl.col("dmg_type") == dt)
                & (pl.col("dmg") >= row[2])
                & (pl.col("dmg") <= row[3])
            ).select(["x", "y", "dmg"])
            if sub_df.is_empty():
                out_row[dt] = 0
            else:
                diffs = ((sub_df["x"] - row[0]) ** 2) + ((sub_df["y"] - row[1]) ** 2)
                out_row[dt] = sub_df[diffs.arg_min(), 2]

        out.append(out_row)

    pl.DataFrame(out).write_csv("out.csv")
    return "OK"


@app.route("/")
def ok():
    return "OK"


if __name__ == "__main__":
    app.run(port=5678)