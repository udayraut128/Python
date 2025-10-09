from django.shortcuts import render
from .forms import TitanicForm
import pickle
import os
import numpy as np

# Load model once when the server starts
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'titanic_model.pkl')

try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None
    print(f"❌ Titanic model not found at: {MODEL_PATH}")

def predict_view(request):
    result = None
    if request.method == 'POST':
        form = TitanicForm(request.POST)
        if form.is_valid():
            try:
                pclass = int(form.cleaned_data['pclass'])
                sex = int(form.cleaned_data['sex'])
                age = float(form.cleaned_data['age'])

                if model:
                    prediction = model.predict([[pclass, sex, age]])
                    result = 'Survived' if prediction[0] == 1 else 'Did not survive'
                else:
                    result = "Model not loaded. Please check the server logs."

            except Exception as e:
                result = f"Error during prediction: {str(e)}"
    else:
        form = TitanicForm()

    return render(request, 'index.html', {'form': form, 'result': result})
