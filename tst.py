import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Generate network packet data and write to CSV file
np.random.seed(0)
data = np.random.rand(200, 4)
df = pd.DataFrame(data)
df.to_csv('network_data.csv', index=False, header=False)

# Step 2: Calculate the correlation matrix
df = pd.read_csv('network_data.csv', header=None)

correlation_matrix = np.corrcoef(df.values, rowvar=False)

# Step 3: Plot and save the correlation matrix to PDF
sns.set(style="white")
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', xticklabels=df.columns, yticklabels=df.columns)
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.pdf')
plt.close()

# Step 4: Find the highest correlation and save the names of the two features
max_corr = np.max(correlation_matrix)
max_corr_indices = np.unravel_index(np.argmax(correlation_matrix), correlation_matrix.shape)
max_corr_features = [df.columns[max_corr_indices[0]], df.columns[max_corr_indices[1]]]

# Step 5: Save the names of the features with highest correlation to PDF
with open('highest_correlation.pdf', 'w') as f:
    f.write(f"Features with highest correlation: {max_corr_features[0]} and {max_corr_features[1]}")

print("Files generated successfully.")
