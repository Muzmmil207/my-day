from django import forms
from .models import chart, index


class ChartForm(forms.ModelForm):

    class Meta:
        model = chart
        fields = ('name', 'description', 'choices')
        widgets = {
            # 'user': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'choices': forms.Select(attrs={'class': 'form-control'}),
        }


class IndexForm(forms.ModelForm):

    class Meta:
        model = index
        #fields = '__all__'
        fields = ('int_value', 'time_value')

        # widgets = {
        #     'int_value': forms.TextInput(attrs={'class': 'form-control'}),
        #     'time_value': forms.TextInput(attrs={'class': 'form-control'}),
        # }
