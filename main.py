# %%
# package import
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime

# %%
# data source
names_url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(names_url)

# %%
# # QUESTION 1
# create dataframe only for "Matthew" name
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

# create matthew line chart through the years
mat_chart = px.line(
    matthew_data,
    x="year",
    y="Total",
    labels={"year": "Year"},
    title="Matthew name through the years",
)

# add mark to highligth the year when he was born
mat_chart.add_trace(
    go.Scatter(
        x=specific_year,
        y=totals_specific_year,
        mode="markers",
        marker_size=5,
        name="1993",
    )
)
mat_chart.show()

# %%
# QUESTION 2
# get data and filter it by name
brittany_data = names.query('name == "Brittany"')
current_year = datetime.datetime.now().year

# create a copy of the data to avoid the SettingWithCopyWarning:
brittany_data_copy = brittany_data.copy()
brittany_data_copy["currentAge"] = current_year - brittany_data_copy["year"]

# create brittany scatter
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
# create copy of the data with specified names and year range
list_names = ["Mary", "Martha", "Peter", "Paul"]
year_names = "year >= 1920 and year <= 2000"
christian_names_data = names.query(f"name in @list_names and {year_names}")

# create line chart to display names between 1920 and 2000
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
# choose name, and year range for the star wars movies, "luke" as the name
movie_name = "Luke"
year_range = "year >= 1960 and year <= 1990"
movie_name_data = names.query(f"name == '{movie_name}' and {year_range}")

# create line chart for luke name through the years
luke_name_chart = px.line(
    movie_name_data,
    x="year",
    y="Total",
    labels={"year": "Year"},
    title="Luke Skywalker impact on names of the people",
)

# data to display movies released data, movies iv, v and vi
movie_release_year = [1977, 1980, 1983]
movie_release_data = names.query(
    f"year in @movie_release_year and name == '{movie_name}'"
)
totals_movie_year = movie_release_data["Total"].values

# add markers for the years when the moview IV to VI were released
luke_name_chart.add_trace(
    go.Scatter(
        x=movie_release_year,
        y=totals_movie_year,
        mode="markers",
        marker_size=8,
        marker_symbol="star",
        marker_color="red",
        name="Years when Star Wars movies were released (IV - VI)",
    )
)
# change the layout so the legend show at bottom of the plot
luke_name_chart.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.4,
    )
)
luke_name_chart.show()

# %%
# # STRETCH QUESTION
# choose name, and year range for Elliot's name
movie_name = "Elliot"
year_range = "year >= 1950 and year <= 2015"
elliot_data = names.query(f"name == '{movie_name}' and {year_range}")

# create line chart for Elliot's name through the years
elliot_chart = px.line(
    elliot_data,
    x="year",
    y="Total",
    color="name",
    labels={"year": "Year"},
    title="Elliot...What?",
)

# data to display movies released data, 1st , 2nd and 3rd
elliot_selected_years_text = {
    1982: "E.T. Released",
    1985: "Second Released",
    2002: "Third Released",
}
elliot_selected_data = names.query(
    f"year in @movie_release_year and name == '{movie_name}'"
)
totals_movie_year = elliot_selected_data["Total"].values

# add vertical lines for the years when the movies were released
vlines_loop_count = 0
selected_years_count = len(elliot_selected_years_text)
annotation_position_list = ["top left", "top right", "top right"]

while vlines_loop_count <= selected_years_count:
    i = 0
    for year, text in elliot_selected_years_text.items():
        # https://plotly.com/python/horizontal-vertical-shapes/
        elliot_chart.add_vline(
            x=year,
            line_width=1,
            line_dash="dash",
            line_color="red",
            annotation_text=text,
            annotation_position=f"{annotation_position_list[i]}",
        )
        vlines_loop_count += 1
        i += 1
        
elliot_chart.show()