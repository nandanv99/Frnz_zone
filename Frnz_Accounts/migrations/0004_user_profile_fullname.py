# Generated by Django 3.2.13 on 2022-06-07 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frnz_Accounts', '0003_auto_20220607_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='fullname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]