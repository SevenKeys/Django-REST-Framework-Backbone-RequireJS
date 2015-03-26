from rest_framework.routers import DefaultRouter
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token


# Create a router and register our viewsets with it.
router = DefaultRouter(trailing_slash=False)
router.register(r'articles', views.ArticleViewSet)
router.register(r'users', views.UserViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='rest_framework/index.html')),
    url(r'^api/', include(router.urls)),
	url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]