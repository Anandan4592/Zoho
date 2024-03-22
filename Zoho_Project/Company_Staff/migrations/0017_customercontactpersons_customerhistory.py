# Generated by Django 3.2.23 on 2024-02-28 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0017_alter_trialperiod_interested_in_buying'),
        ('Company_Staff', '0016_customer_customer_comments_table_customer_doc_upload_table_customer_remarks_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, max_length=220, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.customer')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerContactPersons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=220, null=True)),
                ('first_name', models.CharField(blank=True, max_length=220, null=True)),
                ('last_name', models.CharField(blank=True, max_length=220, null=True)),
                ('email', models.EmailField(blank=True, max_length=220, null=True)),
                ('work_phone', models.CharField(blank=True, max_length=220, null=True)),
                ('mobile', models.CharField(blank=True, max_length=220, null=True)),
                ('skype', models.CharField(blank=True, max_length=220, null=True)),
                ('designation', models.CharField(blank=True, max_length=220, null=True)),
                ('department', models.CharField(blank=True, max_length=220, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.customer')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
    ]