from django.urls import path, include
from profiles_api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('user', views.UserViewSet)
router.register('feed', views.UserFeedViewset)

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view(), name='hello-api-view'),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
