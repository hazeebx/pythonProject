import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Sample dataset
#[Current, Voltage, Speed, Angle]
X = np.array([[90, 25, 40, 0],
              [90, 25, 40, 5],
              [90, 25, 40, 10],
              [90, 25, 40, 15],
              [90, 25, 40, 20],
              [95, 21, 60, 15],
              [95, 22, 60, 15],
              [95, 23, 60, 15],
              [95, 24, 60, 15],
              [95, 25, 60, 15],
              [100, 23, 40, 10],
              [100, 23, 60, 10],
              [100, 23, 80, 10],
              [90, 21, 80, 5],
              [95, 21, 80, 5],
              [100, 21, 80, 5],
              [105, 21, 80, 5],
              [110, 21, 80, 5]])
y_depth = np.array([1.01, 1.01, 1.02, 0.99, 0.98, 1.00, 0.98, 0.97, 0.96, 0.94, 0.98, 1.01, 1.05, 0.92, 0.93, 0.96, 0.99, 1.01])
y_reinforcement = np.array([2.14, 2.14, 2.15, 2.12, 2.10, 2.07, 2.08, 2.10, 2.12, 2.13, 2.18, 2.16, 2.12, 2.14, 2.12, 2.10, 2.09, 2.07])
y_bead_height = np.array([8.14, 8.13, 8.14, 8.18, 8.22, 7.20, 7.27, 7.29, 7.31, 7.32, 7.37, 7.35, 7.31, 7.26, 7.29, 7.31, 7.33, 7.36])

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
