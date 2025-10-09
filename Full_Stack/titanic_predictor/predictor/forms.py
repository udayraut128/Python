from django import forms

class TitanicForm(forms.Form):
    PCLASS_CHOICES = [(1, '1st'), (2, '2nd'), (3, '3rd')]
    SEX_CHOICES = [(0, 'Male'), (1, 'Female')]

    pclass = forms.ChoiceField(choices=PCLASS_CHOICES, label="Passenger Class")
    sex = forms.ChoiceField(choices=SEX_CHOICES, label="Sex")
    age = forms.FloatField(label="Age")
