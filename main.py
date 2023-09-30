# %%
# package import
import pandas as pd
import altair as alt
import numpy as np
from scipy import stats
import datetime

# %%
# data source
names_url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(names_url)

# %%
# display number of rows and columns
names.shape

# %%
# disply first 5 rows
names.head()

# %%
# get column names
names.columns

# %%
# count similar items by year
names.year.value_counts()

# %%
# QUESTION 1
# PLOT FOR THE NAME THROUGH THE YEARS
# HOW DOES YOUR NAME AT YOUR BIRTH YEAR COMPARE TO ITS USE HISTORICALLY
# Analysis ideas:
# - Did your name have a surge in popularity around your birth year?
# - How does it compare to historical trends?

# create dataframe only for "Matthew" name
matthew_data = names.query('name == "Matthew"')
matthew_data

# %%
STARTING_YEAR = 1910
BORN_YEAR = 1993

# convert 'year' column to datetime data type
matthew_data["year"] = pd.to_datetime(matthew_data["year"], format="%Y")

# filter the data, only include data points from the starting year and higher
filtered_data = matthew_data[matthew_data["year"] >= str(STARTING_YEAR)]

# select year was born
birth_year_filter = filtered_data[filtered_data["year"] == str(BORN_YEAR)]

# create chart of name through the years
through_years_chart = (
    alt.Chart(filtered_data).encode(x=alt.X("year:T"), y=alt.Y("Total")).mark_line()
)

# create a chart for the birth year 1993
year_point = (
    alt.Chart(birth_year_filter)
    .mark_circle()
    .encode(x=alt.X("year:T"), y=alt.Y("Total"), color=alt.value("red"))
    .properties(title="Matthew names through the years")
)

matthew_year_chart = through_years_chart + year_point

matthew_year_chart

# %%
# QUESTION 2
# "IF YOU TALKED TO SOMEONE NAMED BRITTANY ON THE PHONE, WHAT IS YOUR
#   GUESS OF HIS OR HER AGE? WHAT AGES WOULD YOU NOT GUESS?"
brittany_data = names.query('name == "Brittany"')
brittany_data

# %%
# get current age and insert a new column in the dataset
current_year = datetime.datetime.now().year
brittany_data["currentAge"] = current_year - brittany_data["year"]
brittany_data

# %%
# create brittany chart
# Create the Altair chart
chart = (
    alt.Chart(brittany_data)
    .mark_circle()
    .encode(
        x=alt.X(
            "currentAge:Q", axis=alt.Axis(title="Current Age (years)", format="d")
        ),  # Customize X-axis
        y=alt.Y("Total:Q", axis=alt.Axis(title="Total")),
    )
    .properties(title="Brittany's ages in the US")
)

chart

# %%
# QUESTION 3
# MARY, MARTHA, PETER, AND PAUL ARE ALL CHRISTIAN NAMES. FROM 1920 - 2000,
#  COMPARE THE NAME USAGE OF EACH OF THE FOUR NAMES. WHAT TRENDS DO YOU NOTICE

# create copy of the data with specified names and year range
list_names = ["Mary", "Martha", "Peter", "Paul"]
christian_names = names.query(f"name in {list_names}")
christian_names_data = christian_names.query("year >= 1920 and year <= 2000")
christian_names_data

chart = (
    alt.Chart(christian_names_data)
    .mark_line()
    .encode(
        x=alt.X(
            "year:T", axis=alt.Axis(title="Year")
        ),  # Specify the x-axis as time-based with a title
        y=alt.Y("total:Q", axis=alt.Axis(title="Name Count")),
        color="name:N",  # Color by the name column
        tooltip=["year", "name", "Total"],
    )
    .properties(
        title="Comparison of Christian Names (1920 - 2000)",
        # width=600,  # Adjust the chart width as needed
        # height=400  # Adjust the chart height as needed
    )
    .interactive()
)

# Add a legend for name colors
chart = chart.encode(color=alt.Color("name:N", legend=alt.Legend(title="Names")))

chart

# QUESTION 4
# THINK OF A UNIQUE NAME FROM A FAMOUS MOVIE. PLOT THE USAGE OF THAT NAME AND
#  SEE HOW CHANGES LINE UP WITH THE MOVIE RELEASE. DOES IT LOOK LIKE THE MOVIE
#  HAD AN EFFECT ON USAGE?

# %%
