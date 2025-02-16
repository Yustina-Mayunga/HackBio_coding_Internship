# Stage01-task Final Solution.

## Overview
This project consists of three key functionalities implemented in Python:
1. Codon to Protein Dictionary – A tool for translating DNA sequences into protein sequences.
2. Logistic Population Growth Curve – A simulation of population growth with randomized lag and exponential phases.
3. Hamming Distance Calculation – A method to measure the difference between two strings, such as Twitter and Slack usernames.

---

## 1. Creating a Codon Dictionary

### Description
This functionality provides a dictionary that maps codons to their corresponding amino acids. Using this dictionary, a function is designed to transcribe a given DNA sequence into mRNA then translate a protein sequence by reading triplet codons and stopping translation when a stop codon is encountered.

---

## 2. Logistic Population Growth Curve

### Description
This function models a logistic population growth curve, incorporating:
- A lag phase with slow initial growth.
- An exponential phase with rapid population increase.
- A stationary phase where growth slows as it approaches the carrying capacity.

To add variability, the durations of the lag and exponential phases are randomized. The function can generate multiple growth curves, which are stored in a pandas DataFrame for further analysis or visualization.

---

## 3. Hamming Distance Calculation

### Description
The Hamming distance measures the number of differing characters between two strings of equal length. This function is particularly useful for comparing usernames, genetic sequences, or detecting errors in encoded data. The function iterates through each character in the two words and counts the number of mismatches.

---

## Installation & Dependencies
### Requirements
- Python 3.x
- Pandas (for data handling in the logistic growth simulation)

### Installation
To install the required dependencies, run:
```bash
pip install pandas
```

---

## Usage
- Use the codon dictionary to translate DNA sequences into protein sequences.
- Simulate different logistic growth curves with randomized phases for dynamic modeling.
- Compute the Hamming distance between two strings for comparison purposes.

Each function can be executed independently or integrated into a larger analysis pipeline.

---

## Author
Developed by Joshua Essien, Karimat Busari, Favour Fabuyi, Nassoufi Chaimae and Yustina Mayunga. 

---
