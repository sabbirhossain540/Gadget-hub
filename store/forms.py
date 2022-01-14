from dataclasses import field
from django import forms
from store.models import ReviewRating

class ReviewForms(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']