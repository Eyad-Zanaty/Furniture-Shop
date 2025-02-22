# Generated by Django 4.2.17 on 2025-02-10 20:36

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
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carts', models.ManyToManyField(blank=True, to='Home.cart')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rate', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Rebly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(max_length=500)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='products/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('orders', models.IntegerField(default=0)),
                ('color', models.CharField(choices=[('Red', 'Red'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Black', 'Black'), ('White', 'White'), ('Blue', 'Blue')], max_length=25)),
                ('breif', models.TextField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, max_length=750, null=True)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('depth', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('quality_checking', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=3)),
                ('freshness_duration', models.DateField(auto_now=True)),
                ('packeting', models.CharField(choices=[('Without touch of hand', 'Without touch of hand'), ('With touch of hand', 'With touch of hand')], max_length=50)),
                ('box_contains', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('comment', models.ManyToManyField(blank=True, to='Home.comments')),
                ('rating', models.ManyToManyField(blank=True, to='Home.rating')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.profile'),
        ),
        migrations.AddField(
            model_name='comments',
            name='reply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.rebly'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.products'),
        ),
    ]
