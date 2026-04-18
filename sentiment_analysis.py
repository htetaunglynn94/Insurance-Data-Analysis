from textblob import TextBlob
import pandas as pd

# Clean column names (important for Power BI)
dataset.columns = dataset.columns.str.strip()

# Calculate polarity (-1 to +1)
dataset['Polarity'] = dataset['Feedback'].apply(
    lambda x: TextBlob(str(x)).sentiment.polarity
)

# Convert to positive satisfaction score (0 to 1)
dataset['Satisfaction Score'] = dataset['Polarity'].apply(
    lambda x: round((x + 1) / 2, 4)
)

dataset