# seaborn_visualizations
Data visualizations using seaborn 


### Planet Discovery & Pulse Analysis Visualizations
Overview
This project includes two visualization parts to explore the seaborn library. The first one (p_test3.py) visualizes the exoplanet discovery dataset from Seaborn. The second one (heat_3.py) focuses on analyzing exercise pulse data using heatmaps and categorical plots. Both projects use a combination of relational, distributional, and categorical plots to find interesting trends and patterns in the data.

### Files 
- **Exercise_Data.csv**: Custom file containing pulse data collected at different times during exercise, along with the subject’s diet and type of activity.
- **copilotchat_vis** : copilot chat log
- **heat_3** : Part 1 file 
- **p_test3**: Part 2 file 

### Libraries Used
- Pandas as pd
- Numpy as np
- Seaborn as sns
- Matplotlib
- os (for handling file paths)

### Visualization Techniques Used

- **Data Transformation**
  - Normalization of numeric data
  - Creation of categorical variables (decades)
  - Filtering for relevant data subsets
  
- **Plot Customization**
  - Custom color palettes
  - Appropriate axis scaling
  - log scales 
  - Clear titles and labels
  - Legend customization
  - Grid and layout adjustments
  
- **Statistical Visualization**
  - Distribution plots (histograms, ECDFs)
  - Relationship plots (scatter plots, line plots)
  - Categorical plots (box plots, count plots, strip plots)
  -  visualizations (heatmaps)


### Part 1: Planet Discovery Visualizations 
- Uses the p_test3.py file and the built-in planets dataset in seaborn 
- This project explores trends in planet mass, discovery methods, and orbital periods over time. It uses multiple plot types to better understand how exoplanet discoveries have changed over the years and how their physical characteristics vary.

**Visualizations Created**
- Scatter Plot: Planet mass vs orbital period (log scale), color-coded by year.
- Line Plot: Average orbital period per year with a 5-year rolling average
- Histogram: Number of planets discovered each year, stacked by discovery method
- ECDF Plot: Cumulative distribution of planet mass with percentile lines
- Count Plot: Number of planets discovered per year
- Swarm Plot: Distribution of planet mass by discovery method (top 5 methods only)

**Features**
- Uses log scales for better data distribution on scatter and ECDF plots
- Annotations highlight peak discovery years
- Percentile markers help break down the distribution of planet masses

### Part 2: Pulse Rate Visualization 
- using the heat_3.py and Exercise_Data.csv files 
- This project analyzes pulse rate changes during exercise based on different time intervals, types of exercise, and diet types. It uses a heat map and a series of box plots to show how physical activity and diet affect heart rate variability

**Visualizations Created**
    - Heatmap: Normalized pulse rate across 1, 15, and 30 minutes post-exercise
    -  Categorical Box Plots: Pulse rates grouped by exercise type and diet across the three time intervals

**Features**
  - A heat map visually represents how heart rate changes over time for different individuals
  - Box plots compare how diet and exercise type influence pulse rates
  - Includes simple explanations of both plots written for an elementary school audience to help make data more accessible

**Limitations**
- Normalizing the data makes it easier to visualize but can change the true differences in actual pulse rates
- Mass and orbital period are highly skewed, so even with log scaling, outliers may still dominate
- The dataset is filtered to remove missing values, which reduces the total number of usable observations



