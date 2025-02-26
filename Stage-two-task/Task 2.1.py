##Task code 2.1
##Github Links;
#karimat: https://github.com/hardae/hackbio-biocoding-internship/blob/main/stage%202/stage%202%20karimah
#Yustina: https://github.com/Yustina-Mayunga/HackBio_coding_Internship/tree/main/Stage-two-task
#Chaimae:
#Favour:
#Joshua:

##LinkedIn link:

### This script analyzes bacterial growth data by processing, visualizing, and statistically comparing 
# the growth of wild-type (WT) and mutant (MUT) strains across three different strain types.

## Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Importing and reading the dataset
Data_source = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv"
df = pd.read_csv(Data_source, sep='\t')  # reading the dataset

# Debug: Check if data is loaded properly
print("Data Preview:")
print(df.head())

# Creating metadata
metadata = pd.DataFrame({
    "Strain": [
        "Strain1_Rep1", "Strain1_Rep2", "Strain2_Rep1",
        "Strain2_Rep2", "Strain3_Rep1", "Strain3_Rep2"
    ],
    "WT_1": ["A1", "A3", "A5", "A7", "A9", "A11"],
    "MUT_1": ["A2", "A4", "A6", "A8", "A10", "A12"],
    "WT_2": ["B1", "B3", "B5", "B7", "B9", "B11"],
    "MUT_2": ["B2", "B4", "B6", "B8", "B10", "B12"],
    "WT_3": ["C1", "C3", "C5", "C7", "C9", "C11"],
    "MUT_3": ["C2", "C4", "C6", "C8", "C10", "C12"]
})

# Convert Data structure for analysis
def convert_to_curve_time(df):
    if 'time' not in df.columns:
        raise ValueError("Input DataFrame must contain a 'time' column.")
    
    df_time_indexed = df.set_index('time')
    transposed_data = df_time_indexed.transpose()
    x_values = df['time'].values  # Extract time values
    return transposed_data, x_values

# Processing Metadata
def process_metadata(metadata_df):
    MD = [] #Creating a metadata
    for _, row in metadata_df.iterrows():
        strain_rep = row['Strain']
        strain, rep = strain_rep.split('_')
        for exp_num in [1, 2, 3]:
            MD.extend([
                {'curve_id': row[f'WT_{exp_num}'], 'strain': strain, 'rep': rep, 'type': 'WT', 'experiment': exp_num},
                {'curve_id': row[f'MUT_{exp_num}'], 'strain': strain, 'rep': rep, 'type': 'MUT', 'experiment': exp_num}
            ])
    return pd.DataFrame(MD)

# Plot bacterial growth curves
def plot_strain_curves(converted_data, x_values, unit_type="min"):
    curve_metadata = process_metadata(metadata)
    fig, axs = plt.subplots(1, 3, figsize=(22, 7))
    fig.subplots_adjust(top=0.85, bottom=0.35, wspace=0.35)
    fig.suptitle('Growth Curves of the Wild Type and Mutant Strains Over Time ', y=1, fontsize=16)
    
    type_colors = {'WT': 'Cyan', 'MUT': 'Pink'}
    rep_styles = {'Rep1': ':', 'Rep2': '-'}
    
    for idx, strain in enumerate(sorted(curve_metadata['strain'].unique())):
        ax = axs[idx]
        ax.set_title(f"{strain}", fontsize=14, pad=15)
        ax.set_xlabel(f"Time ({unit_type})", fontsize=12)
        ax.set_ylabel("OD600 (log scale)", fontsize=12)
        ax.set_yscale('log')
        
        strain_data = curve_metadata[curve_metadata['strain'] == strain]
        
        for _, row in strain_data.iterrows():
            if row['curve_id'] in converted_data.index:
                ax.plot(
                    x_values,
                    converted_data.loc[row['curve_id']],
                    color=type_colors[row['type']],
                    linestyle=rep_styles[row['rep']],
                    linewidth=1.5
                )
        
        y_min = converted_data.loc[strain_data['curve_id']].min().min()
        y_max = converted_data.loc[strain_data['curve_id']].max().max()
        if y_min > 0 and y_max > 0:
            ax.set_ylim(y_min * 0.5, y_max * 2)
        else:
            ax.set_ylim(1e-3, 1)
        
    plt.tight_layout()
    plt.show()

# Convert and plot data
converted_data, x_values = convert_to_curve_time(df)
plot_strain_curves(converted_data, x_values)
#==========================================================================================================================#

# Find 80% of Maximum OD
# This function calculates the OD value at 80% of the max OD and the corresponding time point.
def find_80_percent_density(data, time_step=1):
    max_density = data.max().max()
    
    threshold = 0.8 * max_density
    
    for col in data.columns:
        if (data[col] >= threshold).any():
            time_80_percent = int(col) * time_step  
            density_at_80 = data[col].max() 
            return max_density, time_80_percent, density_at_80
    
    return max_density, None, None 
