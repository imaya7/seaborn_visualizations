import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# making sure the script works in any directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# creating os path for the csv file
csv_path = os.path.join(script_dir, "Exercise_Data.csv")

# Load the excercise data
data = pd.read_csv(csv_path)

# Extract numeric columns of the pulse data 
pulse_data = data[['1 min', '15 min', '30 min']]

# Normalize the data for heatmap visualization
normalized_data = (pulse_data - pulse_data.min()) / (pulse_data.max() - pulse_data.min())

# creating the heatmap
plt.figure(figsize=(6, 5))  # figure size 
sns.heatmap(
    normalized_data, 
    cmap='viridis',  # color
    cbar=True, 
    annot=False,  # Turn annotations off
    linewidths=0.5,  # Add gridlines 
    linecolor='white',  # Make the gridlines that was just added white 
    cbar_kws={'label': 'Normalized Pulse Rate'}  # Add title to the color bar

)
plt.title('Pulse Variability Heatmap', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Time Intervals', fontsize=12)
plt.ylabel('Observations', fontsize=12)
plt.xticks(fontsize=10, rotation=45)  # Rotate the x-axis labels = better readability
plt.yticks(fontsize=10)  # Adjust y-axis labels
plt.tight_layout()  # Adjust layout 
plt.show()

# Explaination of heat map for elementary school students
# This is a heatmap, which is like a colorful picture that shows the difference in pulse rates during different exercise activities.  
# Each row of the heatmap is represented as a person and each column is a time interval (1 min, 15 min, and 30 min) that the pulse was measured.
# The colors on the heatmap tell us how fast or how slow the heartbeats were during different times. 
# The brighter the color is the faster the heartbeats are and the darker the color is the slower the heartbeats are.
# If you look at the heatmap, you can see that the heartbeats were faster at 1 minute and then got slower at 15 minutes and 30 minutes.
# This means that when we exercise, our heart beats faster at first and then slows down as we keep exercising.
# There are a few outliers to this if you look at the heatmap, we can also see that some people's heart rates didnt change as much as others.
# This could mean they may be in better shape than the other participants or they may not be trying as hard as the other participants.



# Creating a categorical plot for pulse values by diet and type of exercise
# Create subplots for each time interval
fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)  # Share y-axis for better comparison

# color palette for green and blue
palette = sns.color_palette(["#7FC97F", "#80B1D3"])  # Light green and light blue


# Plot for '1 min'
sns.boxplot(data=data, x='kind', y='1 min', hue='diet', ax=axes[0], palette=palette)
axes[0].set_title('Pulse at 1 Minute', fontsize=14)
axes[0].set_xlabel('Type of Exercise', fontsize=12)
axes[0].set_ylabel('Pulse Rate', fontsize=12)

# Plot for '15 min'
sns.boxplot(data=data, x='kind', y='15 min', hue='diet', ax=axes[1],palette=palette)
axes[1].set_title('Pulse at 15 Minutes', fontsize=14)
axes[1].set_xlabel('Type of Exercise', fontsize=12)
axes[1].set_ylabel('')  # No y-axis label

# Plot for '30 min'
sns.boxplot(data=data, x='kind', y='30 min', hue='diet', ax=axes[2],palette=palette)
axes[2].set_title('Pulse at 30 Minutes', fontsize=14)
axes[2].set_xlabel('Type of Exercise', fontsize=12)
axes[2].set_ylabel('')  # No y-axis label 

# Adjust layout and add a title
fig.suptitle('Pulse Values by Diet and Type of Exercise', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout 
plt.show()

# Explaination of the categorical plot for elementary school students
# This is a box plot that shows how the heartbeats were different for different types of exercises and diets.
# Each box represents the heartbeats of a group of people who did the same type of exercise and had the same diet.
# The line in the middle of the box is the average heartbeats for that group.
# During each of the three time intervals (1 min, 15 min, and 30 min), we can see how the heartbeats changed for different types of exercises and diets.
# The no fat diet group had the highest pulse rates across all three time intervals, while the high fat diet group had the lowest pulse rates.
# This means that diet can influence how fast our heart beats when we exercise, since the no fat diet group had the highest pulse rates 
# no matter the exercise type, while the high fat diet group had the lowest pulse rates no matter of the exercise type.
# Also the running group had the highest pulse rates no matter of the diet type, while the rest had the lowest pulse rates no matter of the diet type. 
# This means that running takes more energy and makes the heart beat faster than the other exercises.
