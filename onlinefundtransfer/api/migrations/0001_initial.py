# Generated by Django 3.2.11 on 2022-01-28 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('account_number', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('pan', models.CharField(max_length=20, unique=True)),
                ('mpin', models.CharField(max_length=6, unique=True)),
                ('ac_type', models.CharField(max_length=12)),
                ('balance', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_acno', models.CharField(max_length=16)),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=120)),
                ('payment_mode', models.CharField(max_length=120)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile')),
            ],
        ),
    ]