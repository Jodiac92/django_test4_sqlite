# Generated by Django 2.2.7 on 2019-11-18 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
