from django import forms


class MyForm(forms.Form):
    choice = [
        ('kdin','kdin'),
        ('2','other'),
        ('3', 'other'),
        ('4', 'other'),
    ]
    model = forms.ChoiceField(choices=choice, label_suffix="", widget=forms.Select(attrs={'class': 'form-control'}))
    flow = forms.FloatField(label='',label_suffix="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Flow'}))
    hhead = forms.FloatField(label='',label_suffix="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Head'}))

class SQLFileSearchForm(forms.Form):
    sql_file = forms.FileField(label='ไฟล์ SQL')

