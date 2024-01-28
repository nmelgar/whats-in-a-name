# %%
# package import
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from scipy import stats
import datetime

# %%
# data source
names_url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(names_url)

# %%
# count similar items by year
# names.year.value_counts()

# %%
# # QUESTION 1
# # PLOT FOR THE NAME THROUGH THE YEARS
# # HOW DOES YOUR NAME AT YOUR BIRTH YEAR COMPARE TO ITS USE HISTORICALLY
# # Analysis ideas:
# # - Did your name have a surge in popularity around your birth year?
# # - How does it compare to historical trends?

# # create dataframe only for "Matthew" name
matthew_data = names.query('name == "Matthew"')

# filter data
person_name = "Matthew"
year_range = "year >= 1910 and year <= 2015"
matthew_data = names.query(f"name == '{person_name}' and {year_range}")

# specific year for his born
born_year = 1993
born_year_data = matthew_data.query(f"year == {born_year}")
specific_year = born_year_data["year"].values
totals_specific_year = born_year_data["Total"].values


# name chart through the years
mat_chart = px.line(
    matthew_data,
    x="year",
    y="Total",
    labels={"year": "Year"},
    title="Matthew name through the years",
)
mat_chart.add_trace(
    go.Scatter(
        x=specific_year,
        y=totals_specific_year,
        mode="markers",
        marker_size=5,
        name="1993",
    )
)
#### https://stackoverflow.com/questions/70275607/how-to-highlight-a-single-data-point-on-a-scatter-plot-using-plotly-express
mat_chart.show()

# year_chart = px.scatter(born_year_data, x="year", y="Total")
# year_chart.show()

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

brittany_chart = px.scatter(
    brittany_data_copy,
    x="currentAge",
    y="Total",
    labels={
        "currentAge": "Current Age",
    },
    title="Brittany's ages in the US",
)
brittany_chart.show()

# %%
# QUESTION 3
# MARY, MARTHA, PETER, AND PAUL ARE ALL CHRISTIAN NAMES. FROM 1920 - 2000,
#  COMPARE THE NAME USAGE OF EACH OF THE FOUR NAMES. WHAT TRENDS DO YOU NOTICE

# create copy of the data with specified names and year range
list_names = ["Mary", "Martha", "Peter", "Paul"]
year_names = "year >= 1920 and year <= 2000"
christian_names_data = names.query(f"name in @list_names and {year_names}")

# create chart to display names between 1920 and 2000
christian_names_chart = px.line(
    christian_names_data,
    x="year",
    y="Total",
    color="name",
    labels={
        "year": "Year",
        "name": "Name",
    },
    title="Christian Names Between 1920-2000",
)
christian_names_chart.show()

# %%
# QUESTION 4
# THINK OF A UNIQUE NAME FROM A FAMOUS MOVIE. PLOT THE USAGE OF THAT NAME AND
#  SEE HOW CHANGES LINE UP WITH THE MOVIE RELEASE. DOES IT LOOK LIKE THE MOVIE
#  HAD AN EFFECT ON USAGE?

# choose name, and year range for the star wars movies
movie_name = "Luke"
year_range = "year >= 1960 and year <= 1990"
movie_name_data = names.query(f"name == '{movie_name}' and {year_range}")

luke_name_chart = px.line(
    movie_name_data,
    x="year",
    y="Total",
    labels={"year": "Year"},
    title="Luke Skywalker impact on names of the people",
)

luke_name_chart.show()

# data to display movies released data, movies iv, v and vi
movie_release_year = [1977, 1980, 1983]
movie_release_data = names.query(
    f"year in @movie_release_year and name == '{movie_name}'"
)

totals_movie_year = movie_release_data["Total"].values

luke_name_chart.add_trace(
    go.Scatter(
        x=movie_release_year,
        y=totals_movie_year,
        mode="markers",
        marker_size=8,
        marker_symbol="star",
        marker_color="red",
        name="Years when Star Wars movies where released (IV - VI)",
    )
)

luke_name_chart.update_layout(
    legend=dict(
        orientation="h",  # change layout to horizontal
        yanchor="bottom",  # move to the bottom part of the plot
        y=-0.4,  # select the postion below the plot
    )
)
luke_name_chart.show()
