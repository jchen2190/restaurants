# Generated by Django 4.2.1 on 2023-06-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yelp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_field', models.CharField(max_length=200)),
            ],
        ),
    ]
