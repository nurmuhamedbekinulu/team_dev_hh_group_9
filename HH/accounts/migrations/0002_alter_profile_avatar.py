# Generated by Django 4.2 on 2023-04-21 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='/Default.png', null=True, upload_to='uploads', verbose_name='Аватар'),
        ),
    ]
