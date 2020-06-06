# Generated by Django 3.0.7 on 2020-06-04 11:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='form',
            name='h_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Hospital'),
            preserve_default=False,
        ),
    ]
