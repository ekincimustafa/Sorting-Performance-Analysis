# Algorithmic Sorting and Performance Analysis

This repository contains the implementation and performance analysis of various sorting algorithms developed for the optimization of a fictional city's (Algora) critical logistics network. 

The project focuses on implementing classic sorting algorithms from scratch in Python, performing a two-level sorting process based on warehouse priority levels and package counts, and comparing their execution efficiencies. This project was developed as part of the BBM103 course assignments.

## 🚀 Features

- **Custom Pseudorandom Number Generator (PRNG):** Generates reproducible logistics datasets without relying on external random libraries.
- **Two-Level Sorting Mechanism:** Sorts warehouses first by `Priority_Level` and then by `Package_Count`.
- **Algorithm Implementations:** 
  - Bubble Sort
  - Merge Sort
  - Quick Sort
- **Performance Tracking:** Counts iterations (for Bubble Sort) and recursive steps (for Merge and Quick Sorts) to analyze algorithm efficiency.
- **Automated Verification:** Compares the outputs of Merge Sort and Quick Sort against Bubble Sort to ensure absolute accuracy (Tur Bo Grader compliant).

## 🛠️ Tech Stack
- **Language:** Python 3.8
- **Libraries:** `os` (for random seed generation)

## 📦 Dataset Description
The algorithm processes a synthetic dataset formatted as follows:
- `Warehouse_ID`: A unique identifier for each warehouse (e.g., WH-001).
- `Priority_Level`: Integer values representing the urgency of the warehouse (1-5).
- `Package_Count`: Total number of packages to be processed.

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/ekincimustafa/Sorting-Performance-Analysis.git](https://github.com/ekincimustafa/Sorting-Performance-Analysis.git)
   ```
2. Navigate to the project directory:
   ```bash
   cd Sorting-Performance-Analysis
   ```
3. Run the Python script:
   ```bash
   python hw_05.py
   ```
4. The script will read (or generate) the input data from `hw05_input.csv` and generate an output file named `hw05_output.txt` containing the sorted results and performance metrics.

## 📊 Performance Metrics Example

The program evaluates the algorithms based on iteration/recursive step counts. Example metric output:
```text
Bubble priority sort iteration count: 45
Merge priority sort n_of right array is smaller than left: 11
Quick priority sort recursive step count: 3
```
*Note: Merge and Quick sorts significantly outperform Bubble Sort in larger datasets, as demonstrated in the generated metrics.*