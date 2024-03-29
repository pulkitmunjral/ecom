# Generated by Django 4.2.11 on 2024-03-16 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storefront',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(unique=True)),
                ('description', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storefronts', to='clients.company')),
            ],
        ),
    ]
