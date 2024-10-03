# importing modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading the raw data collected using light sensor from CSV file using Pandas library
data = pd.read_csv("RawData1.csv")

# Plotting the raw data 
plt.plot(data['Time(s)'], data['Illuminance(lx)'], label = "Raw Data")
plt.legend()
plt.xlabel("Time(s)")
plt.ylabel("Illuminance(lx)")
plt.show()


# The code will smooth the data by averaging every 5 consecutive values in the dataset
window_size = 5

# This function applies a convolution, commonly used for smoothing data
# "np.ones(window_size) / window_size": This creates an array of ones with a length equal to window_size, then divides each element by window_size, effectively creating a moving average filter.
smoothed_data = np.convolve(data['Illuminance(lx)'], np.ones(window_size) / window_size, mode='valid')

# Plotting the smoothed data using Matplotlib library
plt.plot(data['Time(s)'][window_size-1:], smoothed_data, label="Smoothed Data")
plt.legend()
plt.xlabel("Time(s)")
plt.ylabel("Illuminance(lx)")
plt.show()


# Diving the smoothed data into a fixed number of time intervals
interval_number = 10
data_one_interval = len(smoothed_data) // 10

# Calculate the slope of each time interval and store the values in the 'slopes' array
slopes = []

for i in range(interval_number):
    
    # Getting index of x and y to calculate slope
    start_index = i * data_one_interval
    end_index = (i + 1) * data_one_interval

    # Check if reaching the end of smoothed_data
    if end_index > len(smoothed_data):
        end_index = len(smoothed_data) - 1  

    y1 = smoothed_data[start_index]
    y2 = smoothed_data[end_index]
    x1 = data['Time(s)'][window_size-1 + start_index]
    x2 = data['Time(s)'][window_size-1 + end_index]

    # Calculating slopes and storing them in array
    slope = (y2 - y1) / (x2 - x1)
    slopes.append(slope)

# Setting conditions based on the slope value and display corresponding message
for i in range(0,len(slopes)):
    # Print message depending on condition of slope
    if slopes[i] < -1:
        print(f"Interval {i+1}: Object is approaching (Slope: {slopes[i]:.4f})")
    elif slopes[i] > 1:
        print(f"Interval {i+1}: Object is moving away (Slope: {slopes[i]:.4f})")
    else:
        print(f"Interval {i+1}: No significant movement (Slope: {slopes[i]:.4f})")

# Visualize slope values by plotting them
plt.plot(slopes, "o", label = "Slopes")
plt.axhline(0, color='black', linestyle='--')
plt.legend()
plt.xlabel("Time intervals")
plt.ylabel("Slope(lx/s)")
plt.show()


        
        
        
