# CERN Dimuon Collision Analysis

A simple data science and machine learning project using dimuon collision data from the CERN Open Data Portal.

## Project Overview

This project explores CERN dimuon collision data using Python.

The main goals are to:

- Explore and understand the collision dataset
- Analyze particle and invariant mass distributions
- Visualize a dimuon event in 3D using momentum components
- Classify the `Type2` variable using basic machine learning models
- Compare the performance of different classification methods

This project was developed for educational purposes as part of a Data Science and Machine Learning bootcamp.

## Dataset

The dataset used in this project is obtained from the CERN Open Data Portal:

**Dataset:** `MuRun2010B_0.csv`

The dataset contains 10,000 collision events and includes variables such as:

- Particle energies
- Momentum components (`px`, `py`, `pz`)
- Transverse momentum (`pt`)
- Pseudorapidity (`eta`)
- Azimuthal angle (`phi`)
- Particle charge
- Invariant mass (`M`)
- Particle/event type information

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Data Analysis

The project includes:

- Dataset inspection and preprocessing
- Missing value analysis
- Descriptive statistics
- `Type2` class distribution analysis
- Invariant mass distribution visualization
- Comparison of invariant mass distributions between `Type2` classes
- 3D visualization of muon momentum vectors

## Machine Learning

Two classification algorithms are used:

### Logistic Regression

Logistic Regression is used as a simple baseline classification model.

### K-Nearest Neighbors (KNN)

KNN is used as a second classification approach to compare its performance with Logistic Regression.

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## 3D Collision Visualization

A selected dimuon event is visualized in three dimensions using the momentum components:

`px`, `py`, and `pz`

The visualization represents the momentum directions of the two muons originating from the collision point.

## How to Run

Install the required libraries:

pip install pandas numpy matplotlib scikit-learn jupyter

Then open the Jupyter Notebook and run the cells in order.

The dataset is loaded directly from the CERN Open Data Portal, so it does not need to be stored in the repository.

## Disclaimer

This project is intended for educational and introductory data science purposes.

It does not attempt to reproduce an official CERN physics analysis or claim any new physics discovery.

## Author

Elif Kübra Sağlam

Computer Engineering Student
