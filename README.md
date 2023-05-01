# nba_playoff_predictions_22_23
building predictor for upcoming NBA playoffs based on historical NBA reg season data and playoff results

data: used BeautifulSoup and Selenium to scrape NBA.com; manually got csv playoff result data from basketball-reference

data/ folder: contains data scraped from NBA.com; data is gathered on a season by season basis for a specific type of data. For example, one type of data was statistics regarding how teams performed in clutch time; a different type of data gathered was how a team's opponents generally performed on a per game basis. Once data was gathered for each season since 2000, I aggregated the data per year so that the multiple datasets per year were combined into a single dataset corresponding to that year. These datasets were titled in the following manner: YYYY-YY_data.csv Then, from basketball reference, I found a csv file with data playoff series results. After reformatting that slightly, I looped thru each series since the 2001 playoffs, retrieved the regular season data during that year for each of the teams competing in the series (which I already had) and aggregated the result of the series and regular season data for the teams into a single vector. 

data_v1.csv is the collection of these vectors as rows. 

data_v2.csv removes redundant columns and renames some columns. 

data_v3.csv renames some other columns 

data_v4.csv removes some unneeded columns

data_v5.csv change: win percentage cols were written in decimal form; converted them to percentage form

augmented_data_v5.csv artificially increases size of dataset

x_train.csv, x_test.csv, y_train.csv, y_test.csv: train/test split on v5 followed by select 25 best features according to MI score

x_train_v2.csv, x_test_v2.csv, y_train_v2.csv, y_test_v2.csv: train/test split on v5 followed by select 25 best features according to MI score but also include the other team's corresponding feature (ie: include both  t1 and t2 versions of feature)

data_v6.csv: starts with v5, and subtracts corresponding columns between t1 and t2 to reduce column size by half and creates 'differential' columns

data_v5_22_23.csv: 2023 playoffs test data (state of data corresponds to round); ordering of columns should match training data

data_v7.csv: includes original data and synthetic data produced by GMMs