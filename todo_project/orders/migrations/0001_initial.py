# Generated by Django 4.2.4 on 2023-08-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=255)),
                ('date_due', models.DateField()),
                ('time_due', models.TimeField()),
                ('is_done', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['date_due', 'time_due', '-id'],
            },
        ),
    ]
