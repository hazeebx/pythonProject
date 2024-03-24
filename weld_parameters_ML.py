import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import pandas as pd

# Read the dataset from the CSV file
data = pd.read_csv('welding_data.csv')

# Extract features (X) and target variables (y)
X = data[['Current', 'Voltage', 'Speed', 'Angle']].values
y_depth = data['Depth'].values
y_reinforcement = data['Reinforcement'].values
y_bead_height = data['Height'].values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_depth, test_size=0.2, random_state=42)


# Initialize and train the Random Forest Regression model
model_depth = RandomForestRegressor()
model_depth.fit(X_train, y_train)

# Predict the depth of penetration for a new current value of 97
new_current = np.array([[97, 30, 90, 20]])  # Assuming other features remain constant
depth_prediction = model_depth.predict(new_current)
print("Predicted Depth of Penetration:", depth_prediction)

# Evaluate model performance
y_pred = model_depth.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)

# Plotting the initial values
plt.figure(figsize=(10, 6))

# Plotting depth of penetration
plt.plot(X[:, 0], y_depth, color='blue', marker='o', label='Depth of Penetration')

# Plotting reinforcement height
plt.plot(X[:, 0], y_reinforcement, color='green', marker='s', label='Reinforcement Height')

# Plotting weld bead height
plt.plot(X[:, 0], y_bead_height, color='red', marker='^', label='Weld Bead Height')

# Plotting the new current value
plt.scatter(new_current[0][0], depth_prediction, color='orange', label='New Current Value (97)', marker='x')

plt.xlabel('Welding Current (A)')
plt.ylabel('Depth/Height (mm)')
plt.title('Relationship between Welding Current and Depth/Height')
plt.legend()
plt.grid(True)
plt.show()
