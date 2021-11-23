from django import forms
from blog import models

class BlogThreadForm(forms.Form):
    blog_thread = forms.ModelChoiceField(models.BlogThread.objects, required=False)