import rest_framework.permissions

from django.db.models import Sum
from django.forms import ValidationError
from django.http import Http404, HttpResponse
from djoser.views import UserViewSet
from django.shortcuts import get_object_or_404

from requests import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

# from .pagination import DefaultPagination

# from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from .serializers import (
    TagSerializer,
    IngredientSerializer,
    UserSerializer,
    RecipeSerializerGet,
    # IngredientRecipeSerializer,
    # FoodUserSerializer,
    # RecipeSerializerSet,
    # ShoppingByRecipeSerializer,
    # FavoriteRecipeSerializer
    )
from recipes.models import (
    Tag,
    Ingredient,
    Recipe,
    RecipeIngredient,
    ShoppingByRecipe,
    FavoriteRecipes
    )

from users.models import (
    Users
)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    # permission_classes = (IsAdminOrReadOnly,)

class UserViewSet(UserViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializerGet
    # pagination_class = DefaultPagination
    # permission_classes = (IsOwnerOrReadOnly,)