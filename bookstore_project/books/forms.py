from django import forms
from books.models import Review


class ReviewForm(forms.ModelForm):
   body = forms.CharField(widget = forms.Textarea(attrs={'class':"border rounded w-full p-2" , 'placeholder':"write your review here"}))
   image = forms.ImageField(required=False)
   
   class Meta:
      model = Review
      fields = ['body', 'image']
   