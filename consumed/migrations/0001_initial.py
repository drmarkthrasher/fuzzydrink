# Generated by Django 2.1.3 on 2018-11-29 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_type', models.CharField(choices=[('b', 'Beer'), ('w', 'Wine'), ('s', 'Shot'), ('c', 'Cocktail')], default='b', max_length=1)),
                ('description', models.TextField()),
                ('volume', models.IntegerField(default=0)),
                ('alcohol_content', models.IntegerField(default=0)),
                ('consumption_date', models.DateField()),
                ('consumption_time', models.TimeField()),
            ],
            options={
                'ordering': ['description'],
            },
        ),
    ]
