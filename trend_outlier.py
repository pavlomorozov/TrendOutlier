import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # Or use 'Qt5Agg' or another supported backend

y = [11, 13, 12, 14, 16, 15, 16, 19, 17, 7, 21, 19, 23, 22, 21, 27]

def calculate_outliers(y):
    x = list(range(0, len(y)))
    # Calculate linear regression with Numpy
    regression_model = np.poly1d(np.polyfit(x, y, 1))
    trend = regression_model(x)
    print(f'trend: {trend}')

    # Calculate residuals
    y_np = np.array(y)
    residuals = y_np - trend
    trend_std_residuals = np.std(residuals)
    # Threshold for unusual deviation (e.g., 3σ)
    threshold = 3 * trend_std_residuals
    print(f'threshold: {threshold}')
    # Outliers calculated on aligned_y
    outliers = []
    for i in range(len(y)):
        data_value = y[i]
        trend_value = trend[i]
        if data_value is not None:
            residual = abs(data_value - trend_value)
            if residual > threshold:
                outliers.append(True)
            else:
                outliers.append(False)
        else:
            outliers.append(None)
    print(f'outliers: {outliers}')
    return trend, outliers

def plot(y, trend, outliers):
    x = list(range(0, len(y)))
    plt.figure()
    # showing the plot with input time series and linear regression line
    plt.title('Trend and outliers')

    # Filter data for non-outliers
    non_outliers_x = [x[i] for i in range(len(x)) if not outliers[i]]
    non_outliers_y = [y[i] for i in range(len(y)) if not outliers[i]]
    # Filter data for outliers
    outliers_x = [x[i] for i in range(len(x)) if outliers[i]]
    outliers_y = [y[i] for i in range(len(y)) if outliers[i]]

    plt.scatter(non_outliers_x, non_outliers_y, color='blue', label='Non-Outliers', marker='+', s=100)
    plt.scatter(outliers_x, outliers_y, color='red', label='Outliers', marker='x', s=100)

    # plots the line calculated with linear regression
    plt.plot(x, trend, color='blue')
    plt.show()


trend, outliers = calculate_outliers(y)
plot(y, trend, outliers)