# converting the data to match the wanted structure
converted_data, x_values =convert_to_curve_time(df)
# ploting the growth curves 
plot_strain_curves(converted_data, x_values, unit_type='min')
# Time to reach 80% of Carrying capacity. 
results = []
for curve_id in converted_data.index:
    curve_data = pd.DataFrame(converted_data.loc[curve_id]).transpose() # Get curve data and ensure proper formatting
    curve_data.columns = curve_data.columns.astype(int) # Convert columns to integers
    max_dens, time_80, dens_80 = find_80_percent_density(curve_data, time_step=1)   # Analyze curve
    results.append({
        'curve_id': curve_id,
        'max_density': max_dens,
        'time_to_80%': time_80,
        'density_at_80%': dens_80
    })
results_df = pd.DataFrame(results)
# Create full metadata mapping for merging it to the results
curve_metadata = process_metadata(metadata)
# Merge with your results
results_df = results_df.merge(curve_metadata[['curve_id', 'strain', 'type']], on='curve_id')
# Print results
print("\nTime to reach 80% of Carrying Capacity (Max OD600):")
print(results_df[['strain', 'type', 'time_to_80%', 'density_at_80%']])
#==============================================================================================================#

#Scatter Plot - Time to 80% Carrying Capacity
plt.figure(figsize=(8, 6))
color_map = {'WT': 'Cyan', 'MUT': 'Pink'}
marker_map = {'Strain1': '*', 'Strain2': '+', 'Strain3': 'x'}

for strain in ['Strain1', 'Strain2', 'Strain3']:
    for t in ['WT', 'MUT']:
        subset = results_df[(results_df['strain'] == strain) & (results_df['type'] == t)]
        if not subset.empty:
            plt.scatter(subset['time_to_80%'], subset['density_at_80%'],
                        c=color_map[t], marker=marker_map[strain], s=150, edgecolor='w', alpha=0.9, label=f'{strain} {t}')

plt.title('Time to 80% Carrying Capacity by Strain and Type')
plt.xlabel('Time (minutes)')
plt.ylabel('Density at 80%')
plt.grid(alpha=0.2)
plt.legend()
plt.show()
#======================≈==================================================#

#Boxplot - Time to 80% OD by Strain and Type
plt.figure(figsize=(10, 6))
sns.boxplot(x='strain', y='time_to_80%', hue='type', data=results_df, palette=color_map, width=0.5, linewidth=1.4)

plt.title('Time to Reach Carrying Capacity by Strain and Mutation Type', pad=20)
plt.xlabel('Strain', labelpad=15)
plt.ylabel('Time (minutes)', labelpad=15)
plt.legend(title='Mutation Type', frameon=False)
sns.despine()
plt.show()
#========================================================================#
# Statistical Analysis
wt_times = results_df[results_df['type'] == 'WT']['time_to_80%']  ##Time taken by the wild type strains to reach 80% of max. OD
mut_times = results_df[results_df['type'] == 'MUT']['time_to_80%'] #Time taken by the mutant type strains to reach 80% of max. OD

##Checking for normality (Shapiro-Wilk normality test)
shapiro_wt = stats.shapiro(wt_times) 
shapiro_mut = stats.shapiro(mut_times)

print(f"Shapiro-Wilk Test for WT Strains: W={shapiro_wt.statistic}, p-value={shapiro_wt.pvalue}")
print(f"Shapiro-Wilk Test for MUT Strains: W={shapiro_mut.statistic}, p-value={shapiro_mut.pvalue}")

# Choose appropriate statistical test based on normality
if shapiro_wt.pvalue > 0.05 and shapiro_mut.pvalue > 0.05:
    test_stat, p_value = stats.ttest_ind(wt_times, mut_times)  # Fix: Correct function name
    test_name = "T-Test"
else:
    test_stat, p_value = stats.mannwhitneyu(wt_times, mut_times, alternative='two-sided')  # Fix: Correct variable names
    test_name = "Mann-Whitney U Test"

print(f"{test_name} Result: Statistic={test_stat:.2f}, p-value={p_value:.3f}")
alpha = 0.05
if p_value < alpha:
    print("There is a significant difference between WT and MUT carrying capacity times.")
else:
    print("There is NO significant difference between WT and MUT carrying capacity times.")
#Output: "Mann-Whitney U Test: statistic: 171.50, P-value: 0.775


###Interpretations.
#From the growth curve, both strains (WT & MUT) follow the same growth trajectory.
#The time to reach 80% of the carrying capacity remain close among the WT and MUT type strains, with exception of strain 1
#Based on the statistical results, we can conclude that there is no significant difference between mutants and wild-type strain in terms of OD recorded because the P-value is greater than 0.05. Manipulation done in the mutants didn't affect the growth.
