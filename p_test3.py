import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

try:
    # Load and clean dataset
    # dropna() removes rows with NaN values in the specified columns
    planets = sns.load_dataset('planets')
    if planets is None:
        raise ValueError("Dataset 'planets' could not be loaded.")
    planets = planets.dropna(subset=['mass', 'orbital_period', 'year'])
except Exception as e:
    print(f"Error loading or cleaning dataset: {e}")
    exit()


# Create a 'decade' column for categorical grouping
# Groups the discovery years together 
planets['decade'] = (planets['year'] // 10) * 10

# Set visual style
# Adjust the scaling and context of the plots
sns.set(style="whitegrid", context="talk")

# --------------------------------------
# Relational Plots
# Mass vs Orbital Period Colored by Year
plt.figure(figsize=(12, 7)) # Set figure size
scatter = sns.scatterplot(
    data=planets,
    x='orbital_period',
    y='mass',
    hue='year',
    palette='viridis', #color palette
    alpha=0.8,
    edgecolor=None, #removes color edge 
    size='mass',    #scales the size of the points by mass
    sizes=(20, 200), #range of points size 
    legend='brief' #brief legend
)

plt.xscale('log')
plt.yscale('log')
plt.title('Planet Mass vs Orbital Period Colored by Year') 
plt.xlabel('Orbital Period (days) — Proxy for Distance')
plt.ylabel('Mass (Jupiter Masses)')
plt.colorbar(scatter.collections[0], label='Discovery Year') #shows the discorvery year
plt.tight_layout() #Ajust layout 
plt.show()

# The scatter plot shows the relationship between the mass of planets and their orbital period, colored by the year of discovery.
# The color of the points indicates the year of discovery, with a gradient from purple (earlier years) 
# to yellow (later years). The bigger the dots the larger the mass is and the smaller the dots the smaller the mass is. 
# From this scatter plot we can conclude that there is a correlation between the mass of the planet and the orbital period.
# The plots shows that the planets with a longer orbital period tend to have a larger mass. Althought there are a few outliers 
# that do not follow this trend. The plot also shows that majority of the plants found were from 2000 to 2010, 
# which could because as time goes on our technology advances and we have a better chance at being able to find the planets.


# Average Orbital Period Per Year with Rolling Avg
# Calculate average orbital period per year
avg_orbital_period = planets.groupby('year')['orbital_period'].mean().reset_index()

# creating the line plot 
plt.figure(figsize=(12, 6))
sns.lineplot(data=avg_orbital_period, x='year', y='orbital_period', marker='o',
             color=sns.color_palette("coolwarm")[3], linewidth=2)

# Adds rolling average 
sns.lineplot(data=avg_orbital_period, x='year',
             y=avg_orbital_period['orbital_period'].rolling(5).mean(),
             color='orange', linewidth=2, label='5-Year Rolling Average')

# adds titles and labels 
plt.title('Average Orbital Period Per Year with Rolling Average')
plt.xlabel('Year')
plt.ylabel('Average Orbital Period (days)')
plt.legend(title="Legend") #adding a key 
plt.tight_layout() # Adjust layout
plt.show()

# The line plot shows the average orbital period of planets discovered each year. This graph groups all of the planets found in the same year 
# and takes the average of their orbital period. From this plot we can see that the average orbital period of planets discovered has been 
# increasing over the years, this could be due to the fact that as time goes by we are able to create new technologies that pass our previous 
# limitations and allow us to find planets. 

# --------------------------------------
# Distributional Plots 
# Histogram Number of Planets Discovered Per Year

plt.figure(figsize=(12, 6)) # set figure size 
sns.histplot(
    data=planets,
    x='year',
    bins=20, # number of bins
    kde=True,  # kernel density estimate
    hue='method',
    palette='viridis', # color palette
    alpha=0.7,
    multiple='stack' # stacks the bars on top of each other
)

# Annotate peak discovery years 
#  Finds the top 3 years with the most discoveries
peak_years = planets['year'].value_counts().sort_values(ascending=False).head(3).index
for peak in peak_years:
    count = planets['year'].value_counts()[peak] 
    # Adds the text above the bar
    plt.text(peak, count + 3, f'Peak: {peak}', ha='center', color='black', fontsize=11)

# Adds titles and labels
plt.title('Number of Planets Discovered Per Year by Discovery Method')
plt.xlabel('Year')
plt.ylabel('Number of Planets')
plt.tight_layout() # Adjust layout
plt.show()

# The histogram shows the number of planets discovered per year, with a kernel density estimate (KDE) overlay to visualize the distribution. 
# The bars are colored by discovery method, and the top three peak years are annotated above the bars.
# From this histogram we can conclude that the planets were mostly discoverd using the radial velocity method compared to the other methods of finding planets. 
# This could be cause the other methods were not as used as much as the radial velocity method, or it could indicated that 
# the radial velocity method is more effective in finding planets. Also the histogram shows that there was a spike 
# in the number of planets discovered in 2009 to 2011, which could have been cause by increase observations or 
# maybe a new technology that was used to help find planets.


# ECDF plot of Planet Mass with Percentiles

plt.figure(figsize=(12, 6)) #Figure size 
sns.ecdfplot(data=planets, x='mass', log_scale=True, color=sns.color_palette("Blues_d")[2]) # logarthmic scale and blue color line 

# Define colors for each percentile line to tell which line is which 
percentiles = [25, 50, 75]  # Define the percentiles that will be used
# Gives  each a different color 
percentile_colors = {25: 'green', 50: 'orange', 75: 'purple'}

# Add vertical percentile lines with unique colors and labels
for p in percentiles:
    value = np.percentile(planets['mass'], p) # calculates the values 
    # Adds the vertical line to the plot in the different colors
    plt.axvline(value, linestyle='--', color=percentile_colors[p], alpha=0.7, linewidth=1.5, label=f'{p}th Percentile ≈ {value:.2f} Mj')

# Add a legend to the plot to tell what each line is
plt.legend(title='Percentiles', loc='upper left', fontsize=10)

# Adds titles and labels
plt.title('Cumulative Distribution of Planet Mass (Log Scale) with Percentiles')
plt.xlabel('Mass (Jupiter Masses, Mj)')
plt.ylabel('Cumulative Probability')
plt.tight_layout()
plt.show()

# --------------------------------------
# Categorical Plots
# Count of Planets Discovered per Year

plt.figure(figsize=(16, 6))
sns.countplot(data=planets, x='year', palette='crest') #figure size 
plt.xticks(rotation=90)  # Rotates the x-axis labels 
#title and labels
plt.title('Number of Planets Discovered per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.tight_layout() # Adjust layout
plt.show()


# Strip Plot of Mass by Discovery Method
#filters by top methods
# Filters by top methods
top_methods = planets['method'].value_counts().head(5).index
plt.figure(figsize=(14, 6))  # Set figure size

sns.stripplot(
    data=planets[planets['method'].isin(top_methods)],
    x='method', y='mass', palette='Set2', jitter=True, alpha=0.7  # jitter = better visibility
)

plt.yscale('log')  # Use log scale for mass distribution
# Adds the title and labels
plt.title('Planet Mass Distribution by Discovery Method')
plt.xlabel('Discovery Method')
plt.ylabel('Mass (Jupiter Masses)')
plt.tight_layout()  # Adjust layout
plt.show()

