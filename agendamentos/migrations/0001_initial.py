# Generated by Django 5.2.1 on 2025-05-31 01:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('passeios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_agendada', models.DateField()),
                ('quantidade_pessoas', models.PositiveIntegerField()),
                ('confirmado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('passeio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passeios.passeio')),
            ],
        ),
    ]
