# Generated by Django 3.2.3 on 2024-09-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_subscriptions_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/avatar', verbose_name='Аватар'),
        ),
    ]
