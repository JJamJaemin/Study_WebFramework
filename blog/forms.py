from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:             #ModelForm에서 상속받은 경우에 있어야함
        model = Comment
        fields = ('content', )