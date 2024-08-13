from django.contrib import admin

from recipes.models import (Tag,
                            Ingredient,
                            Users,
                            Recipe,
                            RecipeIngredient,)



class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'slug'
    )

class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'units_measure'
    )

class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'in_favorited'
    )

admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Users)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)