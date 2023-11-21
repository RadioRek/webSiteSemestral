# Generated by Django 4.2.1 on 2023-06-10 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaperShop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Producto',
            new_name='Product',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='categoria',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='imagen',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='precio',
            new_name='price',
        ),
    ]