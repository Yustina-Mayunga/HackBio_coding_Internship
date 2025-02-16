# RNA Codon Table for Translation
codon_table = {
    'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
    'UAC': 'Y', 'UAU': 'Y', 'UAA': '', 'UAG': ''
}
#A= Alanine, R= Arginine, H = Histidine, V =Valine, F = Phenylalanine, L = Leucine, Q = Glutamine,  Y= Tyrosine, '' = stop codon
#Function to translate an DNA sequence into a protein sequence.
def dna_to_protein(dna_sequence):
    #Transcribing the dna sequence
    transcription_rules = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'} #the values are RNA nucleotides
    mrna_sequence = ''.join([transcription_rules[base] for base in dna_sequence])
    #Translating the mrna sequence to protein
    protein = []  #Initializing the empty protein list
    # Split into codons (triplets)
    for i in range(0, len(mrna_sequence), 3):
        codon = mrna_sequence[i:i+3]  # Extract codon
        #Translate codons into AA
        if codon in codon_table:
            amino_acid = codon_table[codon]
         # Stop translation if stop codon is found
            if amino_acid == '':
                break
            #Append the AA to the protein list
            protein.append(amino_acid)
    return ''.join(protein)
#Call the function
protein  = dna_to_protein("ATGCGTAAG")
print(protein)
#_______________________________________________________________________________________
import pandas as pd
import random
# Your logistic growth function with randomization for the lag and exp phases
def logistic_growth_curve(Initial_population, Carrying_capacity, Growth_rate, time_length, lag_phase_duration=None, exp_phase_duration=None):
    Population = Initial_population
    # Randomize the durations if not provided
    if lag_phase_duration is None:
        lag_phase_duration = random.randint(2, 6)  # Randomize lag phase between 2 and 6 time steps
    if exp_phase_duration is None:
        exp_phase_duration = random.randint(5, 15)  # Randomize exponential phase between 5 and 15 time steps
    # List to input population values for each time step
    population_list = []
    # Simulate population growth
    for t in range(time_length):
        if t < lag_phase_duration:
            Population += 0.01 * Population  # Slow growth during lag phase
        elif t < lag_phase_duration + exp_phase_duration:
            Population += Growth_rate * Population  # Rapid growth during exponential phase
        else:
            Population += Growth_rate * Population * (1 - Population / Carrying_capacity)  # Slowing down as it reaches carrying capacity
        # Ensure population doesn't exceed the carrying capacity
        if Population > Carrying_capacity:
            Population = Carrying_capacity
        population_list.append(Population)
    return population_list
# Parameters for the simulation
time_length = 100  # Number of time steps
initial_population = 100  # Initial population size
carrying_capacity = 100000  # Carrying capacity
growth_rate = 0.1  # Growth rate
# Create a list to hold all 100 growth curves
population_list = []
# Generate 100 different growth curves
for i in range(100):
    growth_curve = logistic_growth_curve(initial_population, carrying_capacity, growth_rate, time_length, lag_phase_duration=None, exp_phase_duration=None)
    population_list.append(growth_curve)
# Create a DataFrame to store the 100 growth curves
data_frame = pd.DataFrame(population_list).transpose()
# Label the columns as ‘growth curve_1', ..., ‘growth curve_100'
data_frame.columns = [f"growth curve_{i+1}" for i in range(100)]
# Add a 'Time' column for time steps
data_frame['Time'] = list(range(time_length))
# Display the DataFrame
print(data_frame)
#______________________________________________________________________________________________________________
def time_to_reach_80percent(initial_population, carrying_capacity, growth_rate, time_length):
    population = initial_population  # Initialize population
    target_growth = 0.8 * carrying_capacity  # 80% of carrying capacity(maximum growth)
    for t in range(time_length):
        # Apply logistic growth formula here
        population += growth_rate * population * (1 - population / carrying_capacity)
        # Check if population has reached or exceeded 80% of carrying capacity
        if population >= target_growth:
            return t  # Return the time step when population reaches 80%
    return None  # If it never reaches 80%, return None output
# Example usage:
time_length = 100
initial_population = 100
carrying_capacity = 1000
growth_rate = 0.1
time_to_80percent= time_to_reach_80percent(initial_population, carrying_capacity, growth_rate, time_length)
print("Time to reach 80% of carrying capacity:", time_to_80percent)
#____________________________________________________________________________________________________________________
# Function to calculate Hamming distance
def hamming_distance(word1, word2):
    """
    This function counts how many letters are different between two words.
    Since both words have the same length, we compare them directly.
    """
    difference_count = 0  # Start with zero differences
    # Loop through each index position in the words
    for i in range(len(word1)):  # `i` is the position (0,1,2,...)
        if word1[i] != word2[i]:  # Compare letters at the same position
            difference_count += 1  # If different, increase the count
    return difference_count  # Return the total number of differences
# Define Slack and Twitter usernames
slack_name = "Favour"  # My Slack username
twitter_name = "Fabs24"  # My Twitter username
# Calculate the Hamming distance
distance = hamming_distance(slack_name, twitter_name)
# Show the result
print(f"The Hamming distance between '{slack_name}' and '{twitter_name}' is: {distance}")
