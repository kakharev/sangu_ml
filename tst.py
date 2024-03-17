import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Generate random network packet data with headers and write to CSV file
np.random.seed(0)
num_samples = 200
num_features = 4
feature_names = ['Protocol_Type', 'Source_IP', 'Destination_IP', 'Packet_Length']

# Generate random data for each feature
data = np.random.rand(num_samples, num_features)

# Introduce correlations near 1 between specific features
data[:, 1] = data[:, 0] + np.random.normal(0, 0.05, num_samples)  # Making Source_IP highly correlated with Protocol_Type
data[:, 2] = data[:, 0] + np.random.normal(0, 0.05, num_samples)  # Making Destination_IP highly correlated with Protocol_Type

# Create DataFrame with random data and feature names
df = pd.DataFrame(data, columns=feature_names)

# Write DataFrame to CSV file
df.to_csv('network_data.csv', index=False)

# Step 2: Calculate the correlation matrix
correlation_matrix = np.corrcoef(data, rowvar=False)

# Write correlation matrix to CSV file
correlation_df = pd.DataFrame(correlation_matrix, columns=feature_names, index=feature_names)
correlation_df.to_csv('correlation_data.csv', index=True)

# Step 3: Plot correlation matrix as heatmap and save to PDF
sns.set(style="white")
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, xticklabels=feature_names, yticklabels=feature_names)
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.pdf')
plt.close()

print("ყველა ფაილი წარმატებით დაგენენირდა. მოიძეთ ფაილები პროექტის ფოლდერში")
