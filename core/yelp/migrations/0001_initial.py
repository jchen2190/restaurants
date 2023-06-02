# Generated by Django 4.2.1 on 2023-06-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200, null=True)),
                ('address3', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('image_url', models.URLField(blank=True)),
                ('category', models.CharField(max_length=100)),
                ('review_count', models.IntegerField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=10)),
                ('rating', models.FloatField()),
                ('phone', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]