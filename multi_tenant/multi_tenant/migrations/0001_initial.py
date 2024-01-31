# Generated by Django 4.2 on 2024-01-31 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subdomain', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TenantAwareModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multi_tenant.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multi_tenant.tenantawaremodel')),
                ('name', models.CharField(max_length=255)),
            ],
            bases=('multi_tenant.tenantawaremodel',),
        ),
    ]
