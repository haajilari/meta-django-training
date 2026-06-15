from django import forms
from .models import InputForm
SHIFT = (
    ("1", "Morning"),
    ("2", "Afternoon"),
    ("3", "Evening")
)
class LogForm(forms.ModelForm):
    class Meta:
        model = InputForm
        fields = "__all__"