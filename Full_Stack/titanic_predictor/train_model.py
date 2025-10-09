import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Simple preprocessing
df = df[['Survived', 'Pclass', 'Sex', 'Age']]
df.dropna(inplace=True)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

X = df[['Pclass', 'Sex', 'Age']]
y = df['Survived']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
model_dir = os.path.join('predictor', 'model')
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, 'titanic_model.pkl')

with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"✅ Model saved to: {model_path}")
