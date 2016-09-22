from articles.models import Article
from django.forms import ModelForm


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        exclude = ['author', 'like']