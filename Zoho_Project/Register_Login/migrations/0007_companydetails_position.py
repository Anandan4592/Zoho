# Generated by Django 4.2 on 2023-12-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0006_zohomodules'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetails',
            name='position',
            field=models.CharField(blank=True, default='company', max_length=255, null=True),
        ),
    ]