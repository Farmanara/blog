# Generated by Django 3.2.4 on 2021-06-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['position'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='position',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Visible'),
        ),
    ]
