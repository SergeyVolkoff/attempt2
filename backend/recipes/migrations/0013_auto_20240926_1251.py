# Generated by Django 3.2.3 on 2024-09-26 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0012_auto_20240926_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriterecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='recipes.recipe', verbose_name='Избранный рецепт'),
        ),
        migrations.AlterField(
            model_name='favoriterecipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='shoppingbyrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_recipe', to='recipes.recipe', verbose_name='Список покупок'),
        ),
        migrations.AlterField(
            model_name='shoppingbyrecipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь покупок'),
        ),
    ]
