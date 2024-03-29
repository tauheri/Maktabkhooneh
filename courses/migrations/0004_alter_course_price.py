# Generated by Django 4.2.2 on 2023-06-23 23:47

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[courses.models.validate_course_price]),
        ),
    ]
