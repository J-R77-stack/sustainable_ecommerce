# Generated by Django 3.2 on 2022-06-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_productreviews_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stars',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]