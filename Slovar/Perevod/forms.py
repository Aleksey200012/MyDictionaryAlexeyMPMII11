from django import forms

class AddWordForm(forms.Form):
    word_en = forms.CharField(label="Слово на английском", max_length=100)
    word_ru = forms.CharField(label="Перевод на русском", max_length=100)