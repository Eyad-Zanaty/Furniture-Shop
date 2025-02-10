from django import forms
from Home.models import Rating, Comments

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'comment'] 
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Full Name"
            }),
            "comment": forms.Textarea(attrs={
                "class": "form-control",
                "rows": "1",
                "placeholder": "Message",
            }),
        }



class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['name', 'rate'] 
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Full Name"
            }),
            "rate": forms.Textarea(attrs={
                "class": "form-control",
                "rows": "1",
                "placeholder": "Review",
            }),
        }
