# Generated by Django 5.0 on 2023-12-16 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='Название фирменного знака')),
                ('slug', models.SlugField(max_length=225, unique=True, verbose_name='Url')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Торговая марка',
                'verbose_name_plural': 'Торговые марки',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='Имя категории')),
                ('slug', models.SlugField(max_length=225, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Имя покупателя')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=225, verbose_name='Адрес')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=225, unique=True, verbose_name='Url')),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Старая цена')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'No'), (1, 'Yes')], default=1, verbose_name='Статус')),
                ('depart', models.CharField(blank=True, max_length=225, verbose_name='Упаковка')),
                ('article', models.CharField(blank=True, max_length=225, verbose_name='Артикуль')),
                ('grade', models.CharField(blank=True, max_length=225, verbose_name='Класс')),
                ('height', models.CharField(blank=True, max_length=100, verbose_name='Высота')),
                ('flower_size', models.CharField(blank=True, max_length=225, verbose_name='Размер цветка')),
                ('flowering_period', models.CharField(blank=True, max_length=100, verbose_name='Период')),
                ('landing_place', models.CharField(blank=True, max_length=100, verbose_name='Место посадки')),
                ('frost_resistance', models.CharField(blank=True, max_length=100, verbose_name='Морозостойкость')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flower.brand', verbose_name='Фирменный знак')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-id'],
            },
        ),
    ]
