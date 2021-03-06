# Generated by Django 3.1.4 on 2020-12-24 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=255)),
                ('employee_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='company.city')),
                ('employee_title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='company.employeetitle')),
            ],
        ),
    ]
