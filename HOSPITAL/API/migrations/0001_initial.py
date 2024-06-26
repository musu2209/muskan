# Generated by Django 4.2.11 on 2024-06-04 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DEPARTMENT',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DOCTOR',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=100)),
                ('d_age', models.IntegerField()),
                ('d_gender', models.CharField(max_length=10)),
                ('d_mobile', models.IntegerField(max_length=10)),
                ('d_department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PATIENT',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=100)),
                ('p_age', models.IntegerField()),
                ('p_gender', models.CharField(max_length=10)),
                ('p_mobile', models.IntegerField(max_length=10)),
                ('p_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='REPORT',
            fields=[
                ('r_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_id', models.CharField(max_length=100)),
                ('d_id', models.IntegerField()),
                ('s_id', models.CharField(max_length=10)),
                ('dept_id', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='STAFF',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=100)),
                ('s_age', models.IntegerField()),
                ('s_gender', models.CharField(max_length=10)),
                ('s_mobile', models.IntegerField(max_length=10)),
                ('s_department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MEDICINE',
            fields=[
                ('m_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_name', models.CharField(max_length=100)),
                ('m_unitPrice', models.IntegerField()),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.patient')),
            ],
        ),
    ]
