from django import forms


class EmployeeApplicationForm(forms.Form):
    name = forms.CharField()
    dateOfBirth = forms.DateField()
    position = forms.CharField()
    salary = forms.DecimalField()
