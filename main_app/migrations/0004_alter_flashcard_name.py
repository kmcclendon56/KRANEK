# Generated by Django 4.1 on 2022-09-06 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_deck_flashcards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
