# Generated by Django 5.0 on 2024-04-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0025_eway_eway_bill_history_eway_bill_items_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eway_bill_transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport', models.CharField(blank=True, max_length=220, null=True)),
            ],
        ),
    ]
