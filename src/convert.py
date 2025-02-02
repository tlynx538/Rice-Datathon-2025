import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

def clean_encode_columns(df):
    # Drop Region
    df = df.drop(['Region'],axis=1)
    # Type Cast Model Year
    df['Model Year'] = df['Model Year'].astype('Int64')
    
    # Allocate GVWR based on categories
    gvwr_map = {
    '1': 'Light-Duty',
    '2': 'Light-Duty',
    '3': 'Medium-Duty',
    '4': 'Medium-Duty',
    '5': 'Medium-Duty',
    '6': 'Medium-Duty',
    '7': 'Heavy-Duty',
    '8': 'Heavy-Duty',
    'Not Applicable': 'Not Applicable',
    'Unknown': 'Unknown'
    }

    df['GVWR Group'] = df['GVWR Class'].map(gvwr_map)
    df = pd.get_dummies(df, columns=['GVWR Group'], prefix='GVWR')
    
    # Define mappings for ordinal encoding
    mile_range_mapping = {
        'Not Applicable': 0,
        '0 to 50 miles': 1,
        '51 to 100 miles': 2,
        '101 to 150 miles': 3,
        '>150 miles': 4,
        'Unknown': -1
    }
    
    vehicle_count_mapping = {
        '1': 1,
        '2': 2,
        '3': 3,
        '≥4': 4,
        'Unknown': -1
    }
    
    # Apply ordinal encoding
    df['Electric Mile Range'] = df['Electric Mile Range'].map(mile_range_mapping)
    df['Number of Vehicles Registered at the Same Address'] = df['Number of Vehicles Registered at the Same Address'].map(vehicle_count_mapping)
    df = pd.get_dummies(df, columns=['Vehicle Category', 'Fuel Type', 'Fuel Technology'], drop_first=True)
    df = df.drop(['GVWR Class'],axis=1)
    return df

def impute_df(df):
    imputer = IterativeImputer(random_state=100, max_iter=10)
    imputer.fit(df)
    df_imputed = imputer.transform(df)
    df_ = pd.DataFrame(df_imputed)
    df_.columns = df.columns 
    return df_

def fill_missing_columns(X,scoring_X):
    missing_columns = set(X.columns) - set(scoring_X.columns)
    # Add missing columns to scoring_X with default value (e.g., False)
    for col in missing_columns:
        scoring_X[col] = False  # Use 0 if numerical, or False for boolean

    # Ensure column order matches between X and scoring_X
    scoring_X = scoring_X[X.columns]
    return scoring_X
    
    