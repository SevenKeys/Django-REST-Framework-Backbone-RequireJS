from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from users.models import Article
from users.serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from users.permissions import IsOwnerOrReadOnly



class ArticleViewSet(viewsets.ModelViewSet):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        article = self.get_object()
        return Response(article.highlighted)

    def pre_save(self, obj):
        obj.owner = self.request.user



class UserViewSet(viewsets.ReadOnlyModelViewSet):

    """API endpoint for listing users."""

    queryset = User.objects.all()
    serializer_class = UserSerializer