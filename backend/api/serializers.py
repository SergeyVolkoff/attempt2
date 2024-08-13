from rest_framework import serializers, status
from rest_framework.relations import PrimaryKeyRelatedField
from djoser.serializers import UserSerializer
from django.forms import ValidationError
from drf_extra_fields.fields import Base64ImageField

from recipes.models import (Tag,
                            Ingredient,
                            Users,
                            Recipe,
                            RecipeIngredient,
                            ShoppingByRecipe,
                            FavoriteRecipes,
                        )
from users.models import Users, Subscriptions
from .validators import username_validator


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')


class IngredientSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'units_measure')
        read_only_fields = ('__all__',)

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators = (username_validator,)
    )

    class Meta:
        model = Users
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'is_subscribed',
                  'id')

class RecipeSerializerGet(serializers.ModelSerializer):
    name = serializers.CharField()
    print(name)
    tags = TagSerializer(many=True)
    ingredients = IngredientSerializer(many=True,)
    # author = FoodUserSerializer(read_only=True)
    # ingredient = serializers.SerializerMethodField()
    # is_favorited = serializers.SerializerMethodField()
    # is_in_shopping_cart = serializers.SerializerMethodField()
    image = Base64ImageField()
    
    class Meta:
        model = Recipe
        fields = ('id', 'tags','ingredients',
                  'name', 'image'
                  )
