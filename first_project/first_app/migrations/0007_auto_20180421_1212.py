# Generated by Django 2.0.2 on 2018-04-21 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_auto_20180421_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
