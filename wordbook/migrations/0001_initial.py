# Generated by Django 5.1.4 on 2024-12-13 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_word', models.CharField(max_length=50)),
                ('ja_word', models.CharField(max_length=50)),
                ('en_to_ja_correct_count', models.PositiveIntegerField(default=0)),
                ('en_to_ja_incorrect_count', models.PositiveIntegerField(default=0)),
                ('ja_to_en_correct_count', models.PositiveIntegerField(default=0)),
                ('ja_to_en_incorrect_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]