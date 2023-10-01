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
# names.shape

# %%
# disply first 5 rows
# names.head()

# %%
# get column names
# names.columns

# %%
# count similar items by year
# names.year.value_counts()

# %%
# QUESTION 1
# PLOT FOR THE NAME THROUGH THE YEARS
# HOW DOES YOUR NAME AT YOUR BIRTH YEAR COMPARE TO ITS USE HISTORICALLY
# Analysis ideas:
# - Did your name have a surge in popularity around your birth year?
# - How does it compare to historical trends?

# create dataframe only for "Matthew" name
matthew_data = names.query('name == "Matthew"')

# filter data
person_name = "Matthew"
year_range = "year >= 1910 and year <= 2015"
matthew_data = names.query(f"name == '{person_name}' and {year_range}")

# create matthew chart
matthew_chart = (
    alt.Chart(matthew_data)
    .encode(x=alt.X("year"), y=alt.Y("Total"), color=alt.value("blue"))
    .mark_line()
    .properties(title="Matthew name through the years")
)

# create a chart for the birth year 1993
born_year = 1993
born_year_data = names.query(f"year == {born_year} and name == 'Matthew'")

year_chart = (
    alt.Chart(born_year_data)
    .encode(x=alt.X("year"), y=alt.Y("Total"), color=alt.value("red"))
    .mark_circle()
)

matthew_final_chart = matthew_chart + year_chart

matthew_final_chart


# %%
# QUESTION 2
# "IF YOU TALKED TO SOMEONE NAMED BRITTANY ON THE PHONE, WHAT IS YOUR
#   GUESS OF HIS OR HER AGE? WHAT AGES WOULD YOU NOT GUESS?"

# get data and filter it by name and then by year
brittany_data = names.query('name == "Brittany"')
current_year = datetime.datetime.now().year

# create a copy of the data to avoid the SettingWithCopyWarning:
brittany_data_copy = brittany_data.copy()

brittany_data_copy["currentAge"] = current_year - brittany_data_copy["year"]

# create brittany chart
britanny_chart = (
    alt.Chart(brittany_data_copy)
    .mark_circle()
    .encode(
        x=alt.X(
            "currentAge:Q", axis=alt.Axis(title="Current Age (years)", format="d")
        ),  # Customize X-axis
        y=alt.Y("Total:Q", axis=alt.Axis(title="Total")),
    )
    .properties(title="Brittany's ages in the US")
)

britanny_chart


# %%
# QUESTION 3
# MARY, MARTHA, PETER, AND PAUL ARE ALL CHRISTIAN NAMES. FROM 1920 - 2000,
#  COMPARE THE NAME USAGE OF EACH OF THE FOUR NAMES. WHAT TRENDS DO YOU NOTICE

# create copy of the data with specified names and year range
list_names = ["Mary", "Martha", "Peter", "Paul"]
year_names = "year >= 1920 and year <= 2000"
christian_names_data = names.query(f"name in {list_names} and {year_names}")

# create chart to display names between 1920 and 2000
christian_names_chart = (
    alt.Chart(christian_names_data)
    .encode(x=alt.X("year"), y=alt.Y("Total"), color=alt.Color("name"))
    .transform_loess("year", "Total", groupby=["name"])
    .mark_line()
    .properties(title="Christian Names Between 1920-2000")
)
# .interactive()
christian_names_chart


# %%
# QUESTION 4
# THINK OF A UNIQUE NAME FROM A FAMOUS MOVIE. PLOT THE USAGE OF THAT NAME AND
#  SEE HOW CHANGES LINE UP WITH THE MOVIE RELEASE. DOES IT LOOK LIKE THE MOVIE
#  HAD AN EFFECT ON USAGE?
movie_name = "Luke"
year_range = "year >= 1960 and year <= 1990"
movie_name_data = names.query(f"name == '{movie_name}' and {year_range}")

luke_name_chart = (
    alt.Chart(movie_name_data)
    .encode(x=alt.X("year"), y=alt.Y("Total"), color=alt.value("green"))
    .mark_line()
    .properties(title="Luke Skywalker impact")
)

# create chart to display movies released data, movies iv, v and vi
movie_release_year = [1977, 1980, 1983]
movie_release_data = names.query(f"year in {movie_release_year} and name == 'Luke'")

year_chart = (
    alt.Chart(movie_release_data)
    .encode(x=alt.X("year"), y=alt.Y("Total"), color=alt.value("red"))
    .mark_circle()
)

luke_chart = luke_name_chart + year_chart

luke_chart

# %%
