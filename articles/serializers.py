from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.first_name + ' ' + obj.author.last_name

    class Meta:
        model = Article


class ArticleListSerializer(ArticleSerializer):

    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.first_name + ' ' + obj.author.last_name

    class Meta(ArticleSerializer.Meta):
        fields = ('id', 'title', 'url', 'small_text', 'publication_date', 'author')
