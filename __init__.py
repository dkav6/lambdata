"""
lambdata - a collection of data science helper functions
"""

import pandas as pd
import numpy as np

# Check a dataframe for nulls
def check_nulls(df):
    print("Missing values:", df.isna().sum())

# Visualize a confusion matrix
def conf_matrix(y_true, y_pred):
    import matplotlib.pyplot as plt
    from sklearn.metrics import confusion_matrix
    conf = confusion_matrix(y_true, y_pred)
    plt.imshow(conf, cmap='binary', interpolation='None')
    plt.show()

# Train/validate/test split
def split(df):
    train, validate, test = np.split(df.sample(frac=1), [int(.6*len(df)), int(.8    *len(df))])

# Take two dataframes and make more rows
def gen_data(df1, df2):
    samp1 = df1.sample(100)
    samp2 = df2.sample(100)

# Contigency table and chi-squared
def cont_table(pdSeries1, pdSeries2):
    return pd.crosstab(pdSeries1, pdSeries2, margins=False)
    # chi squared
    from sklearn.feature_selection import chi2
    return chi2(pdSeries1, pdSeries2)

# Split addresses into multiple columns
def split_addr(series):
    regex = r'(?P<City>[^,]+)\s*,\s*(?P<State>[^\s]+)\s+(?P<Zip>\S+)'
    return series.str.extract(regex)

# State abbreviation mappings
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PRICO',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'Washington DC': 'DC',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
def state_abbrev(df):
    abbrev = {state: abbrev for abbrev, state in state_2.items()}
    full = {abbrev: state for abbrev, state in state_2.items()}
    df['abbrev'] = df['state'].map(abbrev)
    df['full'] = df['state'].map(full)
    return df['abbrev'], df['full']


# Take a list, turn into series, add it to df
def add_list_to_df(df, list):
    return df.append(pd.Series(list))
    
# 1.5* interquartile range outlier detection/removal function

# Split dates into multiple columns

# Classification and regression metrics
    
