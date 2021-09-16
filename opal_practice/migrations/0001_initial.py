# Generated by Django 2.2.16 on 2021-09-16 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('opal', '0040_auto_20201007_1346'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('dose', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField(blank=True, help_text='The date on which the patient began receiving this treatment.', null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('drug_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('route_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('frequency_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_opal_practice_treatment_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('drug_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Drug')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('frequency_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Drugfreq')),
                ('route_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Drugroute')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_opal_practice_treatment_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SymptomComplex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('duration', models.CharField(blank=True, choices=[('3 days or less', '3 days or less'), ('4-10 days', '4-10 days'), ('11-21 days', '11-21 days'), ('22 days to 3 months', '22 days to 3 months'), ('over 3 months', 'over 3 months')], help_text='The duration for which the patient had been experiencing these symptoms when recorded.', max_length=255, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_opal_practice_symptomcomplex_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('symptoms', models.ManyToManyField(blank=True, related_name='symptoms', to='opal.Symptom')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_opal_practice_symptomcomplex_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Symptoms',
                'verbose_name_plural': 'Symptom complexes',
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PatientConsultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('when', models.DateTimeField(blank=True, null=True)),
                ('initials', models.CharField(blank=True, help_text='The initials of the user who gave the consult.', max_length=255)),
                ('discussion', models.TextField(blank=True)),
                ('reason_for_interaction_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_opal_practice_patientconsultation_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('reason_for_interaction_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.PatientConsultationReasonForInteraction')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_opal_practice_patientconsultation_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Patient Consultation',
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PastMedicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('year', models.CharField(blank=True, max_length=4)),
                ('details', models.CharField(blank=True, max_length=255)),
                ('condition_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('condition_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Condition')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_opal_practice_pastmedicalhistory_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_opal_practice_pastmedicalhistory_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'PMH',
                'verbose_name_plural': 'Past medical histories',
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('category', models.CharField(blank=True, max_length=255)),
                ('hospital', models.CharField(blank=True, max_length=255)),
                ('ward', models.CharField(blank=True, max_length=255)),
                ('bed', models.CharField(blank=True, max_length=255)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_opal_practice_location_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_opal_practice_location_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('provisional', models.BooleanField(default=False, help_text='True if the diagnosis is provisional. Defaults to False', verbose_name='Provisional?')),
                ('details', models.TextField(blank=True)),
                ('date_of_diagnosis', models.DateField(blank=True, null=True)),
                ('condition_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('condition_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Condition')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_opal_practice_diagnosis_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_opal_practice_diagnosis_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Diagnosis / Issues',
                'verbose_name_plural': 'Diagnoses',
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Demographics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('hospital_number', models.CharField(blank=True, help_text='The unique identifier for this patient at the hospital.', max_length=255, verbose_name='Demographics')),
                ('nhs_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='NHS Number')),
                ('surname', models.CharField(blank=True, max_length=255, verbose_name='Surname')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Middle Name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('religion', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Date of Death')),
                ('post_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Post Code')),
                ('gp_practice_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='GP Practice Code')),
                ('death_indicator', models.BooleanField(default=False, help_text='This field will be True if the patient is deceased.', verbose_name='Death Indicator')),
                ('title_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('marital_status_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('birth_place_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('ethnicity_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('sex_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('birth_place_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Destination')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_opal_practice_demographics_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('ethnicity_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Ethnicity')),
                ('marital_status_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.MaritalStatus')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient', verbose_name='Patient')),
                ('sex_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Gender')),
                ('title_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Title')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_opal_practice_demographics_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Demographics',
                'verbose_name_plural': 'Demographics',
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('provisional', models.BooleanField(default=False, help_text='True if the allergy is only suspected. Defaults to False.', verbose_name='Suspected?')),
                ('details', models.CharField(blank=True, max_length=255)),
                ('drug_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_opal_practice_allergies_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('drug_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Drug')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient', verbose_name='Patient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_opal_practice_allergies_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name_plural': 'Allergies',
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
