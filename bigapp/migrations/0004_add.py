# Generated by Django 4.0.1 on 2022-01-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigapp', '0003_question_q10_question_q11_question_q12_question_q13_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=20)),
                ('msg', models.CharField(max_length=40)),
            ],
        ),
    ]
