
#import libraries needed
import pandas as pd
import plotly.express as px

# i had uploaded these into Hex, which I used to write the code for this
births_df = pd.read_csv("births.csv")
deaths_df = pd.read_csv('deaths.csv')
events_df = pd.read_csv("events.csv")

# get counts of births by year
birth_year_counts = births_df["year_birth"].value_counts().reset_index()

# rename columns
birth_year_counts.columns = ["year", "num_births"]

# percents
birth_year_counts_percent = births_df["year_birth"].value_counts(normalize=True)

# average age at death
average_age_at_death = round((deaths_df["year_death"] - deaths_df["year_birth"]).mean(),2)

# chart the births per year
fig = px.bar(
    birth_year_counts,
    x="year",
    y="num_births",
    title="Number of documented leap year births per year",
    color_discrete_sequence=["orchid"],
)
fig.update_layout(
    title={
        "text": "Number of documented leap year births per year",
        "x": 0.5,
        "xanchor": "center",
    },
)
fig.show()