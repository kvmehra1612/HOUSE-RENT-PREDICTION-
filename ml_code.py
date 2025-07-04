# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load the dataset
df = pd.read_csv('house_rent_dataset_with_20_nulls.csv')

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Drop rows with null values (you can also use fillna() if preferred)
df = df.dropna()

#Plotting histogram of Area
plt.hist(df['Area (sqft)'], bins=10, edgecolor='black')
plt.title('Area Distribution')
plt.xlabel('Area (sqft)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('area_distribution.png')
plt.show()

# Checking correlation between columns using heatmap
sns.heatmap(df.corr(), annot=True, cmap='YlGnBu')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.show()

# Splitting data into inputs (X) and output (y)
X = df[['Area (sqft)', 'BHK']]
y = df['Rent (₹)']

# Splitting into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Making and training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting rents for test data
y_pred = model.predict(X_test)

dataframe_clean = dataframe.dropna()
dataframe_sample = dataframe_clean.sample(30, random_state=42)

plt.figure(figsize=(8, 6))
plt.scatter(df_sample['Area (sqft)'], df_sample['Rent (₹)'],
            color='royalblue', s=80, edgecolor='black')
plt.title('Area vs Rent (Clear View with Fewer Points)')
plt.xlabel('Area (sqft)')
plt.ylabel('Rent (₹)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Checking model accuracy using MAE
mae = mean_absolute_error(y_test, y_pred)
print('Mean Absolute Error:', round(mae, 2))

# --- New Prediction Section: Bar graph for 8 new inputs ---
new_data = pd.DataFrame({
    'Area (sqft)': [600, 900, 1100, 1300, 1600, 2000, 2500, 3000],
    'BHK':         [1,   2,   2,    3,    3,    4,    4,    5]
})
new_predictions = model.predict(new_data)

# Plotting the bar graph
plt.figure(figsize=(7, 5))
labels = [f"{a} sqft / {b}BHK" for a, b in zip(new_data['Area (sqft)'], new_data['BHK'])]
plt.bar(labels, new_predictions, color='skyblue')
plt.title("Predicted Rent for Sample House Inputs")
plt.xlabel("House (Area/BHK)")
plt.ylabel("Predicted Rent (₹)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('predicted_rent_bar_graph.png')
plt.show()
