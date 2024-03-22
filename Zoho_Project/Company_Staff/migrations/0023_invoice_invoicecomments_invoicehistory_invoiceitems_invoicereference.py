# Generated by Django 3.2.23 on 2024-03-20 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0017_alter_trialperiod_interested_in_buying'),
        ('Company_Staff', '0022_journal_journalcomment_journalentry_journalrecievedidmodel_journaltransactionhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(blank=True, max_length=220, null=True)),
                ('customer_billingaddress', models.CharField(blank=True, max_length=220, null=True)),
                ('customer_GSTtype', models.CharField(blank=True, max_length=220, null=True)),
                ('customer_GSTnumber', models.CharField(blank=True, max_length=220, null=True)),
                ('customer_place_of_supply', models.CharField(blank=True, max_length=220, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('expiration_date', models.DateField(auto_now_add=True, null=True)),
                ('reference_number', models.IntegerField(blank=True, null=True)),
                ('invoice_number', models.CharField(blank=True, max_length=220, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=220, null=True)),
                ('cheque_number', models.CharField(blank=True, max_length=220, null=True)),
                ('UPI_number', models.CharField(blank=True, max_length=220, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=220, null=True)),
                ('description', models.CharField(blank=True, max_length=220, null=True)),
                ('terms_and_condition', models.CharField(blank=True, max_length=220, null=True)),
                ('document', models.FileField(null=True, upload_to='images/')),
                ('sub_total', models.FloatField(blank=True, default=0.0, null=True)),
                ('CGST', models.FloatField(blank=True, default=0.0, null=True)),
                ('SGST', models.FloatField(blank=True, default=0.0, null=True)),
                ('IGST', models.FloatField(blank=True, default=0.0, null=True)),
                ('tax_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('shipping_charge', models.FloatField(blank=True, default=0.0, null=True)),
                ('adjustment', models.FloatField(blank=True, default=0.0, null=True)),
                ('grand_total', models.FloatField(blank=True, default=0.0, null=True)),
                ('advanced_paid', models.FloatField(blank=True, default=0.0, null=True)),
                ('balance', models.FloatField(blank=True, default=0.0, null=True)),
                ('status', models.CharField(blank=True, max_length=220, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.customer')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('payment_terms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.company_payment_term')),
            ],
        ),
        migrations.CreateModel(
            name='invoiceReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(blank=True, max_length=220, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.staffdetails')),
            ],
        ),
        migrations.CreateModel(
            name='invoiceitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsn', models.CharField(blank=True, max_length=220, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.FloatField(blank=True, default=0.0, null=True)),
                ('tax_rate', models.FloatField(blank=True, default=0.0, null=True)),
                ('discount', models.FloatField(blank=True, default=0.0, null=True)),
                ('total', models.FloatField(blank=True, default=0.0, null=True)),
                ('Items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.items')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.invoice')),
                ('logindetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='invoiceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, max_length=220, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.invoice')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='invoicecomments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.invoice')),
            ],
        ),
    ]