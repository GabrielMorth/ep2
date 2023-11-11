from django.forms import ModelForm
from .models import Post, Comment

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