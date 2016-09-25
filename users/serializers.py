# -*- coding: utf-8 -*-
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.contrib.auth.models import User


class UserBlogListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    blog_url = serializers.SerializerMethodField()
    articles = serializers.SerializerMethodField()

    def get_blog_url(self, obj):
        url = 'http://127.0.0.1:8000/api/1.0/blog/'
        return url + obj.username

    def get_articles(self, obj):
        return obj.articles.count()

class UserListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()


class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.password = make_password(validated_data.get('password'))
        instance.email = validated_data.get('email')
        instance.save()
        return instance

    def validate_username(self, username):
        if (self.instance is None or self.instance.username != username) \
                and User.objects.filter(username=username).exists():
            raise ValidationError("El nombre de usuario {0} ya está siendo utilizado".format(username))
        return username

    def validate_email(self, email):
        if (self.instance is None or self.instance.email != email) \
                and User.objects.filter(email=email).exists():
            raise ValidationError("El e-mail {0} ya está siendo utilizado".format(email))
        return email.lower()




