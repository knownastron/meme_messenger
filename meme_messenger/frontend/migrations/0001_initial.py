# Generated by Django 2.1.5 on 2019-02-06 16:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=1)),
                ('area', models.CharField(max_length=3)),
                ('phone_number', models.CharField(max_length=7)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='phonenumber',
            unique_together={('country', 'area', 'phone_number')},
        ),
    ]
