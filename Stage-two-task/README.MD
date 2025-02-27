# Task Code 2.1

## Description
This script analyzes bacterial growth data by processing, visualizing, and statistically comparing the growth of wild-type (WT) and mutant (MUT) strains across three different strain types. The analysis includes data processing, growth curve visualization, statistical computations, and hypothesis testing.


## Data Processing
- The script imports a dataset containing bacterial growth measurements.
- Metadata is created to map strain replicates to their respective conditions (WT or MUT).
- Data is restructured for analysis and visualization.

## Visualization
- Growth curves are plotted to compare WT and MUT strains across different conditions.
- Scatter plots and boxplots illustrate the time required to reach 80% of the carrying capacity.

## Statistical Analysis
- The time required for each strain to reach 80% of its maximum optical density (OD) is calculated.
- Normality tests (Shapiro-Wilk) determine whether the data follows a normal distribution.
- A T-test or Mann-Whitney U test is performed to assess statistical significance between WT and MUT strains.
- Results suggest no significant difference in growth between WT and MUT strains (p-value > 0.05).

## Interpretation
- Both WT and MUT strains exhibit similar growth trends.
- Time to reach 80% of carrying capacity remains comparable across most strains.
- Statistical analysis confirms that the mutations do not significantly affect bacterial growth.

This project provides valuable insights into bacterial growth patterns and statistical comparison methodologies in bioinformatics.

# Task 2.3: Botany and Plant Science

## Overview
This project focuses on analyzing metabolite concentration changes in wild-type and mutant plants under pesticide exposure. The dataset contains metabolite levels before and after 24-hour pesticide treatment, allowing for comparison of metabolic changes.

## Dataset
The dataset includes metabolite concentrations under different conditions:
- **WT_DMSO_1**: Wild-type control (DMSO-treated)
- **WT_pesticide_24h_1**: Wild-type after 24-hour pesticide exposure
- **mutant_DMSO_1**: Mutant control (DMSO-treated)
- **mutant_pesticide_24h_1**: Mutant after 24-hour pesticide exposure

### Steps in the analysis:
1. **Import necessary libraries**
   - `pandas` for data manipulation
   - `numpy` for numerical computations
   - `matplotlib` and `seaborn` for data visualization
2. **Create and display the dataset**
   - The script initializes a dictionary containing metabolite concentrations under different conditions.
   - Converts the dictionary into a Pandas DataFrame.
   - Displays the first few rows of the dataset.
3. **Compute metabolic changes (ΔM)**
   - Calculates the difference in metabolite levels after pesticide exposure for both wild-type and mutant samples.
   - Adds new columns:
     - `ΔM_WT = WT_pesticide_24h_1 - WT_DMSO_1`
     - `ΔM_Mutant = mutant_pesticide_24h_1 - mutant_DMSO_1`
   - Displays the computed values.


## Visualization (Optional)
You can extend the script to visualize the metabolite changes using `matplotlib` or `seaborn`. For example:

```python
sns.histplot(df['ΔM_WT'], kde=True, label='Wild Type')
sns.histplot(df['ΔM_Mutant'], kde=True, label='Mutant')
plt.legend()
plt.show()
```

## Future Improvements
- Expand analysis with additional statistical tests.
- Incorporate machine learning for pattern recognition in metabolite changes.
- Develop interactive visualizations for better insights.


# Task 2.4: Biochemistry and Oncology

## Description
This project involves analyzing protein mutation datasets using SIFT and FoldX scores to determine deleterious mutations. The analysis includes data merging, filtering, visualization, and interpretation of the impact of mutations on protein structure and function.

## Data Sources
The datasets used in this analysis are:
- **SIFT Dataset**: [sift.tsv](https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv)
- **FoldX Dataset**: [foldX.tsv](https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv)

## Methodology
1. **Data Loading**
   - The datasets are loaded using `pandas`, ensuring correct tab separation.

2. **Data Processing**
   - A new column `specific_Protein_aa` is created by combining the protein and amino acid columns.
   - The datasets are merged on `specific_Protein_aa` to analyze mutations present in both datasets.

3. **Filtering Deleterious Mutations**
   - Mutations with `sift_score < 0.05` (high probability of being deleterious) and `foldX_score > 2` (destabilizing mutations) are extracted.

4. **Frequency Analysis**
   - The frequency of the first character of amino acids involved in deleterious mutations is calculated.

5. **Data Visualization**
   - Bar charts and pie charts visualize the frequency distribution of the affected amino acids.

## Visualization
- **Bar Charts**: Show frequency of amino acids involved in deleterious mutations for SIFT and FoldX datasets.
- **Pie Charts**: Represent proportional distribution of affected amino acids.

## Structural and Functional Analysis
### Glycine's Role:
- **Structural Role**: Glycine, being the smallest amino acid, provides flexibility in protein structures. It is commonly found in loops and turns.
- **Functional Role**: Essential for enzyme function and protein folding.
- **Impact of Mutations**: Mutations replacing glycine with bulkier amino acids can hinder flexibility, leading to diseases such as osteogenesis imperfecta.

