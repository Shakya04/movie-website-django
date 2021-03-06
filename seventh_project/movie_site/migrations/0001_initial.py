# Generated by Django 3.2.7 on 2021-10-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=5000)),
                ('image', models.ImageField(upload_to='movies')),
                ('genre', models.CharField(choices=[('A', 'ACTION'), ('C', 'COMEDY'), ('R', 'ROMANCE'), ('S', 'SCI-FI')], max_length=1)),
                ('category', models.CharField(choices=[('TR', 'TOP RATED'), ('MW', 'MOST WATCHED'), ('RA', 'RECENTLY ADDED')], max_length=2)),
                ('director', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('average_rating', models.FloatField()),
            ],
        ),
    ]
