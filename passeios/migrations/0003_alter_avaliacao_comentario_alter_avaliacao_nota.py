# Generated by Django 5.2.1 on 2025-06-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passeios', '0002_passeio_vagas_disponiveis_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='comentario',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
