# Generated by Django 4.2.1 on 2023-06-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaperShop', '0005_rename_lastname_users_user_remove_users_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]