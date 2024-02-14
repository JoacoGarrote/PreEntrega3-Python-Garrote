from django import forms

class FormEmpleado(forms.Form):
    nombre = forms.CharField()
    apellido = forms.IntegerField()
    trabajo = forms.IntegerField()