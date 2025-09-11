"""
This script generates the dataset which is used by the app. The final structure of the data looks like:
(State, Year, Total Population, Median Household Income)

Data comes from the American Community Survey 1-year Estimates, and is retrieved from the US Census Bureau's
API via the censusdis package.
"""

from censusdis.datasets import ACS1
from censusdis.multiyear import download_multiyear

census_vars = {
    "NAME": "State",
    "B01001_001E": "Total Population",
    "B19013_001E": "Median Household Income",
}

# Note that data was not published in 2020 due to Covid-19.
# See https://www.census.gov/programs-surveys/acs/data/experimental-data.html
years = [year for year in range(2005, 2024) if year != 2020]
df = download_multiyear(
    dataset=ACS1,
    vintages=years,
    download_variables=census_vars.keys(),
    state="*",
    rename_vars=False,
    prompt=False,
)
df = df.rename(columns=census_vars)

# Reorder columns
cols = df.columns.tolist()
new_order = ["State", "Year"] + [col for col in cols if col not in ["State", "Year"]]
df = df[new_order]

# Sort values and write to disk
df = df.sort_values(["State", "Year"])
df.to_csv("state_data.csv", index=False)
