# Generated by Django 5.0.7 on 2024-07-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0002_menuitem_category_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=150),
        ),
    ]
