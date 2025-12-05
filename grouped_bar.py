import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io

# The data is loaded from the provided CSV file content.
csv_data = """\"Quarter\",\"Male_18_24\",\"Male_25_34\",\"Male_35_44\",\"Male_45_54\",\"Male_55_64\",\"Male_65\",\"Female_18_24\",\"Female_25_34\",\"Female_35_44\",\"Female_45_54\",\"Female_55_64\",\"Female_65\"
Q1,157,1531,3103,5579,8891,12762,304,7170,14305,21689,27803,23965
Q2,3401,25739,55960,90495,111230,90875,10480,130831,306867,475682,491248,267572
Q3,116,1919,4021,7008,11139,13094,365,10033,21070,31397,35508,28362
Q4,721,6550,11829,14986,18299,15747,3298,38290,70364,82810,80207,46698
"""
df = pd.read_csv(io.StringIO(csv_data))

# 1. Transform the data into a long format (unpivot)
df_melted = df.melt(id_vars='Quarter', var_name='Category', value_name='Count')

# 2. Extract Gender and Age Group
df_melted[['Gender', 'Age_Group']] = df_melted['Category'].str.split('_', n=1, expand=True)

# Define plotting parameters
fig, ax = plt.subplots(figsize=(14, 8))
plt.style.use('ggplot')

# Define the 12 categories
categories = df_melted['Category'].unique()

# Define color palettes (6 shades for Male, 6 shades for Female)
male_palette = plt.cm.Blues(np.linspace(0.4, 1, 6)) 
female_palette = plt.cm.Reds(np.linspace(0.4, 1, 6))

# Map categories to color and style
category_map = {}
age_groups_order = ['18_24', '25_34', '35_44', '45_54', '55_64', '65']
markers = ['o', 'v', '^', 's', 'P', '*'] # Unique marker for each age group

for cat in categories:
    gender, age = cat.split('_', 1)
    # Get index based on age group order
    age_index = age_groups_order.index(age) 
    
    if gender == 'Male':
        color = male_palette[age_index]
    else:
        color = female_palette[age_index]
        
    category_map[cat] = {
        'color': color, 
        'marker': markers[age_index], 
        'label': f'{gender} ({age.replace("_", "-")})'
    }

# Ensure Quarter order for X-axis: Q1, Q2, Q3, Q4
quarter_sorter = {'Q1': 0, 'Q2': 1, 'Q3': 2, 'Q4': 3}
df_melted['Quarter_Sort'] = df_melted['Quarter'].map(quarter_sorter)

# Plot each category line
for cat in categories:
    # Filter and sort data for the current category
    plot_data = df_melted[df_melted['Category'] == cat].sort_values('Quarter_Sort')
    
    config = category_map[cat]
    ax.plot(
        plot_data['Quarter'], 
        plot_data['Count'], 
        label=config['label'], 
        color=config['color'], 
        marker=config['marker'], 
        linewidth=2, 
        markersize=8,
        linestyle='-'
    )

# Add labels, title, and formatting
ax.set_title('Count Trends by Age Group and Gender Over Quarters', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Count', fontsize=12)
ax.set_xlabel('Quarter', fontsize=12)
ax.set_xticks(plot_data['Quarter'].unique()) # Explicitly set x-ticks to Q1, Q2, Q3, Q4

# Formatting y-axis ticks to include commas
from matplotlib.ticker import FuncFormatter
formatter = FuncFormatter(lambda x, pos: f'{x:,.0f}')
ax.yaxis.set_major_formatter(formatter)

# Add grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
# Place legend outside the plot area
ax.legend(title='Category', loc='center left', bbox_to_anchor=(1.02, 0.5), ncol=1)

# Ensure the plot layout is tight to accommodate the legend
fig.tight_layout(rect=[0, 0, 0.85, 1]) 
plt.show()