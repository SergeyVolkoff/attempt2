# Generated by Django 3.2.3 on 2024-09-25 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_alter_shoppingbyrecipe_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingrrecipe', to='recipes.ingredient', verbose_name='Ингредиент'),
        ),
    ]
