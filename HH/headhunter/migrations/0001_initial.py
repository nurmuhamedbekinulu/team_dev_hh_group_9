# Generated by Django 4.2 on 2023-04-18 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название вакансии')),
                ('salary', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Заработная плата')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание вакансии')),
                ('experience', models.FloatField(verbose_name='Опыт работы')),
                ('category', models.TextField(choices=[('IT', 'IT'), ('DESIGN', 'Дизайн'), ('MANAGEMENT', 'Менеджмент'), ('MEDICINE', 'Медицина'), ('ENGINEERING', 'Инженерное дело'), ('ART', 'Искусство'), ('TRANSPORT', 'Транспорт'), ('MARKETING', 'Маркетинг'), ('TRADE', 'Торговля'), ('ECONOMY', 'Экономика')], verbose_name='Категория вакансии')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=False, verbose_name='Скрыть вакансию')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL, verbose_name='Работодатель')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['-updated_at'],
            },
        ),
    ]