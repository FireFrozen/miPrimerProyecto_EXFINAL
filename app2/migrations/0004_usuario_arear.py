# Generated by Django 4.2.16 on 2024-12-06 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='areaR',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app2.area'),
        ),
    ]