import pandas as pd

df = pd.read_csv(r'C:\Users\patty\OneDrive\Desktop\capstone_I\Crimes_-_2001_to_Present.csv')

df.fillna(df.mean(numeric_only=True).round(1), inplace=True)

string_columns = df.select_dtypes(include=['object']).columns
df[string_columns] = df[string_columns].fillna(df[string_columns].mode().iloc[0])

df.to_csv('chicago_crimes_cleaned.csv')