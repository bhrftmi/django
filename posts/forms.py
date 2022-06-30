from django import forms

class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    is_enabled = forms.BooleanField()
    publish_date = forms.DateField()