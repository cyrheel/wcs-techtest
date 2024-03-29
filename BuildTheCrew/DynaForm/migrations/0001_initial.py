# Generated by Django 3.2.9 on 2021-11-17 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Argonaute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('add_date', models.DateTimeField(verbose_name='Date added')),
            ],
        ),
        migrations.CreateModel(
            name='Adjectifs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adj_text', models.CharField(max_length=64)),
                ('argonaute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DynaForm.argonaute')),
            ],
        ),
    ]
