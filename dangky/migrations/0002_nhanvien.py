# Generated by Django 4.0.6 on 2022-07-15 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dangky', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NhanVien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ho_ten', models.CharField(max_length=100)),
                ('chuc_vu', models.CharField(max_length=100)),
                ('nam_sinh', models.IntegerField()),
            ],
        ),
    ]