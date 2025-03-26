import pandas as pd
from io import StringIO

# Sample dataset as a multi-line string
data = """Customer_ID,Account_Balance,Transaction_Amount,Reported_Amount,Currency,Country,Transaction_Date,Risk_Score
1001,15000,500,500,USD,US,2025-02-25,3
1002,32000,1200,1200,EUR,DE,2025-02-20,2
1003,-5000,300,300,GBP,UK,2025-02-18,6
1004,70000,2000,1800,USD,US,2025-02-28,5"""

# Read the dataset into a DataFrame
df = pd.read_csv(StringIO(data))

# Filter rows where Risk_Score > 3 and Account_Balance > 0
filtered_df = df[(df['Risk_Score'] > 3) & (df['Account_Balance'] > 0)]

# Display the filtered DataFrame
print(filtered_df)