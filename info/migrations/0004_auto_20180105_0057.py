# Generated by Django 2.0 on 2018-01-04 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20180105_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='adress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.Adress'),
        ),
    ]