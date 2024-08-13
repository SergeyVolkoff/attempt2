from django.urls import include, path, re_path
from rest_framework import routers
from djoser import views as djoser_views
from rest_framework.routers import DefaultRouter

from .views import (
                    UserViewSet,
                    TagViewSet,
                    IngredientViewSet,
                    RecipeViewSet
                    )
app_name = 'api'
router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'users', UserViewSet, basename='users')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')


urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    
]