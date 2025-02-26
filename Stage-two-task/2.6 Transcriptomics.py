#Task 2.6: Transcriptomics
#2.6.1 Volcano Plot
import pandas as pd
resources = "https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt"
df = pd.read_csv(resources, sep = ' ')
import matplotlib.pyplot as plt
import numpy as np
df['-log10(pvalue)'] = -np.log10(df['pvalue'])
#To determine upregulated and downregulated genes
upregulated = (df['log2FoldChange'] > 1) & (df['pvalue'] < 0.01)
downregulated = (df['log2FoldChange'] < -1) & (df['pvalue'] < 0.01)
#Plot
plt.figure(figsize=(10, 6))
#Plot non-significant genes(gray)
plt.scatter(df['log2FoldChange'], df['-log10(pvalue)'], color = "gray", alpha = 0.5, label = "Non-significant")
#To plot upregulated genes(red)
plt.scatter(df[upregulated]['log2FoldChange'], df[upregulated]['-log10(pvalue)'], color = "red", label = "Upregulated")
#To plot downregulated genes(blue)
plt.scatter(df[downregulated]['log2FoldChange'], df[downregulated]['-log10(pvalue)'], color = "blue", label = "downregulated")
#Threshold lines
plt.axhline(-np.log10(0.01), linestyle = '--', color = 'black', linewidth = 0.8)  # p-value threshold
plt.axvline(1, linestyle='--', color='red', linewidth=0.8)  # Log2FoldChange threshold
plt.axvline(-1, linestyle='--', color='blue', linewidth=0.8)  # Log2FoldChange threshold
# Labels and title
plt.xlabel("Log2FC")
plt.ylabel("-log10(p-value)")
plt.title("Volcano Plot of RNA-seq Data")
plt.legend()
plt.show()
#2.6.2 Upregulated genes
upregulated_genes = df[upregulated]
print(f"The upregulated genes are as follows:\n{upregulated_genes}\n")
#2.6.3 Downregulated genes
downregulated_genes = df[downregulated]
print(f"The downregulated genes are as follows:\n{downregulated_genes}\n")
# Display top results
print("Top 5 Upregulated Genes:")
print(upregulated_genes[['Gene', 'log2FoldChange', 'pvalue']].head())
print("\nTop 5 Downregulated Genes:")
print(downregulated_genes[['Gene', 'log2FoldChange', 'pvalue']].head())
# 2.6.4.1 Functions of Top 5 Upregulated Genes
# Open GeneCards links for top 5 upregulated genes
import webbrowser
for gene in upregulated_genes['Gene'].head():
    url = f"https://www.genecards.org/cgi-bin/carddisp.pl?gene={gene}"
    webbrowser.open(url)
print("""
The functions of the top 5 upregulated genes are as follows:\n EMILIN2: Likely anchors smooth muscle cells to elastic fibers and contributes to elastic fiber formation. Also involved in vessel assembly regulation. Exhibits cell adhesive properties.\n
POU3F4: A probable transcription factor active during early neural development and in specific neurons of the mature brain. Plays a role in pituitary and inner ear development.\n
LOC285954: No information available on GeneCards.\n
VEPH1: Interacts with TGF-beta receptor 1 to inhibit SMAD2 dissociation, impairing TGF-beta signaling. May also influence FOXO, Hippo, and Wnt pathways.\n
DTHD1: Encodes a protein with a death domain, involved in apoptosis and cellular signaling complex formation.\n
""")
# 2.6.4.2 Functions of Top 5 Downregulated Genes
# Open GeneCards links for top 5 downregulated genes
for gene in downregulated_genes['Gene'].head():
    url = f"https://www.genecards.org/cgi-bin/carddisp.pl?gene={gene}"
    webbrowser.open(url)
print("""
The functions of the top 5 downregulated genes are as follows:\n TBX5: A transcription regulator crucial for heart and limb development, binding to the NPPA promoter.\n
IFITM1: An interferon-induced antiviral protein preventing viral entry into host cells. Active against multiple viruses, including SARS-CoV-2 and HIV-1. Also involved in cell adhesion, growth regulation, and osteoblast differentiation.\n
LAMA2: A laminin protein facilitating cell attachment, migration, and tissue organization. Essential for embryonic development and extracellular matrix interactions.\n
CAV2: A caveolar protein interacting with G-proteins and regulating MAPK signaling. Involved in mitosis modulation, lipid metabolism, and apoptosis.\n
TNN (Tenascin-N): An extracellular matrix protein involved in neurite outgrowth, cell migration, and angiogenesis. Also plays a role in tumorigenesis, particularly in breast cancer.
""")

##Github Links;
#karimat: https://github.com/hardae/hackbio-biocoding-internship/blob/main/stage%202/stage%202%20karimah
#Yustina: https://github.com/Yustina-Mayunga/HackBio_coding_Internship/tree/main/Stage-two-task
#Chaimae:
#Favour: https://github.com/Fabs247/hackbio_biocoding_intern/blob/main/stage_2_task
#Joshua: https://github.com/RagingThunder99/Hackbio-biocoding-internship/tree/main/Stage%20Two
