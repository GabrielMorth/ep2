from django.forms import ModelForm
from django import forms
from .models import Post, Comment, Category

class CreateAviaoForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class UpdateAviaoForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'autor',
            'text',
        ]
        labels = {
            'autor': 'Usuário',
            'text': 'Comentário',
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')
