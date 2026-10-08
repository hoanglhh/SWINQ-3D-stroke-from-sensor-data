import pandas as pd

# 1. Load the CSV file
df = pd.read_csv('aetekni.csv')

# 2. Keep only columns before 'ball_speed'
col_index = df.columns.get_loc('ball_speed')
df_trimmed = df.iloc[:, :col_index]

# 3. Save the result back to a CSV file
df_trimmed.to_csv('aetekni_trimmed.csv', index=False)