# Generated by Django 3.2.3 on 2024-09-24 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_favoriterecipe_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingbyrecipe',
            options={'default_related_name': 'recipe_shopping', 'verbose_name': 'Рецепт для покупок', 'verbose_name_plural': 'Рецепты для покупок'},
        ),
        migrations.RemoveConstraint(
            model_name='shoppingbyrecipe',
            name='unique_user_recipe',
        ),
    ]
