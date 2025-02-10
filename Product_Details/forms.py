from django import forms
from Home.models import Rating

class RatingForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "name": "name",
            "placeholder": "Your Full Name"
        })
    )
    rate = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "name": "message",
            "rows": "1",
            "placeholder": "Review"
        })
    )
    class Meta:
        model= Rating
        fields= '__all__'