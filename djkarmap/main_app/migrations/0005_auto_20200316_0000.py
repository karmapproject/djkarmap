# Generated by Django 3.0.4 on 2020-03-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200315_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='education',
            field=models.CharField(blank=True, choices=[('', ''), ('HS', 'زیر دیپلم'), ('BD', 'دیپلم'), ('LS', 'لیسانس'), ('MD', 'فوق لیسانس'), ('MBA', 'ام.بی.آ'), ('PhD', 'دکترا')], max_length=25),
        ),
        migrations.AddField(
            model_name='employee',
            name='thumb',
            field=models.ImageField(blank=True, upload_to='employer/thumb'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, choices=[('', ''), ('M', 'مرد'), ('F', 'زن')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='employee'),
        ),
    ]