## Key Findings
- Glycine (G), Leucine (L), Alanine (A), and Proline (P) are among the most affected amino acids.
- Hydrophobic amino acids (L, A, V, I, F, W) are crucial for protein core stability.
- Polar/charged amino acids (R, D, Y, S, T) influence enzymatic activity and protein interactions.
- Mutations in these amino acids can lead to protein misfolding, loss of function, or destabilization.

## Conclusion
- Amino acids involved in stability, flexibility, or enzymatic functions are functionally critical.
- Mutations in these residues are key targets in protein mutation studies due to their potential role in diseases.


# Task Code 2.6: Transcriptomics

## Description
This script analyzes transcriptomic data to identify differentially expressed genes. It includes generating a volcano plot to visualize gene expression changes, identifying significantly upregulated and downregulated genes, and exploring the functions of the top affected genes.

## Data Source
- The dataset is retrieved from: (https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt)

## Analysis Steps
### 2.6.1 Volcano Plot
- The script reads a gene expression dataset containing log2 fold change (log2FC) and p-values.
- It computes the -log10 of the p-value for visualization.
- Genes are classified as:
  - **Upregulated**: log2FC > 1 and p-value < 0.01 (plotted in red)
  - **Downregulated**: log2FC < -1 and p-value < 0.01 (plotted in blue)
  - **Non-significant genes**: remaining genes (plotted in gray)
- A volcano plot is generated using `matplotlib`.

### 2.6.2 Upregulated Genes
- Genes meeting the upregulation criteria are extracted and printed.
- The top 5 upregulated genes are displayed.

### 2.6.3 Downregulated Genes
- Genes meeting the downregulation criteria are extracted and printed.
- The top 5 downregulated genes are displayed.

### 2.6.4 Gene Functions
- The functions of the top 5 upregulated and downregulated genes are explored using GeneCards.
- The script automatically opens GeneCards links for these genes in a web browser.

## Functional Insights
### Upregulated Genes:
- **EMILIN2**: Structural protein aiding vessel assembly and elasticity.
- **POU3F4**: Transcription factor involved in neural development.
- **LOC285954**: No information available on GeneCards.
- **VEPH1**: Inhibits TGF-beta signaling; impacts FOXO, Hippo, and Wnt pathways.
- **DTHD1**: Involved in apoptosis and cell signaling.

### Downregulated Genes:
- **TBX5**: Critical for heart and limb development.
- **IFITM1**: Antiviral protein preventing viral entry; involved in cell adhesion.
- **LAMA2**: Facilitates cell migration and extracellular matrix interactions.
- **CAV2**: Regulates MAPK signaling, mitosis, and lipid metabolism.
- **TNN (Tenascin-N)**: Involved in cell migration, angiogenesis, and tumorigenesis.

# Task 2.7: Public Health

## Overview
This project performs an exploratory data analysis (EDA) on a publicly available dataset from NHANES (National Health and Nutrition Examination Survey). The dataset is loaded from a GitHub repository and analyzed using Python libraries for data manipulation, visualization, and statistical testing.

## Data Source
The dataset is loaded from the following URL:
[https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/nhanes.csv](https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/nhanes.csv)

## Steps of Analysis

### 1. Import Required Libraries
The script imports essential libraries for:
- Data handling (`pandas`, `numpy`)
- Visualization (`matplotlib`, `seaborn`)
- Statistical analysis (`scipy.stats`)

### 2. Load and Explore the Dataset
- Loads the dataset into a Pandas DataFrame.
- Displays the first few rows (`head()`), dataset information (`info()`), and missing values summary (`isnull().sum()`).

### 3. Data Cleaning
- Fills missing values with `0` to handle null values.

### 4. Distribution Analysis
- Plots histograms and density curves for key numerical variables: **BMI, Weight, and Age**.
- Converts Weight from kilograms to pounds and visualizes the distribution.

### 5. Descriptive Statistics
Computes and displays key statistical measures:
- Mean pulse rate
- Blood pressure range
- Income variance and standard deviation

### 6. Relationship Visualization
- Uses scatter plots to visualize Height vs. Weight categorized by **Gender, Diabetes, and Smoking status**.
- Creates a combined subplot comparison for these categories.

### 7. Statistical Hypothesis Testing
Performs t-tests to compare:
- Age distributions between males and females.
- BMI between diabetic and non-diabetic individuals.
- Alcohol consumption between single and married individuals.

## Execution
Run the script in a Python environment to generate visualizations and statistical results.

## Results Interpretation
- Distribution plots help understand the spread and central tendencies of key variables.
- Categorical scatter plots reveal possible relationships between demographic factors and health metrics.
- Statistical tests provide insights into significant differences between groups.
