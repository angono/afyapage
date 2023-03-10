# Generated by Django 4.1.4 on 2022-12-22 11:39

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
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ovulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('fertility_window', models.CharField(choices=[('1 day before', '1 Day Before'), ('2 days before', '2 Days Before'), ('3 days before', '3 Days Before'), ('day of', 'Day of'), ('1 day after', '1 Day After'), ('2 days after', '2 Days After'), ('3 days after', '3 Days After')], max_length=20)),
                ('ovulation_method', models.CharField(choices=[('basal body temperature', 'Basal Body Temperature'), ('ovulation predictor kit', 'Ovulation')], max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intercourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('method_of_birth_control', models.CharField(choices=[('condom', 'Condom'), ('birth control pill', 'Birth Control Pill'), ('IUD', 'IUD')], max_length=50)),
                ('pregnancy_risk', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=20)),
                ('partner', models.CharField(max_length=50)),
                ('relationship_status', models.CharField(choices=[('single', 'Single'), ('dating', 'Dating'), ('engaged', 'Engaged'), ('married', 'Married')], max_length=20)),
                ('lubrication', models.CharField(choices=[('none', 'None'), ('water-based', 'Water-Based'), ('oil-based', 'Oil-Based'), ('silicone-based', 'Silicone-Based')], max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pregnancy',
            fields=[
                ('eventmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.eventmodel')),
                ('baby_count', models.PositiveSmallIntegerField()),
                ('trimesters', models.PositiveSmallIntegerField()),
                ('weight_gain', models.DecimalField(decimal_places=2, max_digits=5)),
                ('doctor_visits', models.TextField(blank=True)),
                ('fetal_movement', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('strong', 'Strong')], max_length=20)),
                ('nutrition', models.CharField(choices=[('good', 'Good'), ('fair', 'Fair'), ('poor', 'Poor')], max_length=50)),
                ('medical_appointments', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('blog.eventmodel',),
        ),
        migrations.CreateModel(
            name='Menstruation',
            fields=[
                ('eventmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.eventmodel')),
                ('flow', models.CharField(choices=[('light', 'Light'), ('medium', 'Medium'), ('heavy', 'Heavy')], max_length=20)),
                ('pain_level', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')], max_length=20)),
                ('mood_changes', models.TextField(blank=True)),
                ('cramps', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')], max_length=20)),
                ('bloating', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')], max_length=20)),
                ('headaches', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')], max_length=20)),
                ('medication', models.CharField(choices=[('none', 'None'), ('NSAIDs', 'NSAIDs'), ('hormonal contraceptives', 'Hormonal Contraceptives'), ('other', 'Other')], max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('blog.eventmodel',),
        ),
        migrations.CreateModel(
            name='Menopause',
            fields=[
                ('eventmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.eventmodel')),
                ('symptoms', models.TextField(blank=True)),
                ('hormonal_changes', models.TextField(blank=True)),
                ('lifestyle_changes', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('blog.eventmodel',),
        ),
    ]
