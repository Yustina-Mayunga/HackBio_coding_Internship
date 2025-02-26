#Task 2.4: Biochemistry and Oncology
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load datasets ensuring correct tab separation
data_source_1 = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv"
data_source_2 = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv"
df_sift = pd.read_csv(data_source_1, sep="\t", names=["Protein", "Amino_Acid", "sift_score"], skiprows=1)
df_foldx = pd.read_csv(data_source_2, sep="\t", names=["Protein", "Amino_Acid", "foldX_score"], skiprows=1)
# Creating the new column
df_sift['specific_Protein_aa'] = df_sift['Protein'] + "_" + df_sift['Amino_Acid']
df_foldx['specific_Protein_aa'] = df_foldx['Protein'] + "_" + df_foldx['Amino_Acid']
# Merge df_sift and df_foldx using specific_Protein_aa as the key
df_merged_dataset = pd.merge(df_sift, df_foldx, on="specific_Protein_aa", how="inner")
df_deleterious_mut = df_merged_dataset[(df_merged_dataset["sift_score"] < 0.05) & (df_merged_dataset["foldX_score"] > 2)]
dataset_freq_sift = df_deleterious_mut["Amino_Acid_x"].str[0].value_counts()
print(dataset_freq_sift)
dataset_freq_foldx = df_deleterious_mut["Amino_Acid_y"].str[0].value_counts()
print(dataset_freq_foldx)
# Bar Chart for both Foldx and Sift Datasets
def plot_bar_chart(data, title):
    sns.barplot(x=data.index, y=data.values)
    plt.xlabel("First Character of Amino Acid")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.show()
plot_bar_chart(dataset_freq_sift, "Frequency of First Character in Amino_Acid_x")
plot_bar_chart(dataset_freq_foldx, "Frequency of First Character in Amino_Acid_y")
# Pie Chart for both datasets
def plot_pie_chart(data, title):
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=data.index, autopct='%1.1f%%')
    plt.title(title)
    plt.show()
plot_pie_chart(dataset_freq_sift, "Pie Chart of First Amino Acid Frequencies (SIFT)")
plot_pie_chart(dataset_freq_foldx, "Pie Chart of First Amino Acid Frequencies (FoldX)")
# Description of Glycine’s Impact on Protein Structure & Function
# Structural Role:
# Glycine is the smallest amino acid, with a hydrogen atom as its side chain.Because of its small size, it provides flexibility in protein structures.It is often found in turns, loops, and tight regions of proteins, such as in collagen and hinge regions of enzymes.
# Functional Role:
# Since glycine is nonpolar, it can be found in both hydrophobic and hydrophilic environments. It plays a critical role in enzyme function by allowing necessary flexibility. Mutations that replace glycine with a bulkier amino acid may restrict movement and affect protein folding, stability, and function.
# Why Glycine Mutations Are Harmful:
# Loss of flexibility → Can disrupt the function of enzymes and structural proteins. The inability to maintain protein conformation → May lead to diseases like osteogenesis imperfecta (collagen disorder).
# Check amino acids with more than 100 occurrences
high_freq_sift = dataset_freq_sift[dataset_freq_sift > 100]
high_freq_foldx = dataset_freq_foldx[dataset_freq_foldx > 100]
print(high_freq_sift)
print(high_freq_foldx)
#  From the frequency analysis, Glycine (G), Leucine (L), Alanine (A), and Proline (P) are the most affected amino acids in both structural (FoldX) and functional (SIFT) analyses.
# Structural Role:
# Many of these amino acids (L, A, V, I, F, W) are hydrophobic, meaning they are typically found inside protein cores to maintain stability.
# Glycine (G) and Proline (P) play key roles in flexibility and rigidity of protein structures.
# Mutations in these amino acids can destabilize protein folding or cause misfolding.
# Functional Role:
# Some amino acids (R, D, Y, S, T) are polar or charged, often participating in enzyme activity, phosphorylation, or binding interactions.
# Mutations in these residues could alter protein function by affecting electrostatic interactions or regulatory modifications.
# Conclusion:





12:20
# Amino acids that are small, hydrophobic, or polar tend to be structurally essential, while those involved in stability, flexibility, or enzymatic functions are functionally critical. Mutations in these residues could lead to protein misfolding, loss of function, or destabilization, making them key targets in protein mutation studies.
