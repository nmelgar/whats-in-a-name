# %%
# package import
import pandas as pd
import altair as alt
import numpy as np
from scipy import stats

# %%
# data source
names_url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(names_url)

# %%
# rows and columns
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
# create dataframe only for "Matthew" name
matthew_data = names.query('name == "Matthew"')
matthew_data

# %%
# QUESTION 1
# PLOT FOR THE NAME THROUGH THE YEARS
# HOW DOES YOUR NAME AT YOUR BIRTH YEAR COMPARE TO ITS USE HISTORICALLY
# Analysis ideas:
# - Did your name have a surge in popularity around your birth year? 
# - How does it compare to historical trends?

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
    alt.Chart(filtered_data).encode(x=alt.X("year:T"), y=alt.Y("Total")).mark_circle()
)

# create a cgart for the birth year 1993
year_point = (
    alt.Chart(birth_year_filter)
    .mark_circle()
    .encode(x=alt.X("year:T"), y=alt.Y("Total"), color=alt.value("red"))
)

final_chart = through_years_chart + year_point

final_chart

# %%
# QUESTION 2
# "IF YOU TALKED TO SOMEONE NAMED BRITTANY ON THE PHONE, WHAT IS YOUR 
#   GUESS OF HIS OR HER AGE? WHAT AGES WOULD YOU NOT GUESS?"
brittany_data = names.query('name == "Brittany"')
brittany_data


# QUESTION 3
# MARY, MARTHA, PETER, AND PAUL ARE ALL CHRISTIAN NAMES. FROM 1920 - 2000, 
#  COMPARE THE NAME USAGE OF EACH OF THE FOUR NAMES. WHAT TRENDS DO YOU NOTICE


# QUESTION 4
# THINK OF A UNIQUE NAME FROM A FAMOUS MOVIE. PLOT THE USAGE OF THAT NAME AND 
#  SEE HOW CHANGES LINE UP WITH THE MOVIE RELEASE. DOES IT LOOK LIKE THE MOVIE 
#  HAD AN EFFECT ON USAGE?

# %%
