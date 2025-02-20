# Generated by Django 5.0.7 on 2024-08-31 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediagnostico', '0003_remove_examen_idpaciente_alter_examen_otros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='pregunta1',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='pregunta2',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='pregunta3',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='agitacion',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='cansancio',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='dabdominal',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='dcabeza',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='dmuscular',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='dojos',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='fatiga',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='fiebre',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='nauseas',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='orina',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='otros',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='pielpalida',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='respiracionRapida',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='sangrado',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='sarpuido',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='examen',
            name='vpersistentes',
            field=models.BooleanField(),
        ),
    ]
