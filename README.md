## BeliEVe
"Believe you can and you're halfway there." - Theodore Roosevelt 

Have you ever wondered what the population of vehicles might look like in the future?
Well, look no further. BeliEVe does the magic for you!

## What does it do?
BeliEVe relies on the good old random forest model to train over data from 2019 to 2024 (based in California) to predict the vehicle population in 2025. 

## How we built it
We built our model in three stages:

**Pre-Processing**
- Check for NaN values within the dataset, and we used MICE imputation to fill in the missing data
- Changed data types of certain columns that had mismatched

**Feature Engineering**
- Used Correlation Matrix and Random Forest Feature Importance to single out key features that strengthen the correlation

**Visualize**
- Visualised key metrics and impactful insights from the dataset to reinforce market trends for cars for both gas or Electric Operated Vehicles.

**Training the model**
- Scaled the model using log transform during training and brought back the original value by transforming it back to exponential and compared RMSE with testing results.

Here are the benchmarks for the models

| Model          | RMSE                        | R²                          |
|----------------|-----------------------------|-----------------------------|
| Decision Tree | 10414.96                | 0.7138                  |
| **Random Forest**  | **9458.02**                     | **0.7639**                      |
| XGBoost        | 9825.53                     | 0.7452                      |


