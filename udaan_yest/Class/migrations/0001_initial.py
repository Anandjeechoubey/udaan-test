# Generated by Django 3.2.7 on 2021-09-08 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(1, 'Gym'), (2, 'Yoga'), (3, 'Dance')], default=(1, 'Gym'), max_length=255)),
                ('capacity', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
