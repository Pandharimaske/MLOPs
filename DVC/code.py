import pandas as pd
import os

# Create a sample Dataframe with column names
data = {'Name': ['Alice' , 'Bob' , 'Charlie'] , 
        'Age': [25, 30, 35] , 
        'City': ['New York' , 'Los Angeles' , 'Chicago']
    }

df = pd.DataFrame(data)

# Ensure the "data" directory exists at he root level
dat_dir = 'DVC/data'
os.makedirs(dat_dir , exist_ok=True)

# Define the file path
file_path = os.path.join(dat_dir , 'sample_data.csv')

# Save the DataFrame to a CSV file , including column names
df.to_csv(file_path , index=False)

print(f"CSV file saved to {file_path}")
