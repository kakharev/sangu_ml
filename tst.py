import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: დავაგენერიროთ ქსელური პაკეტების ნუსხა რანდომული მონაცემებით და შევქმნათ CSV ფაილი
np.random.seed(0)
num_samples = 200
num_features = 4
feature_names = ['Protocol_Type', 'Source_IP', 'Destination_IP', 'Packet_Length']

# შევავსოთ ნუსხა თითოეული სვეტისთვის (ვგულისხმობ features)
data = np.random.rand(num_samples, num_features)

# ვიპოვოთ კორელაცია რომელიც ახლოსაა 1-თან
data[:, 1] = data[:, 0] + np.random.normal(0, 0.05, num_samples) 
data[:, 2] = data[:, 0] + np.random.normal(0, 0.05, num_samples)

# შევქმნათ DataFrame რანდომული მონაცემებით და თუთოეული ფიჩერისთვის
df = pd.DataFrame(data, columns=feature_names)

# შევინახოთ DataFrame CSV ფაილში
df.to_csv('network_data.csv', index=False)

# Step 2: გამოვთვალოთ correlation matrix
correlation_matrix = np.corrcoef(data, rowvar=False)

# შევინახოთ correlation matrix CSV ფაილში
correlation_df = pd.DataFrame(correlation_matrix, columns=feature_names, index=feature_names)
correlation_df.to_csv('correlation_data.csv', index=True)

# Step 3: დავამუშავოთ correlation matrix როგორც heatmap და შევინახოთ PDF-ში
sns.set(style="white")
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, xticklabels=feature_names, yticklabels=feature_names)
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.pdf')
plt.close()

print("ყველა ფაილი წარმატებით დაგენენირდა. მოიძეთ ფაილები პროექტის ფოლდერში")
print("აგრეთვე, დაკავშირებული ვართ github-თან და საჭიროა ფაილების დასინქრონება")
