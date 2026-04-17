# Gender Detection ML Model

A machine learning project that predicts a person's gender based on their physical characteristics (height, weight, and age) using Logistic Regression.

## Problem Statement

Given three input features:
- **Height** (in cm)
- **Weight** (in kg)
- **Age** (in years)

Predict the **Gender** (Male or Female)

## Dataset

The project uses a gender classification dataset containing:
- Features: height, weight, age
- Target: gender (male/female)


## Installation

1. Clone the repository:
```bash
git clone https://github.com/ahmed4mohamed4/Gender-detection-ML-model.git
cd Gender-detection-ML-model
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

4. Install requirements:
```bash
pip install -r requirements.txt
```

## Model Details

- **Algorithm**: Logistic Regression
- **Features**: height, weight, age
- **Target**: gender (encoded as 1 for Male, 0 for Female)
- **Train-Test Split**: 80-20

## Usage

### Running the Notebook

1. Start Jupyter:
```bash
jupyter notebook
```

2. Open `model/main.ipynb` and run all cells

### Making Predictions

After training the model, you can make predictions by providing height, weight, and age:

```python
height = float(input("Enter height: "))
weight = float(input("Enter weight: "))
age = float(input("Enter age: "))
result = model.predict([[height, weight, age]])
print("Predicted Gender:", "Male" if result[0] == 1 else "Female")
```

## Workflow

1. **Data Loading & Exploration**: Load the dataset and check for missing values
2. **Data Preprocessing**: Clean column names and encode gender values
3. **Data Visualization**: Analyze distributions and relationships between features and gender
4. **Model Training**: Split data and train Logistic Regression model
5. **Model Evaluation**: Calculate accuracy on test set
6. **Prediction**: Make predictions on new data

## Authors
- Nourhan Medhat 245365
- Menna Allah Mustafa 245359
- Sara Mohamed 245341
- Ahmed Mohamed 245318