from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.Field(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(\
					view_name='article-highlight', format='html')

	class Meta:
		model = Article
		fields = ('id', 'url', 'created', 'title', 'description',\
		 'language', 'owner', 'highlight',)

	


class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(queryset=Article.objects.all(), 
    										many=True, view_name='article-detail')

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'articles')


