# Generated by Django 5.0 on 2024-04-08 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0026_eway_bill_transportation'),
        ('Register_Login', '0017_alter_trialperiod_interested_in_buying'),
    ]

    operations = [
        migrations.AddField(
            model_name='eway_bill_transportation',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails'),
        ),
    ]
