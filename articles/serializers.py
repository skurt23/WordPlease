from rest_framework import serializers

class UserBlogListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    author = serializers.CharField()
    blog_url = serializers.SerializerMethodField()
    articles = serializers.SerializerMethodField()

    def get_blog_url(self, obj):
        url = 'http://127.0.0.1:8000/blogs/'
        return url + obj.author.username

    def get_articles(self, obj):
        return obj.article.length
