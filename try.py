# %%
# package import
import pandas as pd
import plotly.express as px
import numpy as np
from scipy import stats
import datetime

# %%
# data source
names_url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(names_url)

# %%
# count similar items by year
names.year.value_counts()

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

# name chart through the years
mat_chart = px.line(
    matthew_data,
    x="year",
    y="Total",
    title="Matthew name through the years",
)

mat_chart.show()

year_chart = px.scatter(born_year_data, x="year", y="Total")
year_chart.show()