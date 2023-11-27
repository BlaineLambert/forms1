from django import forms

class Hey_form(forms.Form):
    word = forms.CharField()

class Age_form(forms.Form):
    current_year = forms.IntegerField()
    year_born = forms.IntegerField()

class Order_form(forms.Form):
    burbers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()