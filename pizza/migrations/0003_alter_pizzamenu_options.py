# Generated by Django 4.0.4 on 2022-06-22 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_alter_pizzamenu_options_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizzamenu',
            options={'ordering': ['price'], 'verbose_name_plural': 'Pizza Menu'},
        ),
    ]