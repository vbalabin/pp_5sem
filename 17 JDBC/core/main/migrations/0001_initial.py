# Generated by Django 3.2.7 on 2021-10-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=64)),
                ('position', models.TextField(max_length=64)),
                ('enlisted', models.DateField()),
                ('department', models.TextField(max_length=64)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
