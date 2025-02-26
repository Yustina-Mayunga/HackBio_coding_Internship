#TASK 2.3 (BOTANY AND PLANT SCIENCE)
#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create the dataset
data = {
    "Metabolite": [
        "acetylcarnitine", "aconitic_acid", "adenine", "adenosine_cyclic_monophosphate", "adenosine_monophosphate",
        "adenosine_triphosphate", "adipic_acid", "allantoin", "alpha_ketoglutaric_acid", "aminoadipic_acid",
        "arabitol", "arginine", "argininosuccinic_acid", "asparagine", "aspartic_acid", "butyrylcarnitine",
        "carnitine", "citramalic_acid", "citric_acid_isocitric_acid", "citrulline", "creatine", "creatine_phosphate",
        "creatinine", "cystathionine", "cystine", "cytidine_triphosphate", "deoxy_methylthio_adenosine",
        "deoxyadenosine_triphosphate", "deoxycytidine_monophosphate", "deoxythymidine_triphosphate", "deoxyuridine",
        "dihydroxyacetone_phosphate", "dihydroxyisovalerate", "flavin_adenine_dinucleotide", "folic_acid",
        "fructose_1_6_biphosphate", "gamma_glu_cys", "glutamic_acid", "glutamine", "gluthathione_oxidized",
        "glyceric_acid", "glycine", "guanosine", "guanosine_triphosphate", "hexose", "hexose_1_phosphate",
        "hexose_6_phosphate", "histidine", "homocitrate", "homoserine", "hydroxy_glutamic_acid", "hydroxyglutaric_acid",
        "hypoxanthine", "inosine_monophosphate", "inosine_triphosphate", "isoleucine", "itaconic_acid", "ketobutyrate",
        "ketovaleric_acid", "lactic_acid", "leucine", "maleic_acid", "malic_acid", "methionine", "myristoylcarnitine",
        "n_acetylglutamic_acid", "n_acetylneuraminic_acid", "n_carbamoyl_aspartic_acid", "n_carbamyl_glutamic_acid",
        "nicotinamide_adenine_dinucleotide", "o_phosphorylethanolamine", "orotic_acid", "oxamic_acid", "pantothenic_acid",
        "pentahydroxyhexanoic_acid", "pentose", "phenolred", "phenylalanine", "phenylpyruvic_acid", "phospho_serine",
        "phosphoenolpyruvic_acid", "pyridoxal_5_phosphate", "pyridoxal_hydrochloride", "pyridoxic_acid", "pyridoxine",
        "pyruvic_acid", "riboflavin", "ribose_5_phosphate", "salicylic_acid", "serine", "succinic_acid", "taurine",
        "taurocholic_acid", "thiamine", "threonine", "tryptophan", "tyrosine", "uracil", "uric_acid", "uridine",
        "uridine_diphosphohexose", "uridine_monophosphate", "uridine_triphosphate", "valine", "xanthine", "xanthosine",
        "xylitol", "xylulose_5_phosphate"
    ],
    "WT_DMSO_1": [7, -19.44763901, -0.066412547, -1.917890056, 2.967938969, 12.72884233, 1.165878343, 7.15182243, 3.897284416, 6.566451308, 3.130300677, 10.78788322, 4.529372936, 8.035990108, 12.48780933, 6.450711344, 8.292781335, 2.169572829, 2.775293891, 4.40638839, 12.14212667, 10.9923372, 6.50271102, 9.803747897, 8.805362844, 7.723140751, 0.404038076, 6.573614568, 2.310092091, 6.156367823, 0.066342663, 9.437772289, -0.713531531, 4.766782393, 2.320099265, 7.962358966, 7.788643546, 14.89545443, 15.07049174, 8.246361097, 2.230973374, 13.26447567, 0.5, 8.84362509, 15.51407273, 4.69361598, 8.027299339, 10.07357022, -0.982020371, 6.586799463, 2.474427411, 2.889464911, 5.410297076, 3.276224457, 7.366707808, 11.89033973, 8.858149592, 7.759829632, 8.054340617, 12.7642196, 11.65589608, 14.17273754, 6.789769215, 10.2231342, 5.293257655, 1.624637221, 4.84568322, 3.861186958, -1.441451999, 9.129678488, 6.627829959, -1.3, 0.173257868, 8.593991528, 6.685575078, 14.15627146, 6.665274537, 11.27521346, -2.049134593, 13.43884153, 4.275367495, 2.860044228, 0.667072484, -1.156049774, 5.580222077, 7.178996987, 1.651305172, 6.171646829, 2.935758563, 12.24448764, 6.684445766, 12.75327844, 0.258987743, 10.15638237, 12.98369016, 8.636990755, 11.17042296, 3.097706844, 2.57535632, 3.013875253, 9.541006915, 4.607715907, 9.069960973, 12.14046943, 3.880476129, -0.917890032, 5.148667208, 7.900344807],
    "WT_pesticide_24h_1": [7.900711154, -19.44201458, 0.19558047, -2.173653327, 3.278473476, 12.79676716, 0.575284895, 7.125809097, 4.161240644, 6.336561374, 2.479788896, 9.894826395, 3.988458204, 7.249812779, 12.23886873, 7.814479026, 8.161612936, 1.226277266, 2.124027207, 3, 12.29125752, 11.05323545, 6.86830995, 8.477049396, 5.902271427, 7.818655614, 0.256334501, 6.866636378, 2.140237434, 6.440852023, -0.0767918, 9.922036702, -1.820016376, 4.870740777, 1.733237254, 8.309210622, 7.457725842, 14.64899563, 14.23228954, 8.539733172, 1.470202848, 12.6212927, -0.699722149, 8.973586921, 15.04589703, 4.947592355, 7.948815191, 9.618526889, -0.758615838, 6.108405433, 2.346419628, 2.539064706, 5.194610588, 3.291232706, 7.388589081, 11.86179492, 8.696582926, 7.921670415, 8.288223956, 12.0642288, 10.89618798, 13.05097646, 6.916312006, 9.642908144, 6.590112311, 1.780542969, 4.860381359, 3.696711377, -1.884146713, 9.286091327, 7.243378693, -1.699722143, -0.003728338, 8.406081617, 6.886141749, 13.7355379, 6.196549694, 10.74799134, -2, 14.32050604, 4.79980487, 2.969304611, 0.342922186, -2.256115486, 5.070578335, 7.108147924, 0.923208198, 5.383916725, 2.717117588, 11.6933733, 5.873470569, 12.84010065, 0.115853278, 9.681647749, 12.41239476, 7.663536547, 10.73305983, 2.447584545, 1.923208197, 1.300277847, 9.340211302, 4.781189192, 8.996236871, 11.54620484, 3.424605981, -1.058176118, 5.526786375, 7.836253012],
    "mutant_DMSO_1": [6.49898734, -19.44282046, 0.761424368, -3.291686957, 5.19775963, 12.56360493, 0.219274952, 6.917888241, 4.353611195, 6.238329134, 1.72623494, 10.16724505, 4.110045881, 8.115102651, 11.74682055, 7.166309438, 7.519446854, 1.57126028, 2.177547825, 3.631937643, 11.98436108, 10.93492843, 6.746134497, 9.849925274, 6.953152532, 7.692660279, 0.50532601, 5.651413879, 2.397612192, 5.906021189, 0.829328433, 9.969379531, -2.221297635, 4.627176269, 1.31119744, 8.673953039, 7.135311528, 14.77150006, 14.59675604, 9.557307551, 1.730680845, 12.78820818, 0.681005686, 8.696926717, 15.0883039, 4.957663555, 8.161171996, 9.586172287, -1.059026209, 6.355591559, 2.299274273, 2.389199952, 4.989547616, 3.154569261, 7.2327568, 11.80810463, 7.835082024, 7.666648239, 6.956359182, 12.33267157, 11.42875504, 14.5761148, 6.497031364, 9.879223913, 5.539620275, 2.685592955, 4.928933199, 4.027533534, -2.526152215, 9.238670595, 6.773459856, -1.659418749, 3.546256273, 8.322930864, 6.874601669, 13.74827625, 6.169383145, 10.90429264, -1.806260137, 14.27734532, 4.03653915, 3.534861519, 0.515667954, -2.221297635, 5.213727641, 7.456505881, 0.72623494, 5.360799526, 3.317122274, 11.95482726, 5.890707385, 12.42133969, -0.090053106, 9.816020514, 12.7340582, 8.099610331, 10.98162785, 2.463200534, 1.997409734, 2.141272439, 9.261630331, 6.447418538, 8.854404336, 11.77530615, 3.461864086, -1.121761965, 5.464535744, 7.695150568],
    "mutant_pesticide_24h_1": [5.935604875, -19.44356959, 0.227218025, -1.683514639, 4.834390917, 12.83297581, 0.479984096, 6.608346733, 4.170481011, 6.404160351, 3.244381818, 9.650624543, 4.177448162, 8.283826918, 11.91788011, 7.796669688, 8.318625277, 1.911033913, 1.733325106, 0.272542016, 12.50536161, 11.40048982, 6.717023293, 9.507569261, 5, 7.958103642, 0.427516676, 3, 2.386874692, 6.512029823, 0.16448227, 10.36842838, -0.803808871, 4.893007502, 1, 8.860754354, 7.32737707, 14.74972, 14.46647455, 9.802395155, 0.822376293, 12.96993507, 0.386874691, 9.051973694, 14.93660665, 5.336631937, 8.470240043, 9.46376662, -0.654945485, 6, 2.476760195, 2.741407452, 5.247222701, 3.343285423, 7.43366091, 11.10456743, 8.778660411, 7.909988536, 7.39948593, 12.47118008, 11.08993781, 12.67857439, 6.849114021, 9.642487822, 5.271612145, 3.522816012, 4.967249923, 3.810900974, -1.803808873, 9.553910458, 7.918033325, -1.572483326, 1.257591674, 8.368129359, 7.21227268, 13.51534167, 5.82554775, 10.80611259, -2.005442734, 14.31177642, 4.364372693, 3.794162691, 0.967249923, -3.520015914, 4.798042645, 6.701053287, 0.591492411, 5.543379177, 3.049839704, 11.83342141, 5.690133575, 12.77170726, 0.030181178, 9.878804119, 12.61556456, 7.464199086, 10.6200264, 2.341514158, 1.505519188, 1.352109273, 9.543812499, 6.172724124, 9.170855105, 11.5002758, 2.978690863, -1.005442733, 5.963511997, 7.932445983]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the first few rows
print(df.head()) 
# Calculate ΔM for Wild Type and Mutants
df['ΔM_WT'] = df['WT_pesticide_24h_1'] - df['WT_DMSO_1']
df['ΔM_Mutant'] = df['mutant_pesticide_24h_1'] - df['mutant_DMSO_1']

# Display the calculated ΔM values
print(df[['Metabolite', 'WT_DMSO_1', 'WT_pesticide_24h_1', 'ΔM_WT', 'mutant_DMSO_1', 'mutant_pesticide_24h_1', 'ΔM_Mutant']].head())
# Scatter plot of ΔM_WT vs. ΔM_Mutant
plt.figure(figsize=(8, 6))
sns.scatterplot(x='ΔM_WT', y='ΔM_Mutant', data=df)
plt.title('Scatter Plot of ΔM for WT vs. Mutants')
plt.xlabel('ΔM_WT (Wild Type)')
plt.ylabel('ΔM_Mutant (Mutants)')
plt.grid(True)
plt.show()
# Add a reference line (y = x)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='ΔM_WT', y='ΔM_Mutant', data=df)
plt.plot([-10, 10], [-10, 10], color='red', linestyle='--', label='y = x')
plt.title('Scatter Plot with Reference Line (y = x)')
plt.xlabel('ΔM_WT (Wild Type)')
plt.ylabel('ΔM_Mutant (Mutants)')
plt.grid(True)
plt.legend()
plt.show()
# Calculate residuals
df['Residual'] = df['ΔM_Mutant'] - df['ΔM_WT']

# Define residual cutoff
residual_cutoff = 0.3  # Adjust as needed

# Color points based on residual cutoff
df['Color'] = np.where((df['Residual'] >= -residual_cutoff) & (df['Residual'] <= residual_cutoff), 'grey', 'salmon')

# Scatter plot with colored points
plt.figure(figsize=(8, 6))
sns.scatterplot(x='ΔM_WT', y='ΔM_Mutant', hue='Color', palette={'grey': 'grey', 'salmon': 'salmon'}, data=df)
plt.plot([-10, 10], [-10, 10], color='red', linestyle='--', label='y = x')
plt.title('Scatter Plot with Residual-Based Coloring')
plt.xlabel('ΔM_WT (Wild Type)')
plt.ylabel('ΔM_Mutant (Mutants)')
plt.grid(True)
plt.legend()
plt.show()
# Metabolites outside the residual cutoff
outliers = df[(df['Residual'] < -residual_cutoff) | (df['Residual'] > residual_cutoff)]
print("Metabolites outside the residual cutoff:")
print(outliers[['Metabolite', 'ΔM_WT', 'ΔM_Mutant', 'Residual']])
