# import packages 
import pandas as pd
import numpy as np

# read in data
nfl_data = pd.read_csv("../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv")
sf_permits = pd.read_csv("../input/building-permit-applications-data/Building_Permits.csv")

# set seed for reproducibility
np.random.seed(0) 

# look at a few rows of the nfl_data file. I can see a handful of missing data already
nfl_data.sample(5)
sf_permits.sample(5)

# get the number of missing data points per column
missing_values_count_nfl = nfl_data.isnull().sum()
missing_values_count_sf = sf_permits.isnull().sum()

# look at the # of missing points in the first ten columns
missing_values_count_nfl[0:10]
missing_values_count_sf[0:10]

# checking total missing values
total_cells_nfl = np.product(nfl_data.shape)
total_missing_nfl = missing_values_count_nfl.sum()

total_cells_sf = np.product(sf_permits.shape)
total_missing_sf = missing_values_count_sf.sum()


# percent of data that is missing
missingpercent_nfl = (total_missing/total_cells) * 100
missingpercent_sf = (total_missing/total_cells) * 100

##One option is to delete NA's

# could remove all the rows that contain a missing value with code below
nfl_data.dropna()
rows_with_na_dropped_nfl = nfl_data.dropna(axis=1)

sf_permits.dropna()
rows_with_na_dropped_sf = sf_permits.dropna(axis=1)


# could remove all columns with at least one missing value
columns_with_na_dropped_nfl = nfl_data.dropna(axis=1)
columns_with_na_dropped_nfl.head()

columns_with_na_dropped_sf = sf_permits.dropna(axis=1)
columns_with_na_dropped_sf.head()


# check to see just how much data we lost?
print("Columns in original dataset: %d \n" % nfl_data.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped_nfl.shape[1])
print("Rows in original dataset: %d\n" % nfl_data.shape[1])
print("Rows with na's dropped: %d" % rows_with_na_dropped_nfl.shape[1])

print("Columns in original dataset: %d \n" % sf_permits.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped_sf.shape[1])
print("Rows in original dataset: %d\n" % sf_permits.shape[1])
print("Rows with na's dropped: %d" % rows_with_na_dropped.shape[1])


##Second possibility is to replace NA's with zeros

# could replace all NA's with 0
nfl_data.fillna(0)

# replace all NA's with the value that comes directly after it in the same column, 
# then replace all the reamining na's with 0
nfl_data.fillna(method = 'bfill', axis=0).fillna("0")
sf_permits.fillna(method = 'bfill', axis = 0).fillna("0")



