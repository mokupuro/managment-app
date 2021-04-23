from django import forms
from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'undergraduate', 'cource', 'obtainedu_unit')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'記入例：山田 太郎'}),
            'undergraduate': forms.RadioSelect(),
        }